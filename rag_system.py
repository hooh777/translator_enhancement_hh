# rag_system.py
# FINAL, SIMPLIFIED ARCHITECTURE: Uses a direct, unambiguous prompt to avoid model confusion.

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

def find_terms_in_text(source_text, db, lang):
    found_terms = {}
    text_to_search = source_text
    sorted_keys = sorted(db.keys(), key=len, reverse=True)
    for term in sorted_keys:
        pattern = r'\b' + re.escape(term) + r'\b' if lang == 'en' else re.escape(term)
        if re.search(pattern, text_to_search, re.IGNORECASE):
            match = re.search(pattern, text_to_search, re.IGNORECASE)
            found_terms[match.group(0)] = db.get(term, db.get(term.lower()))
            text_to_search = text_to_search.replace(match.group(0), " " * len(match.group(0)))
    return found_terms

# --- The Main Pipeline Function (with the new simplified prompt) ---
def master_translation_pipeline(source_text: str, model, tokenizer):
    """
    Orchestrates the translation using a direct and robust prompt.
    """
    lang = detect_language(source_text)
    db = CN_TO_EN_DB if lang == 'zh' else EN_TO_CN_DB
    found_terms = find_terms_in_text(source_text, db, lang)
    
    mini_glossary = "No specific terminology found. Translate using your general knowledge."
    if found_terms:
        if lang == 'zh':
            lines = [f"- '{zh}' must be translated as one of: {en_list}" for zh, en_list in found_terms.items()]
        else:
            lines = [f"- '{en}' MUST be translated as '{zh}'" for en, zh in found_terms.items()]
        mini_glossary = "\n".join(lines)

    target_language = "English" if lang == 'zh' else "Traditional Chinese (繁體中文)"
    
    # A new, much simpler and more direct prompt.
    final_prompt = f"""You are an expert translator. Your task is to translate the following "Source Text" into fluent, high-quality {target_language}.
You must strictly follow the rules in the "Terminology Glossary". Your final output must only be the translation itself, with no extra notes.

**Terminology Glossary:**
{mini_glossary}

**Source Text to Translate:**
"{source_text}"

**Final Translation:**
"""
    
    final_translation = call_llm(model, tokenizer, final_prompt)
        
    return {
        "final_translation": final_translation,
        "found_terms_map": found_terms
    }