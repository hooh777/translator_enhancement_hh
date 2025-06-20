# run_tests.py
# FINAL VERSION: A comprehensive A/B comparison tool that generates a beautified,
# highlighted Markdown report for human review.

import json
from datetime import datetime
import argparse
import time
import torch
import gc
import os
import re
from colorama import init, Fore, Style

from llm_handler import setup_llm, call_llm
from rag_system import master_translation_pipeline, detect_language, CN_TO_EN_DB, EN_TO_CN_DB

def highlight_terms(text, glossary_terms_map, source_lang):
    """Finds and highlights a list of terms within a body of text using Markdown backticks."""
    if not glossary_terms_map:
        return text

    # Create a comprehensive list of all possible terms to highlight (both source and target)
    all_terms_to_highlight = set()
    for source_term, target_translation in glossary_terms_map.items():
        all_terms_to_highlight.add(source_term)
        if isinstance(target_translation, list):
            all_terms_to_highlight.update(target_translation)
        else:
            all_terms_to_highlight.add(target_translation)

    # Filter out any None values that might have slipped in
    all_terms_to_highlight = {t for t in all_terms_to_highlight if t}
    
    # Sort by length to match longer terms first (e.g., 'matt ink' before 'matt')
    sorted_terms = sorted(list(all_terms_to_highlight), key=len, reverse=True)
    
    # Create a regex pattern to find any of the terms as whole words
    pattern = r'\b(' + '|'.join(map(re.escape, sorted_terms)) + r')\b'
    
    try:
        # Wrap matches in backticks, ignoring case for robustness
        highlighted_text = re.sub(pattern, r'`\1`', text, flags=re.IGNORECASE)
    except re.error:
        # Fallback in case a term creates a complex, invalid regex pattern
        highlighted_text = text

    return highlighted_text

def run_test_suite(test_file_path: str):
    """Loads a test file and runs a side-by-side comparison, creating a beautified Markdown report."""
    
    init(autoreset=True)
    OK, FAIL, INFO, HEADER, RESET = Fore.GREEN, Fore.RED, Fore.CYAN, Style.BRIGHT, Style.RESET_ALL

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    results_dir = f"test_results_{timestamp}"
    os.makedirs(results_dir, exist_ok=True)
    
    report_md_path = os.path.join(results_dir, "comparison_report.md")
    report_parts = []

    print(f"{INFO}--- Setting up the test environment ---")
    print(f"{INFO}Loading the LLM. This may take a moment...")
    llm_model, llm_tokenizer = setup_llm()

    print(f"{INFO}Loading test cases from: {test_file_path}...")
    with open(test_file_path, 'r', encoding='utf-8') as f:
        test_cases = json.load(f)
    
    print(f"{INFO}--- Found {len(test_cases)} test cases. Starting comparison run. ---")
    
    report_parts.append(f"# Translation Comparison Report: {timestamp}\n\n")
    report_parts.append(f"**Test File:** `{test_file_path}`\n\n")

    for i, test in enumerate(test_cases):
        source_text = test['source_text']
        
        print(f"\n{HEADER}{'='*15} Running Test {i+1}/{len(test_cases)}: {test['id']} {'='*15}")
        print(f"{Fore.WHITE}Source Text: {RESET}{source_text[:120]}...")

        # --- RAG Translation ---
        start_time_rag = time.perf_counter()
        rag_result_data = master_translation_pipeline(source_text, llm_model, llm_tokenizer)
        end_time_rag = time.perf_counter()
        rag_translation = rag_result_data['final_translation']
        rag_duration = end_time_rag - start_time_rag
        
        # --- Baseline Translation ---
        start_time_base = time.perf_counter()
        lang = detect_language(source_text)
        target_lang = "English" if lang == 'zh' else "Traditional Chinese (繁體中文)"
        baseline_prompt = f"Translate the following text to {target_lang}:\n\n\"{source_text}\""
        baseline_translation = call_llm(llm_model, llm_tokenizer, baseline_prompt)
        end_time_base = time.perf_counter()
        base_duration = end_time_base - start_time_base
        
        print(f"{INFO}   -> RAG Time: {rag_duration:.2f}s | Baseline Time: {base_duration:.2f}s")
        
        # --- Highlight terms for the report ---
        found_terms_for_highlight = rag_result_data['found_terms_map']
        highlighted_source = highlight_terms(source_text, found_terms_for_highlight, lang)
        highlighted_rag = highlight_terms(rag_translation, found_terms_for_highlight, lang)
        highlighted_baseline = highlight_terms(baseline_translation, found_terms_for_highlight, lang)

        # --- Build Markdown Report Part for this test ---
        report_parts.append(f"## Test {i+1}/{len(test_cases)}: {test['id']}\n\n")
        report_parts.append(f"### Source Text\n> {highlighted_source}\n\n")
        
        report_parts.append("#### Glossary Terms Identified by RAG System:\n")
        if found_terms_for_highlight:
            for term, translation in found_terms_for_highlight.items():
                report_parts.append(f"- **{term}** -> `{translation}`\n")
        else:
            report_parts.append("- None\n")
        report_parts.append("\n")

        report_parts.append(f"### Comparison of Results\n\n")
        report_parts.append(f"#### 🟢 Advanced RAG System\n")
        report_parts.append(f"*(Time Taken: {rag_duration:.2f}s)*\n")
        report_parts.append(f"> {highlighted_rag}\n\n")
        
        report_parts.append(f"#### ⚪ Baseline LLM\n")
        report_parts.append(f"*(Time Taken: {base_duration:.2f}s)*\n")
        report_parts.append(f"> {highlighted_baseline}\n\n---\n\n")
        
        # --- Stability Pause ---
        time.sleep(1)
        torch.mps.empty_cache()
        gc.collect()

    # --- Final Report Generation ---
    final_report_content = "".join(report_parts)
    with open(report_md_path, 'w', encoding='utf-8') as f:
        f.write(final_report_content)
    
    print(f"\n{Fore.GREEN}{'='*15} Test Run Complete {'='*15}")
    print(f"\n{INFO}A side-by-side comparison report has been saved to: '{report_md_path}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a comparison of RAG vs. Baseline Translation.")
    parser.add_argument("--file",type=str, default="tests/test_cases.json", help="Path to the test case JSON file to run.")
    args = parser.parse_args()
    run_test_suite(args.file)
