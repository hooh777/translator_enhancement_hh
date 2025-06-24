import re
import googletrans
from llm_handler import call_llm
from rag_system import CN_TO_EN_DB, EN_TO_CN_DB, detect_language, find_terms_in_text

# --- FUNCTION 1: For English-to-Chinese Translations ---
def professional_translation(source_text: str, model, tokenizer):
    """
    Executes the robust 3-step hybrid translation pipeline for EN->CN direction.
    Uses programmatic replacement for terminology.
    """
    lang = detect_language(source_text)
    
    # This function is specifically for EN -> CN
    db = EN_TO_CN_DB
    target_lang_code = 'zh-tw'
    # print("(Direction: EN -> CN)") # Optional: Can be uncommented for debugging

    # --- Step 1: Get Fluent Baseline Translation from API ---
    # print("   - Step 1: Getting baseline translation from external API...") # Optional
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
    # print("   - Step 2: Performing programmatic terminology correction...") # Optional
    terms_to_correct = find_terms_in_text(source_text, db, lang)
    corrected_translation = baseline_translation

    if terms_to_correct:
        # For EN->CN, we replace any leftover English terms with the correct Chinese term.
        for term_key, term_value in terms_to_correct.items():
            corrected_translation = re.sub(r'\b' + re.escape(term_key) + r'\b', term_value, corrected_translation, flags=re.IGNORECASE)
            
    # --- Step 3: Final LLM Polish ---
    # print("   - Step 3: Sending to local LLM for final fluency polish...") # Optional
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


# --- FUNCTION 2: For Chinese-to-English Translations ---
def terminology_correction_pipeline(source_text: str, model, tokenizer):
    """
    Executes a 2-step, LLM-based terminology correction pipeline for CN->EN.
    1. Gets a fast baseline translation from the Google Translate API.
    2. Uses an LLM to correct the terminology in the already-translated text.
    """
    # --- Step 1: Get Fluent Baseline Translation from API ---
    # print("   - Step 1: Getting baseline translation from external API...") # Optional
    translator = googletrans.Translator()
    try:
        baseline_english_text = translator.translate(source_text, dest='en').text
    except Exception as e:
        error_message = f"Error calling translation API: {e}"
        return {
            "final_translation": error_message,
            "baseline_translation": error_message,
            "corrected_translation": error_message,
            "terms_applied": {}
        }

    # --- Step 2: Find Relevant Terms from Original Source ---
    # print("   - Step 2: Finding relevant terms in the original source...") # Optional
    terms_to_correct = find_terms_in_text(source_text, CN_TO_EN_DB, 'zh')

    if not terms_to_correct:
        # print("   - No specific terminology found. Skipping LLM correction.") # Optional
        return {
            "final_translation": baseline_english_text,
            "baseline_translation": baseline_english_text,
            "corrected_translation": "N/A (Skipped)",
            "terms_applied": {}
        }

    # --- Step 3: Use LLM for Terminology Correction ---
    # print("   - Step 3: Sending to LLM for targeted terminology correction...") # Optional
    
    correction_rules = ""
    for term_zh, term_en_list in terms_to_correct.items():
        correction_rules += f"- The Chinese term '{term_zh}' MUST be represented in English as '{term_en_list[0]}'.\n"

    correction_prompt = f"""You are an expert technical editor. Your only task is to correct the terminology in the provided 'Text to Correct' using the 'Correction Rules'.

**Correction Rules:**
{correction_rules}
**Text to Correct:**
"{baseline_english_text}"

**Instructions:**
1. Read the 'Text to Correct'.
2. If you see any English words or phrases that are incorrect translations of the Chinese terms in the 'Correction Rules', replace them with the required English translation from the rules.
3. Return ONLY the fully corrected, final English text. Do not add any notes, comments, or explanations.

**Corrected Text:**
"""
    final_corrected_text = call_llm(model, tokenizer, correction_prompt)

    return {
        "baseline_translation": baseline_english_text,
        "corrected_translation": final_corrected_text,
        "final_translation": final_corrected_text,
        "terms_applied": terms_to_correct
    }