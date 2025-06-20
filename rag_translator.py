import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import logging
import warnings
import re

# --- 1. SETUP: LLM Loading ---

def setup_llm():
    """Loads the pre-configured MiniCPM model and tokenizer."""
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    logging.getLogger("transformers").setLevel(logging.ERROR)

    device = torch.device("mps")
    model_path = 'openbmb/MiniCPM-2B-sft-bf16'
    torch_dtype_for_mps = torch.float16

    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    print(f"Loading model to '{device}' with dtype '{torch_dtype_for_mps}'...")
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch_dtype_for_mps,
        device_map=device,
        trust_remote_code=True
    )
    return model, tokenizer

def call_llm(model, tokenizer, prompt):
    """This function calls your local LLM with the provided prompt."""
    response = model.chat(tokenizer=tokenizer, query=prompt)
    if isinstance(response, tuple):
        return response[0]
    return response

# --- 2. RAG CORE: Bidirectional Database and Language Detection ---

CN_TO_EN_DB = {
  "纸板": ["cardboard", "paperboard"],
  "内衬": ["lining"],
  "水性亮光油墨": ["water-based gloss ink"],
  "克铜版纸": ["gsm art paper", "gsm coated paper"],
  "哑光": ["matt", "matte"],
  "哑光油墨": ["matt ink", "matte ink"],
  "哑光涂层": ["matt coating", "matte coating"],
  "哑光覆膜": ["matte laminated", "matt laminated"],
  "灰板": ["greyboard"],
  "上光": ["varnishing", "coating"],
  "白卡纸": ["white card paper"],
  "收缩膜": ["shrink wrap", "shrink film"],
  "包装": ["packaging"],
  "彩盒": ["color box"],
  "紙袋": ["paper bag"],
  "紙卡": ["paper card"],
  "亞克力板": ["acrylic board", "acrylic sheet"],
  "撲克油": ["poker varnishing", "Poker Coating"],
  "裱": ["laminating"],
  "盒蓋": ["box cover", "lid"],
  "燙幻彩": ["holographic foil stamping"],
  "書紙": ["book paper"],
  "书盒": ["slipcase"],
  "卡": ["card"],
  "衬纸": ["endpaper"],
  "封裡頁": ["endpaper"],
  "硬封面": ["hardcover"],
  "精装本": ["hardcover", "hardback"],
  "書套": ["jacket"],
  "平装封面": ["paperback"],
  "软封面": ["paperback"],
  "硬板书": ["boardbook"],
  "纸板书": ["boardbook"],
  "套筒": ["sleeve"]
}

def create_reverse_dictionary(original_db):
    """Automatically creates an EN->CN dictionary from the CN->EN one."""
    reversed_db = {}
    for zh_term, en_translations in original_db.items():
        for en_term in en_translations:
            reversed_db[en_term.lower()] = zh_term
    return reversed_db

EN_TO_CN_DB = create_reverse_dictionary(CN_TO_EN_DB)

def detect_language(text: str) -> str:
    """Detects if the text is primarily Chinese or English."""
    if re.search(r'[\u4e00-\u9fff]', text):
        return 'zh'
    return 'en'

# --- 3. MAIN LOGIC: The Bidirectional RAG Function ---

def translate_with_rag(source_text: str) -> dict:
    """
    Performs the RAG process, automatically handling both CN->EN and EN->CN.
    """
    lang = detect_language(source_text)
    
    # --- THIS BLOCK IS NOW UPGRADED TO MATCH THE OTHER DIRECTION ---
    if lang == 'zh':
        db = CN_TO_EN_DB
        found_terms = {zh: en for zh, en in db.items() if zh in source_text}
        
        print(f"(DEBUG: Found glossary terms: {list(found_terms.keys())})")
        if not found_terms:
            mini_glossary = "No specific terminology found. Translate using your general knowledge."
        else:
            glossary_lines = [
                f"- The Chinese term '{zh}' MUST be translated as one of: {', '.join(f'{en}' for en in en_list)}"
                for zh, en_list in found_terms.items()
            ]
            mini_glossary = "\n".join(glossary_lines)

        final_prompt = f"""
You are a precise Chinese-to-English translator. Your instructions are absolute.

**Instructions:**
1. Your goal is to translate the "Source Text" into fluent English.
2. You MUST follow the examples below, translating full phrases and sentences correctly.
3. You MUST follow the rules in the "Terminology Glossary".

**Examples:**
- Chinese Example: "为最终产品要求覆膜处理。"
- English Translation: "Request lamination for the final product."
- Chinese Example: "用于新打印机的哑光油墨"
- English Translation: "matt ink for the new printer"

**Terminology Glossary:**
{mini_glossary}

**Source Text to Translate:**
"{source_text}"

**Final Translation:**
"""
    # --- END OF UPGRADED BLOCK ---
    else: # lang == 'en'
        db = EN_TO_CN_DB
        found_terms = {en: zh for en, zh in db.items() if re.search(r'\b' + re.escape(en) + r'\b', source_text, re.IGNORECASE)}

        print(f"(DEBUG: Found glossary terms: {list(found_terms.keys())})")
        if not found_terms:
            mini_glossary = "No specific terminology found. Translate using your general knowledge."
        else:
            glossary_lines = [
                f"- The English term '{en}' MUST be translated as '{zh}'"
                for en, zh in found_terms.items()
            ]
            mini_glossary = "\n".join(glossary_lines)
            
        final_prompt = f"""
You are a precise English-to-Chinese translator. Your instructions are absolute.

**Source Text to Translate:**
"{source_text}"

**Instructions:**
1. Your goal is to translate the "Source Text" into Traditional Chinese (繁體中文).
2. You MUST follow the examples below, translating full phrases and sentences correctly.
3. You MUST follow the rules in the "Terminology Glossary".

**Examples:**
- English Example: "matt ink for the new printer"
- Chinese Translation: "用於新打印機的哑光油墨"
- English Example: "Request lamination for the final product."
- Chinese Translation: "為最終產品要求覆膜處理。"

**Terminology Glossary:**
{mini_glossary}

**Source Text to Translate:**
"{source_text}"

**Final Translation:**
"""
    
    return {
        "detected_language": lang,
        "generated_prompt": final_prompt
    }

# --- 4. EXECUTION: Interactive Chat Loop ---

if __name__ == "__main__":
    print("--- Setting up the Bidirectional RAG Translator ---")
    print("This may take a moment as the LLM is loaded into memory...")
    
    llm_model, llm_tokenizer = setup_llm()
    
    print("\n--- Interactive Translator Ready ---")
    print("Enter a sentence in Chinese or English. Type 'quit' or 'exit' to close the program.")
    
    while True:
        try:
            source_text = input("\nTranslate: ")
            if source_text.lower() in ["quit", "exit"]:
                print("Exiting translator. Goodbye!")
                break
            rag_result = translate_with_rag(source_text)
            augmented_prompt = rag_result['generated_prompt']
            
            print(f"(Detected Language: {rag_result['detected_language']}... Translating...)", flush=True)
            final_translation = call_llm(llm_model, llm_tokenizer, augmented_prompt)
            
            print(f"Result: {final_translation}")
            print("-" * 25)
        except KeyboardInterrupt:
            print("\nExiting translator. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")