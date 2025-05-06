from chatbot import get_response
from memory import load_memory, save_memory

print("Bot: Hello! Type 'exit' to end the conversation.")

memory = load_memory()

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Bot: Goodbye!")
        break

    response = get_response(user_input, memory)
    print(f"Bot: {response}")
    save_memory(memory)
