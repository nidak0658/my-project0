import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

class QuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Quote Generator")

        self.quotes = [
            "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
            "The way to get started is to quit talking and begin doing. - Walt Disney",
            "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
            "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
            "If you look at what you have in life, you'll always have more. - Oprah Winfrey",
            "Life is what happens when you're busy making other plans. - John Lennon"
        ]

        self.quote_label = tk.Label(root, text="", wraplength=300, justify="center")
        self.quote_label.pack(pady=20)

        self.new_quote_button = tk.Button(root, text="New Quote", command=self.display_new_quote)
        self.new_quote_button.pack(pady=10)

        self.share_button = tk.Button(root, text="Share Quote", command=self.share_quote)
        self.share_button.pack(pady=10)

    def display_new_quote(self):
        quote = random.choice(self.quotes)
        self.quote_label.config(text=quote)
        self.current_quote = quote

    def share_quote(self):
        if hasattr(self, 'current_quote'):
            pyperclip.copy(self.current_quote)
            messagebox.showinfo("Quote Copied", "The quote has been copied to your clipboard!")
        else:
            messagebox.showwarning("No Quote", "Please generate a quote first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteApp(root)
    root.mainloop()
