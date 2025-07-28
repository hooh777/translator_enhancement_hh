import json
import re
import os
from thefuzz import fuzz
from opencc import OpenCC

# --- SCRIPT CONFIGURATION (Using your provided paths) ---

GLOSSARY_FILE = "./terminology/terms.json"
SOURCE_EMAILS_FILE = "./source_text/real_email.json"
TRANSLATION_FILE = "./translated_text/grok_real_email_translations.txt"
OUTPUT_FILE = "grok_report_real_email_translations.md"

# --- FUZZY MATCHING CONFIGURATION ---
FUZZY_MATCH_THRESHOLD = 90

# --- DATA LOADING FUNCTIONS ---

def load_json_file(filename):
    """Loads a JSON file and returns its content."""
    if not os.path.exists(filename):
        print(f"ERROR: The file '{filename}' was not found.")
        return None
    try:
        
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"An unexpected error occurred while reading '{filename}': {e}")
        return None

def read_translations(filename):
    """Reads the translation file and splits it into a list of translations."""
    if not os.path.exists(filename):
        print(f"ERROR: The file '{filename}' was not found.")
        return None
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        translations = [trans.strip() for trans in content.split('---NEXT---') if trans.strip()]
        return translations
    except Exception as e:
        print(f"An unexpected error occurred while reading '{filename}': {e}")
        return None

# --- METRIC CALCULATION FUNCTIONS ---

def count_syllables(word):
    """A simple heuristic to count syllables in an English word."""
    word = word.lower()
    if len(word) <= 3: return 1
    if word.endswith(('es', 'ed')) and len(word) > 4: word = word[:-2]
    vowels = "aeiouy"
    count = 0
    if word and word[0] in vowels: count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"): count -= 1
    return max(1, count)

def calculate_readability(text):
    """Calculates the Flesch Reading Ease score."""
    words = re.findall(r'\b\w+\b', text)
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if len(s.strip()) > 0]
    num_words, num_sentences = len(words), len(sentences)
    if num_words == 0 or num_sentences == 0: return 0.0, "N/A"
    num_syllables = sum(count_syllables(word) for word in words)
    score = 206.835 - 1.015 * (num_words / num_sentences) - 84.6 * (num_syllables / num_words)
    if score >= 90: interpretation = "Very Easy"
    elif score >= 70: interpretation = "Easy"
    elif score >= 60: interpretation = "Standard"
    elif score >= 50: interpretation = "Fairly Difficult"
    else: interpretation = "Difficult"
    return round(score, 2), interpretation

# --- CORE LOGIC FUNCTIONS ---

# --- NEW: More Intelligent Fuzzy Matching Logic ---
def find_fuzzy_match_in_translation(approved_translations, translated_text):
    """
    Compares glossary terms to individual words/phrases in the translation.
    Returns the word from the translation that was the best match.
    """
    best_match_score = 0
    # The actual word/phrase found in the translation
    best_match_in_text = None
    # The corresponding glossary term
    best_glossary_term = None

    # Tokenize the translated text into words, keeping punctuation
    words_in_translation = re.findall(r'\b[\w-]+\b', translated_text)

    for approved_term in approved_translations:
        num_words_in_term = len(approved_term.split())
        
        # Create n-grams from the translation to match multi-word terms
        # (e.g., if approved_term is "color box", it creates two-word phrases)
        candidate_phrases = [" ".join(words_in_translation[i:i+num_words_in_term]) 
                             for i in range(len(words_in_translation) - num_words_in_term + 1)]
        
        if not candidate_phrases:
            candidate_phrases = words_in_translation

        for phrase in candidate_phrases:
            # Use ratio for a balanced similarity score
            score = fuzz.ratio(approved_term.lower(), phrase.lower())
            if score > best_match_score:
                best_match_score = score
                best_match_in_text = phrase
                best_glossary_term = approved_term

    if best_match_score >= FUZZY_MATCH_THRESHOLD:
        # Return the word actually found in the text
        return best_match_in_text
    else:
        return None
# --- END OF NEW LOGIC ---


def highlight_text(text, terms_to_highlight, is_source=False):
    """Highlights terms within a text."""
    highlighted_text = text
    # Sort terms by length, longest first, to avoid partial highlights (e.g., "paper" in "paper bag")
    sorted_terms = sorted(terms_to_highlight, key=len, reverse=True)
    for term in sorted_terms:
        if is_source:
            highlighted_text = highlighted_text.replace(term, f"**{term}**")
        else:
            highlighted_text = re.sub(r'\b' + re.escape(term) + r'\b', f"**{term}**", highlighted_text, flags=re.IGNORECASE)
    return highlighted_text

# --- MAIN SCRIPT ---

def main():
    """Main function to load data, process it, and generate the report."""
    print("--- Starting Report Generation with Corrected Fuzzy Matching ---")

    cc = OpenCC('t2s')
    term_base = load_json_file(GLOSSARY_FILE)
    source_emails = load_json_file(SOURCE_EMAILS_FILE)
    translations = read_translations(TRANSLATION_FILE)

    if term_base is None or source_emails is None or translations is None:
        print("\nOne or more input files could not be loaded. Aborting script.")
        return

    print(f"Successfully loaded {len(term_base)} glossary terms, {len(source_emails)} source emails, and {len(translations)} translations.")

    if len(translations) != len(source_emails):
        print(f"WARNING: Found {len(translations)} translations, but expected {len(source_emails)}. Report may be incomplete.")
        if len(translations) == 0: return

    report_sections, metrics_summary = [], []

    for i, source_email in enumerate(source_emails):
        if i >= len(translations): break

        case_id = source_email.get('id', f'record_{i+1}')
        scenario = source_email.get('scenario', 'N/A')
        source_body = source_email.get('body', '')
        
        simplified_source_body = cc.convert(source_body)
        translated_block = translations[i]
        print(f"Processing {case_id}...")

        table_rows, source_terms_found, translated_terms_found = [], [], []
        terms_in_source_count, correct_matches = 0, 0

        for ch_term, en_translations in term_base.items():
            if ch_term in simplified_source_body:
                terms_in_source_count += 1
                source_terms_found.append(ch_term)
                match = find_fuzzy_match_in_translation(en_translations, translated_block)
                
                if match:
                    correct_matches += 1
                    status = "✅ Match"
                    grok_used = f"`{match}`"
                    # We add the found term (e.g., "laminated") for highlighting
                    translated_terms_found.append(match)
                else:
                    status = "❌ Mismatch / Not Found"
                    grok_used = "N/A"
                
                approved_str = ", ".join([f"`{t}`" for t in en_translations])
                table_rows.append(f"| `{ch_term}` | {approved_str} | {grok_used} | {status} |\n")
        
        hit_rate = (correct_matches / terms_in_source_count * 100) if terms_in_source_count > 0 else 0
        readability_score, readability_interp = calculate_readability(translated_block)
        metrics_summary.append({
            "case": f"Case {i+1}",
            "hit_rate": hit_rate,
            "hit_rate_str": f"{correct_matches}/{terms_in_source_count}",
            "readability": readability_score,
            "readability_interp": readability_interp
        })

        highlighted_source = highlight_text(source_body, source_terms_found, is_source=True)
        highlighted_translation = highlight_text(translated_block, translated_terms_found, is_source=False)
        
        report_sections.append(
            f"## Case {i+1}: {scenario}\n\n"
            "### Terminology Analysis Table\n\n"
            "| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |\n"
            "| :--- | :--- | :--- | :--- |\n"
            + "".join(table_rows) +
            "\n---\n\n"
            "### Source Text with Highlights\n\n"
            "```text\n" + highlighted_source + "\n```\n\n"
            "### Grok's Translation with Highlights\n\n"
            "```text\n" + highlighted_translation + "\n```\n\n"
            "<hr>\n\n"
        )

    # --- Metrics Summary and Report Writing (Unchanged) ---
    total_hit_rate = sum(m['hit_rate'] for m in metrics_summary)
    avg_hit_rate = total_hit_rate / len(metrics_summary) if metrics_summary else 0
    total_readability = sum(m['readability'] for m in metrics_summary)
    avg_readability = total_readability / len(metrics_summary) if metrics_summary else 0
    _, avg_readability_interp = calculate_readability(" ".join(["a"] * int(avg_readability)))

    summary_table = [
        "# Translation Terminology Report (Grok Analysis)\n\n",
        "## Overall Metrics Summary\n\n",
        "| Case | Terminology Hit Rate | Readability Score (Interpretation) |\n",
        "| :--- | :--- | :--- |\n"
    ]
    for metric in metrics_summary:
        summary_table.append(f"| {metric['case']} | {metric['hit_rate']:.1f}% ({metric['hit_rate_str']}) | {metric['readability']} ({metric['readability_interp']}) |\n")
    
    summary_table.append(f"| **Average** | **{avg_hit_rate:.1f}%** | **{avg_readability:.1f} ({avg_readability_interp})** |\n\n<hr>\n\n")

    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.writelines(summary_table)
            f.writelines(report_sections)
        print(f"\n--- SUCCESS ---")
        print(f"Report with metrics has been generated and saved as '{OUTPUT_FILE}'.")
    except IOError as e:
        print(f"\n--- ERROR ---")
        print(f"Could not write the report to '{OUTPUT_FILE}'. Reason: {e}")

if __name__ == "__main__":
    main()
