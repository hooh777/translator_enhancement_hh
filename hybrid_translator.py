# hybrid_translator.py
# Updated to return the map of found terms for detailed reporting.

import re
import googletrans
from llm_handler import setup_llm, call_llm
from rag_system import CN_TO_EN_DB, EN_TO_CN_DB, detect_language, find_terms_in_text

def professional_translation(source_text: str, model, tokenizer):
    """
    Executes the hybrid pipeline and returns both pre-polish and post-polish results,
    along with the terms that were applied.
    """
    lang = detect_language(source_text)
    
    if lang == 'en':
        db = EN_TO_CN_DB
        target_lang_code = 'zh-tw'
    else: # lang == 'zh'
        db = CN_TO_EN_DB
        target_lang_code = 'en'

    # Step 1: Baseline Translation from API
    translator = googletrans.Translator()
    try:
        baseline_translation = translator.translate(source_text, dest=target_lang_code).text
    except Exception as e:
        return {"error": f"Error calling translation API: {e}"}
    
    # Step 2: Programmatic Correction
    terms_to_correct = find_terms_in_text(source_text, db, lang)
    corrected_translation = baseline_translation
    if terms_to_correct:
        for term_key, term_value in terms_to_correct.items():
            if lang == 'en':
                # For EN->CN, replace the English term if the API missed it
                corrected_translation = re.sub(r'\b' + re.escape(term_key) + r'\b', term_value, corrected_translation, flags=re.IGNORECASE)
            else:
                # For CN->EN, we can try to replace common wrong synonyms if we build a map,
                # but for now, the baseline is often good. This part can be enhanced later.
                pass
            
    # Step 3: Final LLM Polish
    polish_prompt = f"""You are an expert editor. The following text is a machine translation.
Your only task is to fix any minor grammatical errors or awkward phrasing to make it sound perfectly natural.
Do not change the core meaning or the specific technical terms. Return only the polished, final text.

Text to Polish:
"{corrected_translation}"
"""
    final_polished_translation = call_llm(model, tokenizer, polish_prompt)

    return {
        "corrected_pre_polish": corrected_translation,
        "final_translation": final_polished_translation,
        "terms_applied": terms_to_correct # <-- Return the found terms
    }