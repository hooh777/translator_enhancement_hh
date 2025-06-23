# llm_handler.py
# FINAL VERSION: Now with cross-platform support for CUDA, Apple MPS, and CPU.

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import warnings
import logging
import config

def get_best_device():
    """Automatically detects and returns the best available device."""
    if torch.cuda.is_available():
        print("CUDA (NVIDIA GPU) is available. Using CUDA.")
        return torch.device("cuda")
    elif torch.backends.mps.is_available():
        print("MPS (Apple Silicon GPU) is available. Using MPS.")
        return torch.device("mps")
    else:
        print("No GPU found. Falling back to CPU. This will be slower.")
        return torch.device("cpu")

def setup_llm():
    """Loads and returns the pre-configured LLM and tokenizer on the best available device."""
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    logging.getLogger("transformers").setLevel(logging.ERROR)

    device = get_best_device()

    # On CPU, float16 is not always fully supported. It's safer to use the default.
    model_dtype = torch.float16 if device.type != 'cpu' else None

    print(f"Loading tokenizer for model: {config.MODEL_PATH}")
    tokenizer = AutoTokenizer.from_pretrained(config.MODEL_PATH, trust_remote_code=True)

    print(f"Loading model to '{device}'...")
    model = AutoModelForCausalLM.from_pretrained(
        config.MODEL_PATH,
        torch_dtype=model_dtype,
        trust_remote_code=True
    )

    if device.type != 'cpu':
        model.to(device)

    return model, tokenizer, device # Return the device for use elsewhere

def call_llm(model, tokenizer, prompt):
    """Sends a prompt to the LLM, gets the response, and cleans it."""
    # This function remains the same, as it's independent of the device.
    response = model.chat(tokenizer=tokenizer, query=prompt)

    if isinstance(response, tuple):
        text_response = response[0]
    else:
        text_response = response

    cleaned_response = text_response.strip().strip('"').strip("'").strip()

    return cleaned_response