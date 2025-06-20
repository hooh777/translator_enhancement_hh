# llm_handler.py
# Responsibility: Loading the LLM and handling calls to it.
# UPDATED: Now automatically cleans LLM responses.

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import warnings
import logging
import config

def setup_llm():
    """Loads and returns the pre-configured LLM and tokenizer."""
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    logging.getLogger("transformers").setLevel(logging.ERROR)

    device = torch.device("mps")
    model_dtype = torch.float16 if config.TORCH_DTYPE == 'torch.float16' else torch.float32

    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(config.MODEL_PATH, trust_remote_code=True)
    print(f"Loading model to '{device}' with dtype '{model_dtype}'...")
    model = AutoModelForCausalLM.from_pretrained(
        config.MODEL_PATH,
        torch_dtype=model_dtype,
        device_map=device,
        trust_remote_code=True
    )
    return model, tokenizer

def call_llm(model, tokenizer, prompt):
    """Sends a prompt to the LLM, gets the response, and cleans it."""
    response = model.chat(tokenizer=tokenizer, query=prompt)
    
    # Get the core text if the model returns a tuple
    if isinstance(response, tuple):
        text_response = response[0]
    else:
        text_response = response
    
    # --- NEW: Clean the response ---
    # Remove leading/trailing whitespace, and then remove any surrounding quotes
    cleaned_response = text_response.strip().strip('"').strip("'").strip()
    
    return cleaned_response