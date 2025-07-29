# === File: example.py ===
# A script to demonstrate how to use the Translator class.

from translator.translator_engine import Translator
import os
import requests # Make sure requests is imported if you use its exceptions

def main():
    """Main function to run the translation example."""
    
    # ===================================================================
    # >> ACTION REQUIRED <<
    # This is where you put your API key.
    # Replace "YOUR_GROK_API_KEY" with your actual key from x.ai.
    # ===================================================================
    api_key = os.getenv("GROK_API_KEY", "YOUR_GROK_API_KEY")

    # The path to your glossary file.
    glossary_path = "glossary.json"

    # Sample text now includes Traditional Chinese characters (訂單, 覆膜, 紙板)
    # to demonstrate the automatic standardization feature.
    sample_email_traditional = """
    你好，
    
    關於訂單 #T556-B，客戶要求使用 250克銅版紙，並且表面需要做啞光覆膜處理。
    
    請確認包裝用的紙板是否已經準備好。
    
    謝謝！
    """

    try:
        # 1. Initialize the Translator object
        print("Initializing translator...")
        translator = Translator(api_key=api_key, glossary_path=glossary_path)
        
        # 2. Call the translate method
        print("\nTranslating the following text (contains Traditional characters):")
        print("---------------------------------")
        print(sample_email_traditional.strip())
        print("---------------------------------")
        
        translated_text = translator.translate(sample_email_traditional)
        
        # 3. Print the result
        print("\nTranslation Result:")
        print("---------------------------------")
        print(translated_text)
        print("---------------------------------")

    except (ValueError, requests.exceptions.RequestException) as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()