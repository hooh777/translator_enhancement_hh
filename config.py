# config.py
# This file contains all the configuration settings for the project.

# LLM Model Configuration
MODEL_PATH = 'openbmb/MiniCPM4-0.5B'

TORCH_DTYPE = 'torch.float16' 
TERMINOLOGY_FILE = 'terminology/terms.json'

# You can easily switch back to your main model by changing the line above to:
# MODEL_PATH = 'openbmb/MiniCPM-2B-sft-bf16'

TORCH_DTYPE = 'torch.float16' 

# File Paths
TERMINOLOGY_FILE = 'terminology/terms.json'