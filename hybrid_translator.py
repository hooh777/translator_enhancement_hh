# hybrid_translator.py
# FINAL ARCHITECTURE: A truly bidirectional system using the robust
# "Segment-Translate-Reassemble" workflow for both directions.

import re
import time
import googletrans
from rag_system import CN_TO_EN_DB, EN_TO_CN_DB, detect_language

def professional_translation(source_text: str) -> dict:
    """
    Executes the robust 3-step hybrid translation pipeline for any language direction.
    """
    lang = detect_language(source_text)
    
    # Determine the correct database and target language
    if lang == 'en':
        db = EN_TO_CN_DB
        target_lang_code = 'zh-tw'
        print("(Direction: EN -> CN)")
    else: # lang == 'zh'
        db = CN_TO_EN_DB
        target_lang_code = 'en'
        print("(Direction: CN -> EN)")

    # --- Step 1: Isolate and Translate Terminology ---
    sorted_terms = sorted(db.keys(), key=len, reverse=True)
    placeholders = {}
    text_to_translate = source_text
    
    for i, term in enumerate(sorted_terms):
        # Use word boundaries for English for accuracy
        pattern = r'\b' + re.escape(term) + r'\b' if lang == 'en' else re.escape(term)
        
        if re.search(pattern, text_to_translate, re.IGNORECASE):
            placeholder = f"__PLACEHOLDER_{i}__"
            
            # Get the correct translation from our DB
            # For CN->EN, we pick the first English option as the default
            correct_translation = db[term.lower()] if lang == 'en' else db[term][0]
            
            placeholders[placeholder] = correct_translation
            text_to_translate = re.sub(pattern, placeholder, text_to_translate, flags=re.IGNORECASE)

    # --- Step 2: Translate the Generic "Scaffolding" Text ---
    translator = googletrans.Translator()
    try:
        translated_scaffolding = translator.translate(text_to_translate, dest=target_lang_code).text
    except Exception as e:
        return {"error": f"Error calling translation API: {e}", "final_translation": "", "terms_applied": {}}

    # --- Step 3: Reassemble the Final Translation ---
    final_translation = translated_scaffolding
    for placeholder, correct_term in placeholders.items():
        # Use a flexible regex to find placeholders regardless of case or internal spaces
        flexible_pattern = re.compile(f'__\s*PLACEHOLDER_\s*{placeholder.split("_")[3]}\s*__', re.IGNORECASE)
        final_translation = re.sub(flexible_pattern, correct_term, final_translation)
        
    # Final cleanup to remove any extra spaces around reassembled terms
    final_translation = re.sub(r'\s*([,.;:!?])\s*', r'\1', final_translation)

    return {
        "final_translation": final_translation,
        "source_text": source_text,
        "terms_applied": placeholders
    }

if __name__ == "__main__":
    # Example Usage
    cn_source_email = """
    主旨：關於訂單 #T-5501 的最終生產規格

    大家好，

    附件是關於 #T-5501 訂單的最終生產規格，請各部門嚴格遵守。這是一個包含多種組件的複雜包装專案。客戶對品質要求極高，尤其是表面處理。我們必須確保所有細節都準確無誤。

    主要材料與工藝要求如下：
    - 主結構：使用1500克雙層灰板，確保盒子堅固不變形。
    - 表面裱紙：外部需要裱157克的克铜版纸，要求平整無氣泡。
    - 印刷油墨：所有圖案必須使用指定的哑光油墨，以避免不必要的反光。
    - 保護處理：成品需經過上光處理，然後用收缩膜進行單獨包装。
    - 內襯：盒子內部需要一個絲絨材質的内衬來保護產品。

    請注意，上光是為了增加耐磨性，而不是為了亮度。請立即準備相關材料，並在今日下班前回報物料庫存狀況。若有任何問題，請馬上提出。
    """
    
    print("--- Starting Professional Hybrid Translation (CN to EN) ---")
    start_time_cn = time.perf_counter()
    result_cn = professional_translation(cn_source_email)
    end_time_cn = time.perf_counter()
    
    print(f"\nFinal Translation:\n{result_cn['final_translation']}")
    print(f"\nTotal Time Taken: {end_time_cn - start_time_cn:.2f} seconds")
