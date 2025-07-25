import json
import re
import os

# --- SCRIPT CONFIGURATION ---

# Define the names of the input and output files.
GLOSSARY_FILE = "glossary.json"
SOURCE_EMAILS_FILE = "./source_text/confusing_case.json"
TRANSLATION_FILE = "./translated_text/grok_translations_confusing_with_terms.txt"
OUTPUT_FILE = "grok_report_confusing_with_terms.md"

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
    except json.JSONDecodeError:
        print(f"ERROR: The file '{filename}' is not a valid JSON file. Please check its content.")
        return None
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
    # Handle some common exceptions
    if len(word) <= 3:
        return 1
    if word.endswith(('es', 'ed')) and len(word) > 4:
        word = word[:-2]
    
    vowels = "aeiouy"
    count = 0
    # Count groups of consecutive vowels
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    # Adjust for silent 'e' at the end
    if word.endswith("e"):
        count -= 1
    # Ensure at least one syllable
    return max(1, count)

def calculate_readability(text):
    """
    Calculates the Flesch Reading Ease score.
    Higher scores mean easier to read.
    """
    # Clean up the text for analysis
    words = re.findall(r'\b\w+\b', text)
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if len(s.strip()) > 0]

    num_words = len(words)
    num_sentences = len(sentences)
    num_syllables = sum(count_syllables(word) for word in words)

    if num_words == 0 or num_sentences == 0:
        return 0.0, "N/A"

    # Flesch Reading Ease formula
    score = 206.835 - 1.015 * (num_words / num_sentences) - 84.6 * (num_syllables / num_words)
    
    # Interpretation of the score
    if score >= 90:
        interpretation = "Very Easy"
    elif score >= 80:
        interpretation = "Easy"
    elif score >= 70:
        interpretation = "Fairly Easy"
    elif score >= 60:
        interpretation = "Standard"
    elif score >= 50:
        interpretation = "Fairly Difficult"
    elif score >= 30:
        interpretation = "Difficult"
    else:
        interpretation = "Very Difficult"
        
    return round(score, 2), interpretation

# --- CORE LOGIC FUNCTIONS ---

def find_match_in_translation(approved_translations, translated_text):
    """Checks for a case-insensitive, whole-word match."""
    for term in approved_translations:
        if re.search(r'\b' + re.escape(term) + r'\b', translated_text, re.IGNORECASE):
            return term
    return None

def highlight_text(text, terms_to_highlight, is_source=False):
    """Highlights terms within a text."""
    highlighted_text = text
    if is_source:
        for term in terms_to_highlight:
            highlighted_text = highlighted_text.replace(term, f"**{term}**")
    else:
        for term in terms_to_highlight:
            highlighted_text = re.sub(r'\b' + re.escape(term) + r'\b', f"**{term}**", highlighted_text, flags=re.IGNORECASE)
    return highlighted_text

# --- MAIN SCRIPT ---

def main():
    """Main function to load data, process it, and generate the report."""
    print("--- Starting Report Generation with Metrics ---")

    # Load all data
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

    report_sections = []
    metrics_summary = []

    # Process each email and translation
    for i, source_email in enumerate(source_emails):
        if i >= len(translations): break

        case_id, scenario, source_body = source_email['id'], source_email['scenario'], source_email['body']
        translated_block = translations[i]
        print(f"Processing {case_id}: {scenario}...")

        # --- 1. Terminology Analysis ---
        table_rows, source_terms_found, translated_terms_found = [], [], []
        terms_in_source_count = 0
        correct_matches = 0

        for ch_term, en_translations in term_base.items():
            if ch_term in source_body:
                terms_in_source_count += 1
                source_terms_found.append(ch_term)
                match = find_match_in_translation(en_translations, translated_block)
                
                if match:
                    correct_matches += 1
                    status = "✅ Match"
                    grok_used = f"`{match}`"
                    translated_terms_found.append(match)
                else:
                    status = "❌ Mismatch / Not Found"
                    grok_used = "N/A"
                
                approved_str = ", ".join([f"`{t}`" for t in en_translations])
                table_rows.append(f"| `{ch_term}` | {approved_str} | {grok_used} | {status} |\n")
        
        # --- 2. Calculate Metrics for this case ---
        hit_rate = (correct_matches / terms_in_source_count * 100) if terms_in_source_count > 0 else 0
        readability_score, readability_interp = calculate_readability(translated_block)
        metrics_summary.append({
            "case": f"Case {i+1}",
            "hit_rate": hit_rate,
            "hit_rate_str": f"{correct_matches}/{terms_in_source_count}",
            "readability": readability_score,
            "readability_interp": readability_interp
        })

        # --- 3. Highlight Texts ---
        highlighted_source = highlight_text(source_body, source_terms_found, is_source=True)
        highlighted_translation = highlight_text(translated_block, translated_terms_found, is_source=False)
        
        # --- 4. Assemble Markdown for this Case ---
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

    # --- 5. Create the Overall Metrics Summary Table ---
    total_hit_rate = sum(m['hit_rate'] for m in metrics_summary)
    avg_hit_rate = total_hit_rate / len(metrics_summary) if metrics_summary else 0
    total_readability = sum(m['readability'] for m in metrics_summary)
    avg_readability = total_readability / len(metrics_summary) if metrics_summary else 0
    _, avg_readability_interp = calculate_readability(" ".join(["a"] * int(avg_readability))) # Hack to get interpretation

    summary_table = [
        "# Translation Terminology Report (Grok Analysis)\n\n",
        "## Overall Metrics Summary\n\n",
        "| Case | Terminology Hit Rate | Readability Score (Interpretation) |\n",
        "| :--- | :--- | :--- |\n"
    ]
    for metric in metrics_summary:
        summary_table.append(f"| {metric['case']} | {metric['hit_rate']:.1f}% ({metric['hit_rate_str']}) | {metric['readability']} ({metric['readability_interp']}) |\n")
    
    summary_table.append(f"| **Average** | **{avg_hit_rate:.1f}%** | **{avg_readability:.1f} ({avg_readability_interp})** |\n\n<hr>\n\n")

    # --- 6. Write the final report ---
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