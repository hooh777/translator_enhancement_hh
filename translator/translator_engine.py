# === File: translator/translator_engine.py (Corrected) ===

import json
import requests
from opencc import OpenCC

class Translator:
    """
    A self-contained object to translate Chinese text to English using the Grok API,
    with support for a custom glossary and automatic conversion to Simplified Chinese.
    """
    
    _GROK_API_URL = "https://api.x.ai/v1/chat/completions"
    _MODEL_NAME = "grok-3" # You can change this to the Grok-3 model when you have the name

    def __init__(self, api_key: str, glossary_path: str = "glossary.json"):
        """
        Initializes the Translator object.
        """
        if not api_key:
            raise ValueError("API key cannot be empty.")
            
        self.api_key = api_key
        self.glossary_path = glossary_path
        
        # ===================================================================
        # >> THE FIX IS HERE <<
        # Initialize OpenCC without the .json extension.
        # Change from OpenCC('t2s.json') to OpenCC('t2s').
        # ===================================================================
        self.cc = OpenCC('t2s') 
        
        self.glossary = self._load_glossary()

    def _load_glossary(self) -> dict:
        """Private method to load the glossary from the specified JSON file."""
        try:
            with open(self.glossary_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: Glossary file not found at '{self.glossary_path}'.")
            return {}
        except json.JSONDecodeError:
            print(f"Warning: Could not decode JSON from '{self.glossary_path}'.")
            return {}
            
    def _standardize_to_simplified(self, text: str) -> str:
        """Private method to convert Traditional Chinese text to Simplified Chinese."""
        return self.cc.convert(text)

    def _find_terms_in_text(self, text: str) -> dict:
        """Private method to scan the input text for terms present in the glossary."""
        found_terms = {}
        if not self.glossary:
            return found_terms
        for term, translations in self.glossary.items():
            if term in text:
                found_terms[term] = translations
        return found_terms

    def _build_prompt(self, text_to_translate: str, found_terms: dict) -> str:
        """Private method to dynamically build the system prompt for the LLM."""
        system_prompt = (
            "You are a professional translator specializing in business communication for the printing industry. "
            "Translate the user's Chinese email into professional, natural-sounding English. "
            "Do not add any commentary, preamble, or notes. Provide only the translated English text."
        )
        if found_terms:
            glossary_instruction = (
                "\n\nCRITICAL: You must use the following specific translations for these terms. "
                "For terms with multiple options, choose the one that best fits the context:\n"
            )
            for term, translations in found_terms.items():
                translations_str = ", ".join(f"'{t}'" for t in translations)
                glossary_instruction += f"- For '{term}', use one of: [{translations_str}]\n"
            system_prompt += glossary_instruction
        return system_prompt

    def translate(self, text_to_translate: str) -> str:
        """Translates a string of Chinese text into English."""
        simplified_text = self._standardize_to_simplified(text_to_translate)
        found_terms = self._find_terms_in_text(simplified_text)
        system_prompt = self._build_prompt(simplified_text, found_terms)

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self._MODEL_NAME,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": simplified_text} 
            ],
            "temperature": 0.3,
            "max_tokens": 4096
        }

        try:
            response = requests.post(self._GROK_API_URL, headers=headers, json=payload, timeout=90)
            response.raise_for_status()
            response_data = response.json()
            if response_data.get("choices") and response_data["choices"][0].get("message"):
                return response_data["choices"][0]["message"]["content"].strip()
            else:
                raise ValueError("Invalid API response format.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the API request: {e}")
            raise
