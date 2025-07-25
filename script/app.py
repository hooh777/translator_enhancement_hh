# app.py
# A user-friendly, graphical interface for the advanced Hybrid Translator.

import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import queue
import time

# Import the powerful functions from our other modules
from llm_handler import setup_llm, call_llm
from rag_system import master_translation_pipeline, detect_language

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Hybrid RAG Translator")
        self.root.geometry("850x700")

        # --- Model Loading ---
        self.llm_model = None
        self.llm_tokenizer = None

        # --- GUI Widgets (with larger fonts) ---
        main_frame = tk.Frame(root)
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.input_label = tk.Label(main_frame, text="Enter Text to Translate:", font=("Helvetica", 14, "bold"))
        self.input_label.pack(pady=(10, 5))
        self.input_text = scrolledtext.ScrolledText(main_frame, height=10, font=("Helvetica", 14), wrap=tk.WORD, relief=tk.SOLID, borderwidth=1)
        self.input_text.pack(pady=5, padx=5, fill="both", expand=True)

        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)
        self.translate_button = tk.Button(button_frame, text="Translate", command=self.start_translation_thread, font=("Helvetica", 14, "bold"), state=tk.DISABLED, padx=10, pady=5)
        self.translate_button.pack(side="left", padx=10)
        self.exit_button = tk.Button(button_frame, text="Exit", command=root.quit, font=("Helvetica", 14), padx=10, pady=5)
        self.exit_button.pack(side="left", padx=10)

        self.output_label = tk.Label(main_frame, text="Translation Result:", font=("Helvetica", 14, "bold"))
        self.output_label.pack(pady=(10, 5))
        self.output_text = scrolledtext.ScrolledText(main_frame, height=10, font=("Helvetica", 14), wrap=tk.WORD, relief=tk.SOLID, borderwidth=1, state=tk.DISABLED)
        self.output_text.pack(pady=5, padx=5, fill="both", expand=True)
        
        # Status Bar
        self.status_var = tk.StringVar()
        self.status_bar = tk.Label(root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W, font=("Helvetica", 11))
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # --- Threading & Queue ---
        self.result_queue = queue.Queue()
        self.load_model_thread()

    def add_message(self, message, tag):
        """Adds a message to the output history with specified formatting."""
        self.output_text.config(state='normal')
        self.output_text.insert(tk.END, message + "\n\n", tag)
        self.output_text.config(state='disabled')
        self.output_text.see(tk.END)

    def load_model_thread(self):
        self.status_var.set("Loading local LLM for polishing... Please wait.")
        thread = threading.Thread(target=self.load_model_worker, daemon=True)
        thread.start()

    def load_model_worker(self):
        """Worker function to load the model in the background."""
        try:
            self.llm_model, self.llm_tokenizer, self.device = setup_llm()
            self.status_var.set(f"Model loaded successfully. Ready to translate on {self.device.type.upper()}!")
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
        self.status_var.set("I'm still running, I didn't sleep -- Joe Biden")
        
        # Clear previous output
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)

        thread = threading.Thread(target=self.translation_worker, args=(source_text,), daemon=True)
        thread.start()
        
        self.root.after(100, self.check_queue)

    def translation_worker(self, source_text):
        """The actual translation logic that runs in the background."""
        try:
            # We use the simplified pipeline since the hybrid API one is complex for this example
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