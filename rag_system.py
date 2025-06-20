# rag_system.py
# FINAL PRODUCTION VERSION: Returns detailed information for transparent logging.

import json
import re
import config
import jieba
from llm_handler import call_llm

# --- Database Loading (Unchanged) ---
def load_terminology_db(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_reverse_dictionary(original_db):
    reversed_db = {}
    for zh_term, en_translations in original_db.items():
        for en_term in en_translations:
            reversed_db[en_term.lower()] = zh_term
    return reversed_db

CN_TO_EN_DB = load_terminology_db(config.TERMINOLOGY_FILE)
EN_TO_CN_DB = create_reverse_dictionary(CN_TO_EN_DB)

# --- Core Logic (Unchanged) ---
def detect_language(text: str) -> str:
    if re.search(r'[\u4e00-\u9fff]', text):
        return 'zh'
    return 'en'

# --- MAIN PIPELINE (Updated to return more data) ---
def master_translation_pipeline(source_text: str, model, tokenizer):
    """
    Orchestrates the full 3-stage translation process and returns detailed results.
    """
    lang = detect_language(source_text)
    db = CN_TO_EN_DB if lang == 'zh' else EN_TO_CN_DB
    
    text_for_translation = source_text
    placeholder_map = {} # Maps placeholders like __TERM_0__ to their final translation
    found_terms_map = {} # Maps the original source term to its target translation
    
    # --- Integrated Find-and-Replace Loop ---
    sorted_keys = sorted(db.keys(), key=len, reverse=True)
    
    i = 0
    for term in sorted_keys:
        pattern = r'\b' + re.escape(term) + r'\b' if lang == 'en' else re.escape(term)
        match = re.search(pattern, text_for_translation, re.IGNORECASE)

        if match:
            original_term_in_text = match.group(0)
            placeholder = f" __TERM_{i}__ "
            
            # For this simplified example, we'll skip the disambiguation check
            # and assume all found terms should be replaced.
            
            target_translation = db[term][0] if lang == 'zh' else db[term]
            placeholder_map[placeholder.strip()] = target_translation
            found_terms_map[original_term_in_text] = target_translation
            
            text_for_translation = text_for_translation[:match.start()] + placeholder + text_for_translation[match.end():]
            i += 1

    # --- Translation Stage ---
    prompt_instruction = (
        "Translate the following Chinese text to fluent English." if lang == 'zh'
        else "Translate the following English text to Traditional Chinese (繁體中文)."
    )
    final_prompt = f"""
{prompt_instruction} Keep the `__TERM_...__` placeholders exactly as they are. Do not add quotes around the final translation.
Text to Translate:
"{text_for_translation}"
"""
    
    translated_masked_text = call_llm(model, tokenizer, final_prompt)
        
    # --- Post-Processing Stage ---
    final_translation = translated_masked_text
    for placeholder, final_term in placeholder_map.items():
        final_translation = final_translation.replace(placeholder.strip(), final_term)
        
    return {
        "final_translation": final_translation,
        "found_terms_map": found_terms_map, # The terms that were identified and replaced
        "detected_language": lang
    }