# rag_system.py
# FINAL ARCHITECTURE: Uses a powerful Few-Shot RAG prompt for the highest quality translations.

import json
import re
import config
import jieba
from llm_handler import call_llm

# --- Database Loading ---
def load_terminology_db(file_path):
    """Loads the terminology database from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_reverse_dictionary(original_db):
    """Automatically creates an EN->CN dictionary."""
    reversed_db = {}
    for zh_term, en_translations in original_db.items():
        for en_term in en_translations:
            reversed_db[en_term.lower()] = zh_term
    return reversed_db

CN_TO_EN_DB = load_terminology_db(config.TERMINOLOGY_FILE)
EN_TO_CN_DB = create_reverse_dictionary(CN_TO_EN_DB)

# --- Core Logic ---
def detect_language(text: str) -> str:
    """Detects if the text is primarily Chinese or English."""
    if re.search(r'[\u4e00-\u9fff]', text):
        return 'zh'
    return 'en'

def find_terms_in_text(source_text, db, lang):
    """Finds glossary terms using a smarter, longest-match-first strategy."""
    found_terms = {}
    text_to_search = source_text
    # Sort keys by length, descending, to find "matt ink" before "matt"
    sorted_keys = sorted(db.keys(), key=len, reverse=True)

    for term in sorted_keys:
        # Use word boundaries for English to avoid matching parts of words
        pattern = r'\b' + re.escape(term) + r'\b' if lang == 'en' else re.escape(term)

        # Use re.search for case-insensitivity
        if re.search(pattern, text_to_search, re.IGNORECASE):
            # Find the actual text that matched to use as the key
            match = re.search(pattern, text_to_search, re.IGNORECASE)
            # We use the original key from the DB for consistency in the glossary
            original_db_key = term
            found_terms[match.group(0)] = db[original_db_key]
            # Blank out the found term so we don't match its substrings
            text_to_search = text_to_search.replace(match.group(0), " " * len(match.group(0)))

    return found_terms

# --- The Main Pipeline Function ---
def master_translation_pipeline(source_text: str, model, tokenizer):
    """
    Orchestrates the translation using the final, most robust prompt.
    """
    lang = detect_language(source_text)
    db = CN_TO_EN_DB if lang == 'zh' else EN_TO_CN_DB
    found_terms = find_terms_in_text(source_text, db, lang)

    # --- Prompt Generation Stage ---
    mini_glossary = "No specific terminology found."
    if found_terms:
        if lang == 'zh':
            lines = [f"- The Chinese term '{zh}' MUST be translated as one of: `{', '.join(en_list)}`" for zh, en_list in found_terms.items()]
        else: # lang == 'en'
            lines = [f"- The English term `{en}` MUST be translated as `{zh}`" for en, zh in found_terms.items()]
        mini_glossary = "\n".join(lines)

    target_language = "English" if lang == 'zh' else "Traditional Chinese (繁體中文)"

    # This prompt provides strong guidance without being overly complex
    final_prompt = f"""You are an expert translator for the printing industry. Your task is to translate the "Source Text" into fluent, high-quality {target_language}.
Strictly follow the rules in the "Terminology Glossary" and the style in the "Examples". Your final output should only be the translation itself, with no extra notes or commentary.

**Terminology Glossary:**
{mini_glossary}

**Examples:**
- English: "matt ink for the new printer" -> Chinese: "用於新打印機的哑光油墨"
- Chinese: "为最终产品要求覆膜处理。" -> English: "Request lamination for the final product."

**Source Text to Translate:**
"{source_text}"

**Final Translation:**
"""

    final_translation = call_llm(model, tokenizer, final_prompt)

    # Return the found terms map for better logging and highlighting
    return {
        "final_translation": final_translation,
        "found_terms_map": found_terms
    }