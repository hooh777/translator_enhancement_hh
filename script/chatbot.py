# chatbot.py
# A user-friendly, graphical chatbot interface for the MiniCPM model.

import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import queue
import time

# Import the powerful functions from our other modules
from llm_handler import setup_llm, call_llm
from config import MODEL_PATH

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MiniCPM Chatbot")
        self.root.geometry("800x750")

        # --- Model Loading ---
        self.llm_model = None
        self.llm_tokenizer = None

        # --- GUI Widgets ---
        # Main Frame
        main_frame = tk.Frame(root)
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Chat History Display
        self.chat_history = scrolledtext.ScrolledText(main_frame, state='disabled', height=20, wrap=tk.WORD, font=("Helvetica", 14))
        self.chat_history.pack(padx=10, pady=10, fill="both", expand=True)
        # Configure colors for user and bot messages
        self.chat_history.tag_config('user', foreground="#007bff") # Blue for user
        self.chat_history.tag_config('bot', foreground="#28a745")  # Green for bot
        self.chat_history.tag_config('info', foreground="#6c757d", font=("Helvetica", 10, "italic")) # Gray/italic for info

        # Input Frame
        input_frame = tk.Frame(main_frame)
        input_frame.pack(padx=10, pady=(5, 10), fill="x")

        # Input Text Box
        self.input_text = tk.Text(input_frame, height=3, font=("Helvetica", 14))
        self.input_text.pack(side="left", fill="x", expand=True)
        self.input_text.bind("<Return>", self.send_message_event) # Bind Enter key

        # Send Button
        self.send_button = tk.Button(input_frame, text="Send", command=self.start_send_thread, font=("Helvetica", 14, "bold"), state=tk.DISABLED, padx=10)
        self.send_button.pack(side="right", padx=(10, 0))

        # Status Bar
        self.status_var = tk.StringVar()
        self.status_bar = tk.Label(root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W, font=("Helvetica", 11))
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # --- Threading & Queue ---
        self.result_queue = queue.Queue()
        self.load_model_thread()

    def add_message_to_history(self, speaker, message, tag):
        """Adds a message to the chat history with specified formatting."""
        self.chat_history.config(state='normal')
        self.chat_history.insert(tk.END, f"{speaker}: {message}\n", tag)
        self.chat_history.config(state='disabled')
        self.chat_history.see(tk.END) # Auto-scroll to the bottom

    def load_model_thread(self):
        self.status_var.set(f"Loading model: {MODEL_PATH}...")
        thread = threading.Thread(target=self.load_model_worker, daemon=True)
        thread.start()

    def load_model_worker(self):
        """Worker function to load the model in the background."""
        try:
            self.llm_model, self.llm_tokenizer = setup_llm()
            self.status_var.set("Model loaded successfully. Ready to chat!")
            self.send_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Model Loading Error", f"Failed to load the model: {e}")
            self.status_var.set("Error: Failed to load model.")

    def send_message_event(self, event):
        """Handles the Enter key press event."""
        self.start_send_thread()
        return "break" # Prevents the default Enter key behavior (adding a newline)

    def start_send_thread(self):
        """Starts the message sending process in a new thread."""
        user_input = self.input_text.get("1.0", tk.END).strip()
        if not user_input:
            return

        self.add_message_to_history("You", user_input, 'user')
        self.input_text.delete("1.0", tk.END)
        self.send_button.config(state=tk.DISABLED)
        self.status_var.set("Bot is thinking...")

        thread = threading.Thread(target=self.message_worker, args=(user_input,), daemon=True)
        thread.start()
        self.root.after(100, self.check_queue)

    def message_worker(self, user_input):
        """The actual LLM call that runs in the background."""
        try:
            start_time = time.perf_counter()
            response = call_llm(self.llm_model, self.llm_tokenizer, user_input)
            end_time = time.perf_counter()
            duration = end_time - start_time
            self.result_queue.put({"response": response, "duration": duration})
        except Exception as e:
            self.result_queue.put({"error": str(e)})

    def check_queue(self):
        """Periodically checks the queue for a result from the worker thread."""
        try:
            result = self.result_queue.get(block=False)
            if "error" in result:
                self.add_message_to_history("System Error", result['error'], 'bot')
            else:
                self.add_message_to_history("Bot", result['response'], 'bot')
                # Also add the timing information
                self.add_message_to_history("Info", f"(Responded in {result['duration']:.2f} seconds)", 'info')

            self.status_var.set("Ready.")
            self.send_button.config(state=tk.NORMAL)
        except queue.Empty:
            self.root.after(100, self.check_queue)

def on_closing():
    """Handles the window closing event."""
    if messagebox.askokcancel("Quit", "Do you want to exit the chatbot?"):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
