import tkinter as tk
from nltk.chat.util import Chat, reflections
import random

BG_COLOR = "#f0f0f0"
TEXT_COLOR = "#333333"
BOT_COLOR = "#3399ff"
USER_COLOR = "#99cc99"

class ChatBotGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sophisticated ChatBot")
        self.master.geometry("400x500")
        self.master.configure(bg=BG_COLOR)

        self.chat_frame = tk.Frame(master, bg=BG_COLOR)
        self.chat_frame.pack(padx=10, pady=10)

        self.chat_display = tk.Text(self.chat_frame, height=15, width=40, fg=TEXT_COLOR, bg=BG_COLOR, wrap=tk.WORD)
        self.chat_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.chat_frame, command=self.chat_display.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_display.config(yscrollcommand=self.scrollbar.set)

        self.user_input = tk.Entry(master, width=40, fg=TEXT_COLOR, bg=BG_COLOR)
        self.user_input.pack(pady=10)

        self.user_input.bind("<Return>", lambda event: self.process_input())

        # Initialize the chatbot instance
        self.chatbot = Chat(self.get_chat_patterns(), reflections)

        self.init_chat()

    def init_chat(self):
        self.display_response("Hello! I'm your sophisticated ChatBot. How can I assist you today?")

    def process_input(self):
        user_input = self.user_input.get().lower()
        if user_input == 'bye':
            self.display_response("Goodbye! Have a great day.")
            self.master.destroy()
        else:
            response = self.chatbot_response(user_input)
            self.display_response(response)
            self.user_input.delete(0, tk.END)

    def display_response(self, response):
        self.chat_display.tag_configure("user", foreground=USER_COLOR)
        self.chat_display.insert(tk.END, "You: " + self.user_input.get() + "\n", "user")

        self.chat_display.tag_configure("bot", foreground=BOT_COLOR)
        self.chat_display.insert(tk.END, "ChatBot: " + response + "\n", "bot")

        self.chat_display.yview(tk.END)

    def get_chat_patterns(self):
        patterns = [
            ["hi|hello|hey", ["Hello!", "Hi there!", "How can I assist you today?"]],
            ["how are you|what's up", ["I'm doing well, thank you!", "I'm fine, thanks for asking."]],
            ["what's your name|give me your name", ["You can call me ChatBot.", "I'm your friendly ChatBot."]],
            ["bye|goodbye", ["Goodbye!", "Have a great day!", "See you later!"]],
            ["tell me a joke|joke", [self.joke_response()]],
            ["fun fact", [self.fun_fact_response()]],
        ]
        return patterns

    @staticmethod
    def joke_response():
        jokes = [
            "In Tunisia we don't say: why are you angry?. We say: why are you eating yourself?",
        ]
        return random.choice(jokes)

    @staticmethod
    def fun_fact_response():
        fun_facts = [
            "nheb norkod",
            "tawwa el 10 mtee ellil",
            "kaad nesmaa fl phonk",
        ]
        return random.choice(fun_facts)

    def chatbot_response(self, user_input):
        response = self.chatbot.respond(user_input)
        if isinstance(response, list):
            return random.choice(response)
        elif callable(response):
            return response()
        else:
            return response or ""

if __name__ == "__main__":
    root = tk.Tk()
    chatbot_gui = ChatBotGUI(root)
    root.mainloop()
