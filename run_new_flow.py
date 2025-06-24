import asyncio
import time
import json
from typing import List, Dict, Any, AsyncGenerator
from transformers import AutoModel, AutoTokenizer
import torch
import os
from pathlib import Path

# --- CONFIGURATION ---
# Parameters for the batching logic
BATCH_SIZE = 4
BATCH_TIMEOUT_SECONDS = 0.5  # Wait a maximum of 0.5s to fill a batch

# --- NEW CLASS FOR YOUR REAL MiniCPM MODEL ---
# You would add this class to your script.

# Make sure you have the necessary libraries installed, e.g., 'pip install transformers torch'

# --- NEW HELPER FUNCTION TO PATCH THE MODEL's BUGGY FILE ---
def patch_model_file():
    """
    Finds the problematic resampler.py file in the Hugging Face cache
    and adds the missing 'from typing import List' import.
    """
    try:
        # Construct the path to the problematic file in the cache
        cache_dir = Path.home() / ".cache" / "huggingface" / "modules"
        # Search for the resampler.py file within the model's module directory
        resampler_file = next(cache_dir.glob("**/resampler.py"))
        
        print(f"Found problematic model file at: {resampler_file}")
        
        with open(resampler_file, 'r+') as f:
            lines = f.readlines()
            # Check if the patch is already applied
            if "from typing import List" not in lines[0]:
                print("Applying patch: Adding 'from typing import List' to file...")
                f.seek(0) # Go to the beginning of the file
                f.write("from typing import List\n")
                f.writelines(lines)
                print("Patch applied successfully.")
            else:
                print("Patch already applied. No changes needed.")

    except (StopIteration, FileNotFoundError):
        print("Could not find resampler.py to patch. Maybe the model isn't downloaded yet or the path is different.")
    except Exception as e:
        print(f"An error occurred while trying to patch the file: {e}")

# --- CORRECTED CLASS ---

class RealMiniCPMLLM:
    """
    This class wraps the actual MiniCPM model and tokenizer to perform inference.
    """
    def __init__(self, model_path="openbmb/MiniCPM-Llama3-V-2_5", device=None):
        if device is None:
            if torch.backends.mps.is_available():
                device = "mps"
            elif torch.cuda.is_available():
                device = "cuda"
            else:
                device = "cpu"
        
        print(f"Initializing RealMiniCPMLLM on device: {device}...")
        
        # NOTE: The patch must be applied BEFORE loading the model
        patch_model_file()
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        
        self.model = AutoModel.from_pretrained(
            model_path,
            trust_remote_code=True,
            torch_dtype=torch.bfloat16
        ).to(device)
        self.model.eval()
        print("Real MiniCPM model loaded successfully.")

    async def generate_stream_batch(self, prompts: List[str]) -> AsyncGenerator[Dict[str, Any], None]:
        """
        This method needs to be implemented to handle batch processing and streaming
        with your actual model.
        """
        print("WARNING: Real model streaming logic is not yet implemented. Using placeholder.")
        for i, prompt in enumerate(prompts):
            mock_response = f"[REAL MODEL PLACEHOLDER for Prompt #{i+1}]"
            for token in mock_response.split():
                 await asyncio.sleep(0.05)
                 yield {"request_index": i, "token": f" {token}"}
            yield {"request_index": i, "token": None, "status": "done"}


# --- 1. MOCK LOCAL LLM (REPLACE WITH YOUR MiniCPM RUNNER) ---
# This class simulates a local MiniCPM model running on your hardware.
# It accepts a batch of prompts and streams back responses.

class MockLocalLLM:
    """
    A mock class to simulate a local LLM runner like MiniCPM.
    It introduces a fake processing delay and streams back a response.
    This version is corrected to handle batch streaming correctly.
    """
    def __init__(self, token_delay=0.03):
        print(f"MockLocalLLM initialized. Simulating a {token_delay*1000:.0f}ms delay per token.")
        self.token_delay = token_delay

    async def generate_stream_batch(self, prompts: List[str]) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Accepts a batch of prompts and yields token responses asynchronously
        by merging multiple concurrent streams using a queue.
        """
        q = asyncio.Queue()

        # This "producer" coroutine runs one stream and puts its items into the queue.
        async def producer(index, prompt):
            try:
                async for item in self._stream_single_response(index, prompt):
                    await q.put(item)
            finally:
                # When the stream is done, put a special "end" signal into the queue.
                await q.put({"request_index": index, "status": "producer_done"})

        # Start all producer tasks to run in the background concurrently.
        producer_tasks = [asyncio.create_task(producer(i, p)) for i, p in enumerate(prompts)]

        # This "consumer" loop yields items as they arrive in the queue.
        finished_producers = 0
        while finished_producers < len(prompts):
            item = await q.get()
            if item.get("status") == "producer_done":
                finished_producers += 1
            else:
                yield item
            q.task_done()

    async def _stream_single_response(self, index: int, prompt: str) -> AsyncGenerator[Dict[str, Any], None]:
        """Helper to stream a single mock response. (This function was correct and remains unchanged)"""
        # Simulate initial model processing time
        await asyncio.sleep(0.2)
        
        # A more dynamic mock response for better testing
        prompt_words = prompt.split()
        source_language = "Chinese" if "Chinese" in prompt else "English"
        mock_response = f"[Mock Response for Batch Item #{index+1}] Translating from {source_language}. Keywords: {prompt_words[-5:]}"
        
        for token in mock_response.split():
            yield {"request_index": index, "token": f" {token}"}
            # Simulate the time it takes to generate one token
            await asyncio.sleep(self.token_delay)
        
        # Signal that this specific stream's content is complete
        yield {"request_index": index, "token": None, "status": "done"}


# --- 2. WORKFLOW IMPLEMENTATION ---

def load_bidirectional_glossary() -> Dict[str, str]:
    """
    Loads the glossary and creates a bidirectional mapping for easy lookup
    in both EN->CN and CN->EN directions.
    """
    # This is the content from your provided terms.json file
    glossary_data = {
        "纸板": ["cardboard", "paperboard"], "内衬": ["lining"], "水性亮光油墨": ["water-based gloss ink"],
        "克铜版纸": ["gsm art paper", "gsm coated paper"], "哑光": ["matt", "matte"], "哑光油墨": ["matt ink", "matte ink"],
        "哑光涂层": ["matt coating", "matte coating"], "哑光覆膜": ["matte laminated", "matt laminated"],
        "灰板": ["greyboard"], "上光": ["varnishing", "coating"], "白卡纸": ["white card paper"],
        "收缩膜": ["shrink wrap", "shrink film"], "包装": ["packaging"], "彩盒": ["color box"],
        "紙袋": ["paper bag"], "紙卡": ["paper card"], "亞克力板": ["acrylic board", "acrylic sheet"],
        "撲克油": ["poker varnishing", "Poker Coating"], "裱": ["laminating"], "盒蓋": ["box cover", "lid"],
        "燙幻彩": ["holographic foil stamping"], "書紙": ["book paper"], "书盒": ["slipcase"], "卡": ["card"],
        "衬纸": ["endpaper"], "封裡頁": ["endpaper"], "硬封面": ["hardcover"], "精装本": ["hardcover", "hardback"],
        "書套": ["jacket"], "平装封面": ["paperback"], "软封面": ["paperback"], "硬板书": ["boardbook"],
        "纸板书": ["boardbook"], "套筒": ["sleeve"]
    }
    
    bidirectional_map = {}
    for chinese, english_list in glossary_data.items():
        # Use the first English translation as the canonical one
        english = english_list[0]
        bidirectional_map[chinese] = english
        bidirectional_map[english] = chinese
        
    return bidirectional_map

def prepare_prompt(source_text: str, glossary: Dict[str, str]) -> str:
    """
    Implements Dynamic Glossary Injection and Concise Instructions.
    """
    # Detect translation direction (simple check for demonstration)
    is_cn_to_en = any('\u4e00' <= char <= '\u9fff' for char in source_text)
    direction_text = "from Chinese to English" if is_cn_to_en else "from English to Chinese"

    # Dynamic Glossary Injection
    dynamic_glossary = {}
    for term, translation in glossary.items():
        if term in source_text:
            # Add the mapping relevant for the translation direction
            if is_cn_to_en:
                dynamic_glossary[term] = translation
            else:
                # Find the chinese term corresponding to the english term
                if glossary.get(term):
                    dynamic_glossary[term] = glossary[term]
    
    # Concise Instructions
    prompt = f"""Translate {direction_text}, using the provided glossary.
Glossary: {dynamic_glossary}
Text: {source_text}"""

    return prompt

async def main():
    """
    Main function to run the entire translation workflow.
    """
    # Load test cases from the provided data
    test_cases_str = """
    [
        { "id": "long_email_en_01", "source_text": "Subject: Urgent Update on Order #P-5821 - Material Change. Hi Team, Please be advised that the client has requested a change to the material specifications for their upcoming order of color boxes. The main structure must now be made from 2mm thick greyboard for added rigidity, not the standard paperboard we quoted. For the exterior, we will be laminating 157 gsm coated paper onto the surface. The final product requires individual shrink wrap for protection during shipping. Please update the bill of materials and confirm the new cost immediately. Thanks."},
        { "id": "long_email_en_02", "source_text": "Hi Sarah, Following up on the 'Galaxy' board game project. The client was very happy with the prototype but has a few final requests for the packaging. They loved the main box cover with the holographic foil stamping. For the cards themselves, they want to ensure we use a professional poker varnishing for the best feel. The box itself should be a sturdy slipcase to hold everything securely. Please confirm that these changes are feasible and let's proceed with the full production run. Best regards."},
        { "id": "long_email_cn_01", "source_text": "各位，關於訂單 #C-1024 的進度更新。客戶要求我們所有的彩盒都必須使用高品質的白卡纸來製作，以確保結構的挺度。盒子的表面處理，他們最終選擇了哑光涂层，而不是一般的上光。另外，每個獨立的彩盒在裝箱前，都需要用收缩膜進行熱縮處理。請生產部門據此更新作業流程，並回報預計的完成時間。謝謝。"},
        { "id": "long_email_cn_02", "source_text": "你好，我想詢問一下關於兒童硬板书的製作細節。我們計畫的這本書，其封面和內頁是否都使用同樣厚度的灰板？在油墨的選擇上，為了兒童安全，我們傾向於使用水性亮光油墨。此外，書本的内衬設計是否有推薦的圖案？我們希望這個包装能吸引孩子的注意。請提供相關建議，謝謝。"}
    ]
    """
    test_cases = json.loads(test_cases_str)
    
    # Initialize components
    model = RealMiniCPMLLM()
    glossary = load_bidirectional_glossary()
    
    print(f"\n--- Starting Translation Workflow ---")
    print(f"Processing {len(test_cases)} test cases with BATCH_SIZE={BATCH_SIZE}\n")
    
    # This list will hold future tasks
    all_requests = []
    results = {}

    # Create tasks for all test cases
    for test_case in test_cases:
        request = {
            "id": test_case["id"],
            "source_text": test_case["source_text"],
            "start_time": time.monotonic(),
            "translation": ""
        }
        all_requests.append(request)
        results[request['id']] = request

    # Process requests in batches
    for i in range(0, len(all_requests), BATCH_SIZE):
        batch = all_requests[i:i + BATCH_SIZE]
        batch_ids = [req['id'] for req in batch]
        print(f"--- Processing Batch: {batch_ids} ---")
        
        # Step 3: Prepare prompts for the current batch
        prompts_to_process = [prepare_prompt(req["source_text"], glossary) for req in batch]

        # Step 4 & 5: Process the batch and handle streamed responses
        async for stream_event in model.generate_stream_batch(prompts_to_process):
            request_index_in_batch = stream_event["request_index"]
            original_request = batch[request_index_in_batch]
            
            token = stream_event.get("token")
            
            if token:
                original_request["translation"] += token
            
            # Check if this specific stream is done
            if stream_event.get("status") == "done":
                end_time = time.monotonic()
                total_time = end_time - original_request["start_time"]
                
                print(f"\n[Record Complete]")
                print(f"  ID: {original_request['id']}")
                print(f"  Translation Time: {total_time:.4f} seconds")
                print(f"  Final Translation (Mock):{original_request['translation']}")
        
        print(f"--- Batch Complete ---")


if __name__ == "__main__":
    asyncio.run(main())