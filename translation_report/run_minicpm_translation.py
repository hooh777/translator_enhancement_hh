import json
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import time
import gc
import re

# --- SCRIPT CONFIGURATION ---
SOURCE_EMAILS_FILE = "source_emails.json"
GLOSSARY_FILE = "glossary.json"
OUTPUT_REPORT_FILE = "minicpm8B_report_with_glossary.md"
MODEL_PATH = "openbmb/MiniCPM4-8B"
DELAY_BETWEEN_TRANSLATIONS = 0.5

# --- PROMPT TEMPLATE ---
TRANSLATION_PROMPT_TEMPLATE = """You are an expert translator specializing in technical documents for the printing, packaging, and book manufacturing industry. Your primary task is to translate the provided text into professional, clear, and accurate business English.

**CRITICAL INSTRUCTION:** You MUST use the provided terminology glossary. For any Chinese term listed in the glossary below, you must use one of its approved English translations from the list. Do not use any other translation for these specific terms.

### Terminology Glossary
```json
{glossary_json}
```

### Additional Rules
1.  **Tone:** Maintain a professional and direct business communication style.
2.  **Mixed Language:** Preserve original English terms, numbers, and abbreviations (e.g., 'A4', '4C+4C') and integrate them naturally.
3.  **Output Format:** Provide ONLY the translated English text. Do not add any introductory phrases, explanations, or conversational filler like 'Here is the translation:'.

Now, strictly following the glossary, translate the following text:

{email_body}
"""

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
    if word.endswith(('es', 'ed')): word = word[:-2]
    vowels = "aeiouy"
    count = 0
    if word and word[0] in vowels: count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"): count -= 1
    return max(1, count)

def calculate_readability(text):
    words = re.findall(r'\b\w+\b', text)
    sentences = [s for s in re.split(r'[.!?]+', text) if len(s.strip()) > 0]
    num_words, num_sentences = len(words), len(sentences)
    if num_words == 0 or num_sentences == 0: return 0.0, "N/A"
    num_syllables = sum(count_syllables(word) for word in words)
    score = 206.835 - 1.015 * (num_words / num_sentences) - 84.6 * (num_syllables / num_words)
    if score >= 90: interp = "Very Easy"
    elif score >= 70: interp = "Easy"
    elif score >= 60: interp = "Standard"
    elif score >= 50: interp = "Fairly Difficult"
    else: interp = "Difficult"
    return round(score, 2), interp

def find_match_in_translation(approved_translations, translated_text):
    for term in approved_translations:
        if re.search(r'\b' + re.escape(term) + r'\b', translated_text, re.IGNORECASE):
            return term
    return None

def highlight_text(text, terms_to_highlight, is_source=False):
    highlighted_text = text
    for term in terms_to_highlight:
        if is_source:
            highlighted_text = highlighted_text.replace(term, f"**{term}**")
        else:
            highlighted_text = re.sub(r'\b' + re.escape(term) + r'\b', f"**{term}**", highlighted_text, flags=re.IGNORECASE)
    return highlighted_text

# --- MAIN SCRIPT LOGIC ---

def main():
    """Main function to run translations and generate the final report."""
    print("--- MiniCPM Analysis & Report Generation Script (with Glossary Prompt) ---")

    # 1. Load Data Files
    if not torch.cuda.is_available():
        print("\nERROR: No NVIDIA GPU detected. Aborting script.")
        return
    device = "cuda"
    print(f"GPU detected: {torch.cuda.get_device_name(0)}")

    source_emails = load_json_file(SOURCE_EMAILS_FILE)
    term_base = load_json_file(GLOSSARY_FILE)
    if source_emails is None or term_base is None: return

    # --- FIXED: Prepare the glossary string ONCE outside the loop ---
    glossary_json_string = json.dumps(term_base, ensure_ascii=False, indent=4)
    print("Successfully loaded data and prepared glossary.")
    # --- End of Fix ---

    # 2. Load LLM Model
    print(f"\nLoading model '{MODEL_PATH}'...")
    start_time = time.time()
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, trust_remote_code=True, torch_dtype=torch.bfloat16, device_map=device)
        model.eval()
    except Exception as e:
        print(f"\nERROR: Failed to load the model. Details: {e}")
        return
    print(f"Model loaded successfully in {time.time() - start_time:.2f} seconds.")

    # 3. Process Each Email
    print("\n--- Starting Translation and Analysis Loop ---")
    report_sections, metrics_summary = [], []

    for i, email_data in enumerate(source_emails):
        case_id, source_body = email_data['id'], email_data['body']
        print(f"Processing Case {i+1} ({case_id})... ", end='', flush=True)

        # A. Get Translation
        # --- FIXED: Assemble the full prompt in one step inside the loop ---
        prompt_for_model = TRANSLATION_PROMPT_TEMPLATE.format(
            glossary_json=glossary_json_string,
            email_body=source_body
        )
        # --- End of Fix ---

        with torch.no_grad():
            translated_text, _ = model.chat(tokenizer, prompt_for_model, temperature=0.5, top_p=0.8)
        print("Translated. ", end='', flush=True)
        
        # B. Analyze and Calculate Metrics
        table_rows, source_terms_found, translated_terms_found = [], [], []
        terms_in_source_count, correct_matches = 0, 0

        for ch_term, en_translations in term_base.items():
            if ch_term in source_body:
                terms_in_source_count += 1
                source_terms_found.append(ch_term)
                match = find_match_in_translation(en_translations, translated_text)
                if match:
                    correct_matches += 1
                    translated_terms_found.append(match)
                status, model_used = ("✅ Match", f"`{match}`") if match else ("❌ Mismatch / Not Found", "N/A")
                approved_str = ", ".join([f"`{t}`" for t in en_translations])
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
        highlighted_source = highlight_text(source_body, source_terms_found, is_source=True)
        highlighted_translation = highlight_text(translated_text, translated_terms_found, is_source=False)
        report_sections.append(
            f"## Case {i+1}: {email_data['scenario']}\n\n"
            "### Terminology Analysis Table\n\n"
            "| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |\n"
            "| :--- | :--- | :--- | :--- |\n"
            + "".join(table_rows) +
            "\n---\n\n"
            "### Source Text with Highlights\n\n"
            "```text\n" + highlighted_source + "\n```\n\n"
            "### MiniCPM's Translation with Highlights\n\n"
            "```text\n" + highlighted_translation + "\n```\n\n"
            "<hr>\n\n"
        )
        
        # D. Cleanup and Delay
        gc.collect()
        torch.cuda.empty_cache()
        print(f"Done. Waiting {DELAY_BETWEEN_TRANSLATIONS}s.")
        time.sleep(DELAY_BETWEEN_TRANSLATIONS)

    # 4. Assemble the Final Report with Summary
    print("\n--- Assembling Final Report ---")
    avg_hit_rate = sum(m['hit_rate'] for m in metrics_summary) / len(metrics_summary) if metrics_summary else 0
    avg_readability = sum(m['readability'] for m in metrics_summary) / len(metrics_summary) if metrics_summary else 0
    _, avg_readability_interp = calculate_readability(" ".join(["a"]*int(avg_readability)))

    summary_table = [
        f"# Translation Terminology Report (MiniCPM {MODEL_PATH} Analysis)\n\n",
        "## Overall Metrics Summary\n\n",
        "| Case | Terminology Hit Rate | Readability Score (Interpretation) |\n",
        "| :--- | :--- | :--- |\n"
    ]
    for metric in metrics_summary:
        summary_table.append(f"| {metric['case']} | {metric['hit_rate']:.1f}% ({metric['hit_rate_str']}) | {metric['readability']} ({metric['readability_interp']}) |\n")
    summary_table.append(f"| **Average** | **{avg_hit_rate:.1f}%** | **{avg_readability:.1f} ({avg_readability_interp})** |\n\n<hr>\n\n")

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
