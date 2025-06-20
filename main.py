# main.py
# FINAL VERSION: With larger fonts and a custom status message.

import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import queue

# Import the powerful functions from our other modules
from llm_handler import setup_llm
from rag_system import master_translation_pipeline

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced RAG Translator")
        self.root.geometry("850x700") # Increased window size for larger fonts

        # --- Model Loading ---
        self.llm_model = None
        self.llm_tokenizer = None
        self.model_loaded = threading.Event()

        # --- GUI Widgets (with larger fonts) ---
        # Input Text Area
        self.input_label = tk.Label(root, text="Enter Text to Translate:", font=("Helvetica", 14, "bold"))
        self.input_label.pack(pady=(10, 2))
        self.input_text = scrolledtext.ScrolledText(root, width=90, height=10, font=("Helvetica", 14), wrap=tk.WORD)
        self.input_text.pack(pady=5, padx=15, fill="both", expand=True)

        # Translate Button
        self.translate_button = tk.Button(root, text="Translate", command=self.start_translation_thread, font=("Helvetica", 14, "bold"), state=tk.DISABLED, padx=10, pady=5)
        self.translate_button.pack(pady=10)

        # Output Text Area
        self.output_label = tk.Label(root, text="Translation Result:", font=("Helvetica", 14, "bold"))
        self.output_label.pack(pady=(10, 2))
        self.output_text = scrolledtext.ScrolledText(root, width=90, height=10, font=("Helvetica", 14), wrap=tk.WORD, state=tk.DISABLED)
        self.output_text.pack(pady=5, padx=15, fill="both", expand=True)
        
        # Status Bar
        self.status_var = tk.StringVar()
        self.status_bar = tk.Label(root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W, font=("Helvetica", 11))
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # --- Threading & Queue for communication ---
        self.result_queue = queue.Queue()
        
        # Load the model in a background thread to keep the GUI responsive
        self.load_model_thread()

    def load_model_thread(self):
        self.status_var.set("Loading LLM... This may take a minute. Please wait.")
        thread = threading.Thread(target=self.load_model_worker, daemon=True)
        thread.start()

    def load_model_worker(self):
        """Worker function to load the model in the background."""
        try:
            self.llm_model, self.llm_tokenizer = setup_llm()
            self.model_loaded.set()
            self.status_var.set("Model loaded successfully. Ready to translate.")
            self.translate_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Model Loading Error", f"Failed to load the model: {e}")
            self.status_var.set("Error: Failed to load model.")

    def start_translation_thread(self):
        """Starts the translation process in a new thread."""
        source_text = self.input_text.get("1.0", tk.END).strip()
        if not source_text:
            messagebox.showwarning("Input Error", "Please enter some text to translate.")
            return

        self.translate_button.config(state=tk.DISABLED)
        
        # --- NEW: Set your custom status message ---
        self.status_var.set("I'm still running, I didn't sleep -- Joe Biden")
        
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)

        # Run the actual translation in a background thread
        thread = threading.Thread(target=self.translation_worker, args=(source_text,), daemon=True)
        thread.start()
        
        self.root.after(100, self.check_queue)

    def translation_worker(self, source_text):
        """The actual translation logic that runs in the background."""
        try:
            result = master_translation_pipeline(source_text, self.llm_model, self.llm_tokenizer)
            self.result_queue.put(result['final_translation'])
        except Exception as e:
            self.result_queue.put(f"An error occurred during translation: {e}")

    def check_queue(self):
        """Periodically checks the queue for a result from the worker thread."""
        try:
            result = self.result_queue.get(block=False)
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, result)
            self.output_text.config(state=tk.DISABLED)
            self.status_var.set("Translation complete. Ready for next input.")
            self.translate_button.config(state=tk.NORMAL)
        except queue.Empty:
            self.root.after(100, self.check_queue)

def on_closing():
    """Handles the window closing event."""
    if messagebox.askokcancel("Quit", "Do you want to exit the translator?"):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()