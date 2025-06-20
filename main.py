# main.py
# The interactive tool for single translations. This file is stable and does not need changes.

from llm_handler import setup_llm
from rag_system import master_translation_pipeline # Imports the main translation function

def main():
    """Main function to run the interactive translator."""
    print("--- Setting up the Advanced RAG Translator ---")
    print("This may take a moment as the LLM is loaded into memory...")
    
    # Load the LLM and tokenizer once at the start.
    llm_model, llm_tokenizer = setup_llm()
    
    print("\n--- Interactive Translator Ready ---")
    print("Enter a sentence, phrase, or question. Type 'quit' or 'exit' to close.")
    
    # Start the interactive loop.
    while True:
        try:
            source_text = input("\nTranslate: ")

            if source_text.lower() in ["quit", "exit"]:
                print("Exiting translator. Goodbye!")
                break

            print(f"(Analyzing context and Translating...)", flush=True)

            # Call the master translation pipeline
            result = master_translation_pipeline(source_text, llm_model, llm_tokenizer)
            
            # Print the final, clean result
            print(f"Result: {result['final_translation']}")
            print("-" * 25)

        except KeyboardInterrupt:
            # Allow clean exit with Ctrl+C
            print("\nExiting translator. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()