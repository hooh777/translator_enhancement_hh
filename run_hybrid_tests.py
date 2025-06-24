# run_tests.py
# Final version with the requested "Glossary Terms Applied" section in the report.

import json
from datetime import datetime
import argparse
import time
import torch
import gc
import os
from colorama import init, Fore, Style

from llm_handler import setup_llm
from hybrid_translator import professional_translation

def run_test_suite(test_file_path: str):
    """Loads a test file and runs the comparison, creating a beautified report."""
    
    init(autoreset=True)
    INFO = Fore.CYAN
    HEADER = Style.BRIGHT
    RESET = Style.RESET_ALL

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    results_dir = f"test_results_{timestamp}"
    os.makedirs(results_dir, exist_ok=True)
    
    report_md_path = os.path.join(results_dir, "polish_comparison_report.md")
    report_parts = []

    print(f"{INFO}--- Setting up the test environment ---")
    print(f"{INFO}Loading the LLM. This may take a moment...")
    llm_model, llm_tokenizer, device = setup_llm()

    print(f"{INFO}Loading test cases from: {test_file_path}...")
    with open(test_file_path, 'r', encoding='utf-8') as f:
        test_cases = json.load(f)
    
    print(f"{INFO}--- Found {len(test_cases)} test cases. Starting comparison run. ---")
    
    report_parts.append(f"# Translation Polish Comparison Report: {timestamp}\n\n")
    report_parts.append(f"**Test File:** `{test_file_path}`\n\n")

    for i, test in enumerate(test_cases):
        source_text = test['source_text']
        
        print(f"\n{HEADER}{'='*15} Running Test {i+1}/{len(test_cases)}: {test['id']} {'='*15}")
        print(f"{Fore.WHITE}Source Text: {RESET}{source_text[:120]}...")

        start_time = time.perf_counter()
        result = professional_translation(source_text, llm_model, llm_tokenizer)
        duration = time.perf_counter() - start_time
        
        corrected_translation = result.get('corrected_pre_polish', 'ERROR')
        final_translation = result.get('final_translation', 'ERROR')
        
        print(f"{INFO}   -> Total Time Taken: {duration:.2f}s")
        
        # --- Build Markdown Report Part for this test ---
        report_parts.append(f"## Test {i+1}/{len(test_cases)}: {test['id']}\n\n")
        report_parts.append(f"### Source Text\n> {source_text}\n\n")

        # --- NEW: Add the Glossary Terms section to the report ---
        report_parts.append("#### Glossary Terms Applied:\n")
        if result.get('terms_applied'):
            for term, translation in result['terms_applied'].items():
                report_parts.append(f"- **{term}** -> `{translation}`\n")
        else:
            report_parts.append("- None\n")
        report_parts.append("\n")

        report_parts.append(f"### Comparison of Results\n\n")
        
        report_parts.append(f"#### ⚪ Without LLM Polish (API + Code Correction)\n")
        report_parts.append(f"> {corrected_translation}\n\n")
        
        report_parts.append(f"#### 🟢 With LLM Polish (Final Result)\n")
        report_parts.append(f"*(Total Time: {duration:.2f}s)*\n")
        report_parts.append(f"> {final_translation}\n\n---\n\n")
        
        time.sleep(1)
        if device.type != 'cpu': torch.cuda.empty_cache() if device.type == 'cuda' else torch.mps.empty_cache()
        gc.collect()

    final_report_content = "".join(report_parts)
    with open(report_md_path, 'w', encoding='utf-8') as f:
        f.write(final_report_content)
    
    print(f"\n{Fore.GREEN}{'='*15} Test Run Complete {'='*15}")
    print(f"\n{INFO}A complete report has been saved to the folder: '{results_dir}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Hybrid Translation Polish Comparison.")
    parser.add_argument("--file",type=str, default="tests/test_cases.json", help="Path to the test case JSON file to run.")
    args = parser.parse_args()
    run_test_suite(args.file)