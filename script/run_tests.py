# run_tests.py
# FINAL ARCHITECTURE: Now fully cross-platform for both Mac and Windows.

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
from rag_system import master_translation_pipeline, detect_language

def run_test_suite(test_file_path: str):
    """Loads a test file, runs a comparison, and creates a beautified Markdown report."""

    # --- Setup ---
    init(autoreset=True)
    # ... (Colorama setup is unchanged) ...
    INFO = Fore.CYAN
    HEADER = Style.BRIGHT
    RESET = Style.RESET_ALL

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    results_dir = f"test_results_{timestamp}"
    os.makedirs(results_dir, exist_ok=True)
    report_md_path = os.path.join(results_dir, "comparison_report.md")
    report_parts = []

    print(f"{INFO}--- Setting up the test environment ---")
    print(f"{INFO}Loading the LLM. This may take a moment...")
    llm_model, llm_tokenizer, device = setup_llm() # <-- Get the device object here

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

        # ... (Translation logic is unchanged) ...
        # RAG Translation
        start_time_rag = time.perf_counter()
        rag_result_data = master_translation_pipeline(source_text, llm_model, llm_tokenizer)
        rag_translation = rag_result_data['final_translation']
        rag_duration = time.perf_counter() - start_time_rag

        # Baseline Translation
        start_time_base = time.perf_counter()
        lang = detect_language(source_text)
        target_lang = "English" if lang == 'zh' else "Traditional Chinese (繁體中文)"
        baseline_prompt = f"Translate the following text to {target_lang}:\n\n\"{source_text}\""
        baseline_translation = call_llm(llm_model, llm_tokenizer, baseline_prompt)
        base_duration = time.perf_counter() - start_time_base

        print(f"{INFO}   -> RAG Time: {rag_duration:.2f}s | Baseline Time: {base_duration:.2f}s")

        # ... (Report building logic is unchanged) ...
        report_parts.append(f"## Test {i+1}/{len(test_cases)}: {test['id']}\n\n"
                            f"### Source Text\n> {source_text}\n\n"
                            f"### Comparison of Results\n\n"
                            f"#### 🟢 Advanced RAG System\n*(Time Taken: {rag_duration:.2f}s)*\n> {rag_translation}\n\n"
                            f"#### ⚪ Baseline LLM\n*(Time Taken: {base_duration:.2f}s)*\n> {baseline_translation}\n\n---\n\n")

        # --- NEW: Cross-Platform Stability Improvements ---
        print(f"{INFO}   Pausing and clearing cache...")
        time.sleep(1)
        if device.type == 'mps':
            torch.mps.empty_cache()
        elif device.type == 'cuda':
            torch.cuda.empty_cache()
        gc.collect()
        # --- END OF IMPROVEMENTS ---

    # --- Final Report Generation ---
    final_report_content = "".join(report_parts)
    with open(report_md_path, 'w', encoding='utf-8') as f:
        f.write(final_report_content)

    print(f"\n{Fore.GREEN}{'='*15} Test Run Complete {'='*15}")
    print(f"\n{INFO}A side-by-side comparison report has been saved to: '{report_md_path}'")

# ... (__main__ block remains unchanged) ...
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a comparison of RAG vs. Baseline Translation.")
    parser.add_argument("--file",type=str, default="tests/test_cases.json", help="Path to the test case JSON file to run.")
    args = parser.parse_args()
    run_test_suite(args.file)