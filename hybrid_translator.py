import re
import googletrans
from llm_handler import call_llm
# We will borrow the helper functions from rag_system.py
from rag_system import CN_TO_EN_DB, EN_TO_CN_DB, detect_language, find_terms_in_text

def professional_translation(source_text: str, model, tokenizer):
    """
    Executes the robust 3-step hybrid translation pipeline for any language direction.
    """
    lang = detect_language(source_text)
    
    # Determine the correct database and target language for the API call
    if lang == 'en':
        db = EN_TO_CN_DB
        target_lang_code = 'zh-tw'
        print("(Direction: EN -> CN)")
    else: # lang == 'zh'
        db = CN_TO_EN_DB
        target_lang_code = 'en'
        print("(Direction: CN -> EN)")

    # --- Step 1: Get Fluent Baseline Translation from API ---
    print("   - Step 1: Getting baseline translation from external API...")
    translator = googletrans.Translator()
    try:
        baseline_translation = translator.translate(source_text, dest=target_lang_code).text
    except Exception as e:
        error_message = f"Error calling translation API: {e}"
        return {
            "final_translation": error_message,
            "baseline_translation": error_message,
            "corrected_translation": error_message,
            "terms_applied": {}
        }
    
    # --- Step 2: Programmatic Terminology Correction ---
    print("   - Step 2: Performing terminology correction...")
    terms_to_correct = find_terms_in_text(source_text, db, lang)
    corrected_translation = baseline_translation

    if terms_to_correct:
        if lang == 'en':
            # For EN->CN, we replace any leftover English terms with the correct Chinese term.
            for term_key, term_value in terms_to_correct.items():
                corrected_translation = re.sub(r'\b' + re.escape(term_key) + r'\b', term_value, corrected_translation, flags=re.IGNORECASE)
        else: # lang == 'zh'
            # For CN->EN, the API might use a common synonym. We need to find and replace it.
            for term_key, term_values in terms_to_correct.items():
                # How the API likely translated the term on its own
                api_generic_translation = translator.translate(term_key, dest='en').text
                # The correct term we want (we'll use the first option)
                required_translation = term_values[0]
                
                # Replace the API's generic version with our required version
                if api_generic_translation.lower() in corrected_translation.lower():
                    # Use regex for case-insensitive replacement
                    corrected_translation = re.sub(r'\b' + re.escape(api_generic_translation) + r'\b', required_translation, corrected_translation, flags=re.IGNORECASE)
            
    # --- Step 3: Final LLM Polish ---
    print("   - Step 3: Sending to local LLM for final fluency polish...")
    polish_prompt = f"""You are an expert editor. The following text is a machine translation.
Your only task is to fix any minor grammatical errors or awkward phrasing to make it sound perfectly natural.
Do not change the core meaning or the specific technical terms. Return only the polished, final text.

Text to Polish:
"{corrected_translation}"
"""
    final_polished_translation = call_llm(model, tokenizer, polish_prompt)

    return {
        "baseline_translation": baseline_translation,
        "corrected_translation": corrected_translation,
        "final_translation": final_polished_translation,
        "terms_applied": terms_to_correct
    }