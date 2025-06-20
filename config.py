# config.py
# This file contains all the configuration settings for the project.

# LLM Model Configuration# Point to the new, ultra-efficient 0.5B model


MODEL_PATH = 'openbmb/minicpm-2b-sft-bf16'
TORCH_DTYPE = 'torch.float16' 
TERMINOLOGY_FILE = 'terminology/terms.json'


"""
MODEL_PATH = 'openbmb/MiniCPM4-0.5B'
TORCH_DTYPE = 'torch.float16' 
TERMINOLOGY_FILE = 'terminology/terms.json'
"""