# run_hybrid_tests.py
# A test runner for the Hybrid API workflow.

import json
from datetime import datetime
import argparse
import time
import os
import re
from colorama import init, Fore, Style

# Import the new hybrid translation function
from hybrid_translator import professional_translation

def run_test_suite(test_file_path: str):
    """Loads a test file and runs the hybrid translation, creating a Markdown report."""
    
    init(autoreset=True)
    INFO = Fore.CYAN
    HEADER = Style.BRIGHT
    RESET = Style.RESET_ALL

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    results_dir = f"test_results_hybrid_{timestamp}"
    os.makedirs(results_dir, exist_ok=True)
    
    report_md_path = os.path.join(results_dir, "hybrid_translation_report.md")
    report_parts = []

    print(f"{INFO}--- Loading test cases from: {test_file_path} ---")
    with open(test_file_path, 'r', encoding='utf-8') as f:
        test_cases = json.load(f)
    
    print(f"{INFO}--- Found {len(test_cases)} test cases. Starting translation run. ---")
    
    report_parts.append(f"# Hybrid Translation Report: {timestamp}\n\n")
    report_parts.append(f"**Test File:** `{test_file_path}`\n\n")

    for i, test in enumerate(test_cases):
        source_text = test['source_text']
        
        print(f"\n{HEADER}{'='*15} Running Test {i+1}/{len(test_cases)}: {test['id']} {'='*15}")
        print(f"{Fore.WHITE}Source Text: {RESET}{source_text[:120]}...")

        # --- Run Hybrid Translation ---
        start_time = time.perf_counter()
        result = professional_translation(source_text)
        end_time = time.perf_counter()
        duration = end_time - start_time
        final_translation = result.get('final_translation', 'ERROR')
        
        print(f"{INFO}   -> Time Taken: {duration:.2f}s")
        
        # --- Build Markdown Report Part for this test ---
        report_parts.append(f"## Test {i+1}/{len(test_cases)}: {test['id']}\n\n")
        report_parts.append(f"### Source Text\n> {source_text}\n\n")
        
        report_parts.append("#### Glossary Terms Applied:\n")
        if result.get('terms_applied'):
            # THIS IS THE CORRECTED LOGIC
            for original_term, translation in result['terms_applied'].items():
                report_parts.append(f"- **{original_term}** -> `{translation}`\n")
        else:
            report_parts.append("- None\n")
        report_parts.append("\n")

        report_parts.append(f"### Final Translation\n")
        report_parts.append(f"*(Time Taken: {duration:.2f}s)*\n")
        report_parts.append(f"> {final_translation}\n\n---\n\n")
        
    # --- Final Report Generation ---
    final_report_content = "".join(report_parts)
    with open(report_md_path, 'w', encoding='utf-8') as f:
        f.write(final_report_content)
    
    print(f"\n{Fore.GREEN}{'='*15} Test Run Complete {'='*15}")
    print(f"\n{INFO}A complete report has been saved to the folder: '{results_dir}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Hybrid Translation Test Suite.")
    parser.add_argument("--file",type=str, default="tests/test_cases.json", help="Path to the test case JSON file to run.")
    args = parser.parse_args()
    run_test_suite(args.file)