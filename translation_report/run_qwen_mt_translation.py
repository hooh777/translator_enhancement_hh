import json
import os
import time
import gc
import re
from openai import OpenAI
# --- SCRIPT CONFIGURATION ---
SOURCE_EMAILS_FILE = "./source_text./source_emails.json"
GLOSSARY_FILE = "./terminology/terms.json"
OUTPUT_REPORT_FILE = "./results/qwen_mt_report_glossary_source_text.md"
MODEL_NAME = "qwen-mt-plus"

DELAY_BETWEEN_TRANSLATIONS = 0.2

# --- PROMPT TEMPLATE ---
TRANSLATION_PROMPT_TEMPLATE = "{email_body}"

# --- HELPER & METRIC FUNCTIONS (Unchanged) ---

def load_json_file(filename):
    if not os.path.exists(filename):
        print(f"ERROR: The file '{filename}' was not found.")
        return None
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"An unexpected error occurred while reading '{filename}': {e}")
        return None

def count_syllables(word):
    word = word.lower()
    if len(word) <= 3: return 1
    if word.endswith(('es', 'ed', 'e')):
        word = word[:-2] if word.endswith(('es', 'ed')) else word[:-1]
    vowels = "aeiouy"
    count = 0
    if word and word[0] in vowels: count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    return max(1, count)

def calculate_readability(text):
    words = re.findall(r'\b\w+\b', text)
    sentences = [s for s in re.split(r'[.!?]+', text) if len(s.strip()) > 0]
    num_words, num_sentences = len(words), len(sentences)
    if num_words == 0 or num_sentences == 0: return 0.0, "N/A"
    num_syllables = sum(count_syllables(word) for word in words)
    if num_words == 0:
        return 0.0, "N/A"
    score = 206.835 - 1.015 * (num_words / num_sentences) - 84.6 * (num_syllables / num_words)
    if score >= 90: interp = "Very Easy"
    elif score >= 70: interp = "Easy"
    elif score >= 60: interp = "Standard"
    elif score >= 50: interp = "Fairly Difficult"
    else: interp = "Difficult"
    return round(score, 2), interp

def find_match_in_translation(approved_translations, translated_text):
    translated_text_lower = translated_text.lower()
    for term in approved_translations:
        if ' ' in term:
            pattern = re.escape(term.lower())
        else:
            pattern = r'\b' + re.escape(term.lower()) + r'\b'
            
        if re.search(pattern, translated_text_lower):
            return term
    return None

def highlight_text(text, terms_to_highlight, is_source=False):
    highlighted_text = text
    sorted_terms = sorted(terms_to_highlight, key=len, reverse=True)

    for term in sorted_terms:
        if is_source:
            highlighted_text = re.sub(re.escape(term), f"**{term}**", highlighted_text)
        else:
            if '*' in highlighted_text:
                pattern = r'(?<!\*)\b' + re.escape(term) + r'\b(?!\*)'
            else:
                pattern = r'\b' + re.escape(term) + r'\b'

            def replacer(match):
                return f"**{match.group(0)}**"

            highlighted_text = re.sub(pattern, replacer, highlighted_text, flags=re.IGNORECASE)
    return highlighted_text

# --- Global LANGUAGES dictionary (remains here) ---
LANGUAGES = {
    "Auto Detect": "auto",
    "English": "English",
    "Chinese": "Chinese",
    "Traditional Chinese": "Traditional Chinese",
    "Japanese": "Japanese",
    "Thai": "Thai",
    "Vietnamese": "Vietnamese",
    "Cantonese": "Cantonese"
}

# --- Translation Function (now accepts LANGUAGES as an argument) ---
def translate_text(text: str, source_lang: str, target_lang: str, my_glossary: list, supported_languages: dict) -> str:
    """
    Calls Alibaba Cloud's Qwen-MT model for translation.
    Returns the full translated text (not streaming for command line).
    """
    if not text.strip():
        return "Please enter text to translate."
    
    messages = [{"role": "user", "content": text}]
    
    # Use the passed supported_languages dictionary
    translation_options = {
        "source_lang": supported_languages.get(source_lang, "auto"),
        "target_lang": supported_languages.get(target_lang, "English")
    }
    
    if my_glossary:
        translation_options["terms"] = my_glossary
    
    # If you had translation memory (tm_list), you'd add it here too:
    # my_translation_memory is not defined in this function's scope,
    # so you'd need to pass it as an argument or define it globally if used.
    # if my_translation_memory:
    #     translation_options["tm_list"] = my_translation_memory
    
    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            stream=False,
            max_tokens=2048,
            extra_body={"translation_options": translation_options})
        
        translated_content = completion.choices[0].message.content
        return translated_content
        
    except Exception as e:
        return f"Translation error: {str(e)}"

# --- Main Script Logic ---

def main():
    """Main function to run translations and generate the final report."""
    print(f"--- Qwen-MT ({MODEL_NAME}) Analysis & Report Generation Script (with Glossary) ---")

    # 1. Initialize OpenAI Client
    api_key = os.environ.get('API_KEY', "sk-e15729fcadc04744ab6798d190972fe2")
    global client # Declare client as global to allow modification
    client = OpenAI(
        api_key=api_key,
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
    )
    print("OpenAI client initialized.")

    # 2. Load Data Files
    source_emails = load_json_file(SOURCE_EMAILS_FILE)
    if source_emails is None:
        return

    # Load and process glossary INSIDE main
    original_glossary_data = {}
    formatted_glossary_for_api = []

    try:
        with open(GLOSSARY_FILE, 'r', encoding='utf-8') as f:
            original_glossary_data = json.load(f)
            for chinese_term, english_translations in original_glossary_data.items():
                if english_translations:
                    formatted_glossary_for_api.append({
                        "source": chinese_term,
                        "target": english_translations[0]
                    })
        print(f"Glossary loaded successfully from '{GLOSSARY_FILE}'.")
    except FileNotFoundError:
        print(f"Warning: '{GLOSSARY_FILE}' not found. Glossary will not be used for intervention or evaluation.")
        original_glossary_data = {}
        formatted_glossary_for_api = []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{GLOSSARY_FILE}'. Check file format.")
        original_glossary_data = {}
        formatted_glossary_for_api = []
    except Exception as e:
        print(f"An unexpected error occurred while loading glossary: {e}")
        original_glossary_data = {}
        formatted_glossary_for_api = []
    
    print("Successfully loaded source emails and glossary.")

    # 3. Process Each Email
    print("\n--- Starting Translation and Analysis Loop ---")
    report_sections, metrics_summary = [], []

    for i, email_data in enumerate(source_emails):
        case_id = email_data.get('id', f"Unknown Case {i+1}")
        source_body = email_data.get('body', '')
        source_text_full = f"{email_data.get('subject', '')}\n\n{source_body}" if email_data.get('subject') else source_body

        print(f"Processing Case {i+1} ({case_id})... ", end='', flush=True)

        # A. Get Translation from Qwen-MT
        prompt_for_model = TRANSLATION_PROMPT_TEMPLATE.format(email_body=source_text_full)
        
        translated_text = ""
        start_translation_time = time.time()
        try:
            # Pass LANGUAGES and formatted_glossary_for_api to the translate_text function
            translated_text = translate_text(
                prompt_for_model, 
                "Auto Detect", 
                "English", 
                formatted_glossary_for_api, # my_glossary argument
                LANGUAGES # supported_languages argument
            )
            print(f"Translated in {time.time() - start_translation_time:.2f}s. ", end='', flush=True)

            # --- CRITICAL FIX: Clean up potential extra output from Qwen-MT ---
            cleanup_markers = [
                "I've included some words from a bilingual dictionary.",
                "Here's a breakdown of the terms from your glossary and how they are handled in the translation:",
                "I've included some words from a bilingual dictionary."
            ]
            for marker in cleanup_markers:
                if marker in translated_text:
                    translated_text = translated_text.split(marker)[0].strip()
                    break 
            if translated_text.endswith('|'):
                translated_text = translated_text.rsplit('\n\n|', 1)[0].strip()

        except Exception as e:
            translated_text = f"TRANSLATION FAILED: {str(e)}"
            print(f"Translation failed: {str(e)}. ", end='', flush=True)

        # B. Analyze and Calculate Metrics
        table_rows, source_terms_found, translated_terms_matched = [], [], []
        terms_in_source_count, correct_matches = 0, 0

        for ch_term, en_translations_options in original_glossary_data.items():
            source_pattern = re.compile(re.escape(ch_term), re.IGNORECASE)
            
            if source_pattern.search(source_text_full):
                terms_in_source_count += 1
                source_terms_found.append(ch_term)
                
                matched_term_in_output = find_match_in_translation(en_translations_options, translated_text)
                
                if matched_term_in_output:
                    correct_matches += 1
                    translated_terms_matched.append(matched_term_in_output)
                    status, model_used = ("✅ Match", f"`{matched_term_in_output}`")
                else:
                    status, model_used = ("❌ Mismatch / Not Found", "N/A")
                
                approved_str = ", ".join([f"`{t}`" for t in en_translations_options])
                table_rows.append(f"| `{ch_term}` | {approved_str} | {model_used} | {status} |\n")

        hit_rate = (correct_matches / terms_in_source_count * 100) if terms_in_source_count > 0 else 0
        readability_score, readability_interp = calculate_readability(translated_text)
        metrics_summary.append({
            "case": f"Case {i+1}",
            "hit_rate": hit_rate,
            "hit_rate_str": f"{correct_matches}/{terms_in_source_count}",
            "readability": readability_score,
            "readability_interp": readability_interp
        })
        print("Analyzed. ", end='', flush=True)

        # C. Assemble Report Section for this Case
        highlighted_source = highlight_text(source_text_full, source_terms_found, is_source=True)
        highlighted_translation = highlight_text(translated_text, translated_terms_matched, is_source=False)
        report_sections.append(
            f"## Case {i+1}: {email_data.get('scenario', 'No Scenario Provided')}\n\n"
            "### Terminology Analysis Table\n\n"
            "| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |\n"
            "| :--- | :--- | :--- | :--- |\n"
            + "".join(table_rows) +
            "\n---\n\n"
            "### Source Text with Highlights\n\n"
            "```text\n" + highlighted_source + "\n```\n\n"
            "### Qwen-MT's Translation with Highlights\n\n"
            "```text\n" + highlighted_translation + "\n```\n\n"
            "<hr>\n\n"
        )
        
        # D. Cleanup and Delay
        gc.collect() 
        print(f"Done. Waiting {DELAY_BETWEEN_TRANSLATIONS}s.")
        time.sleep(DELAY_BETWEEN_TRANSLATIONS)

    # 4. Assemble the Final Report with Summary
    print("\n--- Assembling Final Report ---")
    avg_hit_rate = sum(m['hit_rate'] for m in metrics_summary) / len(metrics_summary) if metrics_summary else 0
    avg_readability_score = sum(m['readability'] for m in metrics_summary) / len(metrics_summary) if metrics_summary else 0
    _, avg_readability_interp = calculate_readability("This is a dummy text to get interpretation." * 5)

    summary_table = [
        f"# Translation Terminology Report (Qwen-MT {MODEL_NAME} Analysis)\n\n",
        "## Overall Metrics Summary\n\n",
        "| Case | Terminology Hit Rate | Readability Score (Interpretation) |\n",
        "| :--- | :--- | :--- |\n"
    ]
    for metric in metrics_summary:
        summary_table.append(f"| {metric['case']} | {metric['hit_rate']:.1f}% ({metric['hit_rate_str']}) | {metric['readability']} ({metric['readability_interp']}) |\n")
    summary_table.append(f"| **Average** | **{avg_hit_rate:.1f}%** | **{avg_readability_score:.1f} ({avg_readability_interp})** |\n\n<hr>\n\n")

    # 5. Write to File
    try:
        with open(OUTPUT_REPORT_FILE, 'w', encoding='utf-8') as f:
            f.writelines(summary_table)
            f.writelines(report_sections)
        print(f"\n--- SUCCESS ---")
        print(f"Report has been generated and saved as '{OUTPUT_REPORT_FILE}'.")
    except IOError as e:
        print(f"\n--- ERROR ---")
        print(f"Could not write the report to file. Reason: {e}")

if __name__ == "__main__":
    main()