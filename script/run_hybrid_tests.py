# run_hybrid_tests.py (with debug statements)
import json
from datetime import datetime
import argparse
import time
import torch
import gc
import os
import re
from colorama import init, Fore, Style

from llm_handler import setup_llm
from hybrid_translator import professional_translation, detect_language, terminology_correction_pipeline

def run_test_suite(test_file_path: str):
    """Loads a test file and runs the translation, creating a Markdown report."""
    
    print("DEBUG: --- Script starting run_test_suite function ---")
    
    init(autoreset=True)
    INFO = Fore.CYAN
    HEADER = Style.BRIGHT
    RESET = Style.RESET_ALL

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    results_dir = f"test_results_hybrid_{timestamp}"
    print(f"DEBUG: Creating results directory: {results_dir}")
    os.makedirs(results_dir, exist_ok=True)
    print("DEBUG: Directory created.")
    
    report_md_path = os.path.join(results_dir, "hybrid_translation_report.md")
    report_parts = []

    print("DEBUG: --- Calling setup_llm() to load model. This may take a while... ---")
    llm_model, llm_tokenizer, device = setup_llm()
    print("DEBUG: --- setup_llm() finished successfully. Model is loaded. ---")

    print(f"DEBUG: Loading test cases from: {test_file_path}")
    with open(test_file_path, 'r', encoding='utf-8') as f:
        test_cases = json.load(f)
    print("DEBUG: Test cases loaded successfully.")
    
    print(f"{INFO}--- Found {len(test_cases)} test cases. Starting translation run. ---")
    
    report_parts.append(f"# Hybrid Translation Report: {timestamp}\n\n")
    report_parts.append(f"**Test File:** `{test_file_path}`\n\n")

    print("DEBUG: --- Entering main test loop... ---")
    for i, test in enumerate(test_cases):
        source_text = test['source_text']
        
        print(f"\nDEBUG: --- Processing test case {i+1}/{len(test_cases)} ({test['id']}) ---")
        print(f"{HEADER}{'='*15} Running Test {i+1}/{len(test_cases)}: {test['id']} {'='*15}")
        print(f"{Fore.WHITE}Source Text: {RESET}{source_text[:120]}...")

        start_time = time.perf_counter()
        
        lang = detect_language(source_text)
        print(f"DEBUG: Language detected as '{lang}'.")
        
        if lang == 'en':
            print("DEBUG: Calling 'professional_translation' function...")
            result = professional_translation(source_text, llm_model, llm_tokenizer)
        else:
            print("DEBUG: Calling 'terminology_correction_pipeline' function...")
            result = terminology_correction_pipeline(source_text, llm_model, llm_tokenizer)
            
        print(f"DEBUG: Finished processing test case {i+1}.")
        end_time = time.perf_counter()
        duration = end_time - start_time
        final_translation = result.get('final_translation', 'ERROR')

        print(f"{INFO}   -> Total Time Taken: {duration:.2f}s")
        
        # This part just builds the report string, it should be fast.
        report_parts.append(f"## Test {i+1}/{len(test_cases)}: {test['id']}\n\n")
        report_parts.append(f"### Source Text\n> {source_text}\n\n")
        report_parts.append("#### Glossary Terms Applied:\n")
        if result.get('terms_applied'):
            for original_term, translation in result['terms_applied'].items():
                report_parts.append(f"- **{original_term}** -> `{translation}`\n")
        else:
            report_parts.append("- None\n")
        report_parts.append("\n")
        report_parts.append(f"### Translation Steps\n\n")
        report_parts.append(f"#### 1. Baseline from API\n")
        report_parts.append(f"> {result.get('baseline_translation', 'N/A')}\n\n")
        report_parts.append(f"#### 2. After Programmatic Correction\n")
        report_parts.append(f"> {result.get('corrected_translation', 'N/A')}\n\n")
        report_parts.append(f"#### 3. Final Polished Result (After Local LLM)\n")
        report_parts.append(f"*(Total Time: {duration:.2f}s)*\n")
        report_parts.append(f"> {final_translation}\n\n---\n\n")
        
        print("DEBUG: Clearing cache for next loop...")
        time.sleep(1)
        if device.type == 'cuda':
            torch.cuda.empty_cache()
        elif device.type == 'mps':
            torch.mps.empty_cache()
        gc.collect()

    print("DEBUG: --- Finished main test loop. Generating final report. ---")
    final_report_content = "".join(report_parts)
    with open(report_md_path, 'w', encoding='utf-8') as f:
        f.write(final_report_content)
    
    print(f"\n{Fore.GREEN}{'='*15} Test Run Complete {'='*15}")
    print(f"\n{INFO}A complete report has been saved to the folder: '{results_dir}'")

if __name__ == "__main__":
    print("DEBUG: --- Script entry point (__main__) reached. ---")
    parser = argparse.ArgumentParser(description="Run the Hybrid Translation Test Suite.")
    parser.add_argument("--file",type=str, default="tests/test_cases.json", help="Path to the test case JSON file to run.")
    args = parser.parse_args()
    run_test_suite(args.file)