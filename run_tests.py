# run_tests.py
# FINAL VERSION: A streamlined test runner that generates a single report for human review.

import json
import logging
from datetime import datetime
import argparse
import time
import torch
import gc
import os
from llm_handler import setup_llm, call_llm
from rag_system import master_translation_pipeline

def setup_logger(log_filename):
    """Sets up a logger to output to both console and a file."""
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    if logger.hasHandlers():
        logger.handlers.clear()
    os.makedirs(os.path.dirname(log_filename), exist_ok=True)
    file_handler = logging.FileHandler(log_filename, 'w', 'utf-8')
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter('%(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    return logger

def run_test_suite(test_file_path: str):
    """Loads a test case file, runs the translations, and saves all results to a single summary file."""
    
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    results_dir = f"test_results_{timestamp}"
    log_filename = os.path.join(results_dir, "full_run_details.log")
    logger = setup_logger(log_filename)

    logger.info("--- Setting up the test environment ---")
    logger.info("Loading the LLM. This may take a moment...")
    llm_model, llm_tokenizer = setup_llm()

    logger.info(f"Loading test cases from: {test_file_path}...")
    with open(test_file_path, 'r', encoding='utf-8') as f:
        test_cases = json.load(f)
    
    logger.info(f"--- Found {len(test_cases)} test cases. Starting translation run. ---")
    
    all_results = []

    for i, test in enumerate(test_cases):
        logger.info(f"\n--- Running Test {i+1}/{len(test_cases)}: {test['id']} ---")
        logger.info(f"Source Text: \"{test['source_text']}\"")

        # Call the master translation pipeline
        result = master_translation_pipeline(test['source_text'], llm_model, llm_tokenizer)
        final_translation = result['final_translation']
        
        # Log the identified terms before showing the result
        logger.info("--- Glossary Terms Identified and Replaced ---")
        if result['found_terms_map']:
            for term, translation in result['found_terms_map'].items():
                logger.info(f"  - Found '{term}' -> Translated as '{translation}'")
        else:
            logger.info("  - None")
        logger.info("--------------------------------------------")
        
        logger.info(f"Final Result: \"{final_translation}\"")

        # Create a summary object for the final report
        result_summary = {
            "id": test['id'],
            "source_text": test['source_text'],
            "final_translation": final_translation,
            "glossary_terms_applied": result['found_terms_map']
        }
        all_results.append(result_summary)
        
        logger.info("-" * 20)
        
        # Stability improvements
        logger.info("Pausing for 2 seconds and clearing cache...")
        time.sleep(2)
        torch.mps.empty_cache()
        gc.collect()

    # --- Write the single summary file with all results ---
    summary_file = os.path.join(results_dir, "translation_summary_for_review.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)

    logger.info("\n--- Test Run Complete ---")
    print(f"\nDetailed log saved to the folder: '{results_dir}'")
    print(f"A consolidated summary for your review has been saved to: '{summary_file}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the RAG Translator Test Suite.")
    parser.add_argument(
        "--file",
        type=str,
        default="tests/test_cases.json",
        help="Path to the test case JSON file to run."
    )
    args = parser.parse_args()
    run_test_suite(args.file)