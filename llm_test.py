# chatbot.py

import sys
import time # <-- NEW: Import the time library
from llm_handler import setup_llm, call_llm
from config import MODEL_PATH

def main():
    """Main function to run the interactive chatbot."""
    print("--- Simple Chatbot Mode ---")
    print(f"Model being used: {MODEL_PATH}")

    # --- Load the Model ---
    try:
        print("\nLoading model... This may take a moment.")
        model, tokenizer = setup_llm()
        print("\n--- Model Loaded. You can now start chatting. ---")
        print("Type 'quit' or 'exit' to end the session.")
    except Exception as e:
        print(f"\nError loading model: {e}")
        print("Please ensure your config.py points to a valid model and you are authenticated if required.")
        sys.exit(1)

    # --- Interactive Chat Loop ---
    while True:
        try:
            user_input = input("\nYou: ")

            if user_input.lower() in ["quit", "exit"]:
                print("Bot: Goodbye!")
                break
            
            # --- NEW: Start the timer ---
            start_time = time.perf_counter()

            # For a simple chat, the prompt is just the user's input.
            response = call_llm(model, tokenizer, user_input)
            
            # --- NEW: Stop the timer and calculate duration ---
            end_time = time.perf_counter()
            duration = end_time - start_time
            
            # Display the response along with the time taken
            print(f"Bot: {response} \n(Responded in {duration:.2f} seconds)")

        except KeyboardInterrupt:
            print("\nBot: Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
