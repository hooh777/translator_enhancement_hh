# run_hybrid_tests.py
import json
from datetime import datetime
import argparse
import time
import torch
import gc
import os
import re
from colorama import init, Fore, Style

# --- MODIFIED IMPORTS ---
from llm_handler import setup_llm
from hybrid_translator import professional_translation, detect_language
from rag_system import master_translation_pipeline
# --- END MODIFICATION ---

def run_test_suite(test_file_path: str):
    """Loads a test file and runs the translation, creating a Markdown report."""
    
    init(autoreset=True)
    INFO = Fore.CYAN
    HEADER = Style.BRIGHT
    RESET = Style.RESET_ALL

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    results_dir = f"test_results_hybrid_{timestamp}"
    os.makedirs(results_dir, exist_ok=True)
    
    report_md_path = os.path.join(results_dir, "hybrid_translation_report.md")
    report_parts = []

    print(f"{INFO}--- Setting up the test environment ---")
    print(f"{INFO}Loading local LLM...")
    llm_model, llm_tokenizer, device = setup_llm()
    print(f"{Fore.GREEN}✅ Local LLM ready. Using device: {str(device).upper()}")

    print(f"{INFO}Loading test cases from: {test_file_path}...")
    with open(test_file_path, 'r', encoding='utf-8') as f:
        test_cases = json.load(f)
    
    print(f"{INFO}--- Found {len(test_cases)} test cases. Starting translation run. ---")
    
    report_parts.append(f"# Hybrid Translation Report: {timestamp}\n\n")
    report_parts.append(f"**Test File:** `{test_file_path}`\n\n")

    for i, test in enumerate(test_cases):
        source_text = test['source_text']
        
        print(f"\n{HEADER}{'='*15} Running Test {i+1}/{len(test_cases)}: {test['id']} {'='*15}")
        print(f"{Fore.WHITE}Source Text: {RESET}{source_text[:120]}...")

        # --- MODIFIED SECTION: Run Translation with Strategy Selection ---
        start_time = time.perf_counter()
        
        # Detect language to choose the correct translation strategy
        lang = detect_language(source_text)
        
        if lang == 'en':
            # For EN -> CN, the existing hybrid approach is effective.
            print(f"{INFO}   -> Using Hybrid Strategy (EN->CN)...")
            result = professional_translation(source_text, llm_model, llm_tokenizer)
            final_translation = result.get('final_translation', 'ERROR')

        else: # lang is 'zh'
            # For CN -> EN, the RAG approach is more reliable for terminology.
            # This directly addresses the failure seen in the test report.
            print(f"{INFO}   -> Using RAG Strategy (CN->EN)...")
            rag_result = master_translation_pipeline(source_text, llm_model, llm_tokenizer)
            
            # Adapt the RAG output to match the report's expected structure
            final_translation = rag_result.get('final_translation', 'ERROR')
            result = {
                'baseline_translation': 'N/A (RAG approach used)',
                'corrected_translation': 'N/A (RAG approach used)',
                'final_translation': final_translation,
                'terms_applied': rag_result.get('found_terms_map', {})
            }

        end_time = time.perf_counter()
        duration = end_time - start_time
        # --- END MODIFICATION ---

        print(f"{INFO}   -> Total Time Taken: {duration:.2f}s")
        
        # --- Build Markdown Report Part for this test ---
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
        
        # --- Stability Improvements ---
        print(f"{INFO}   Pausing and clearing cache...")
        time.sleep(1)
        if device.type == 'cuda':
            torch.cuda.empty_cache()
        elif device.type == 'mps':
            torch.mps.empty_cache()
        gc.collect()

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