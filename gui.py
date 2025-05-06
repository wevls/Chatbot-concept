import tkinter as tk
from chatbot import get_response
from memory import load_memory, save_memory

memory = load_memory()

def on_send():
    user_input = entry.get()
    chat.insert(tk.END, f"You: {user_input}\n")
    response = get_response(user_input, memory)
    chat.insert(tk.END, f"Bot: {response}\n")
    entry.delete(0, tk.END)
    save_memory(memory)

root = tk.Tk()
root.title("Chatbot")

chat = tk.Text(root, height=20, width=50)
chat.pack()

entry = tk.Entry(root, width=50)
entry.pack()

send_button = tk.Button(root, text="Send", command=on_send)
send_button.pack()

root.mainloop()
