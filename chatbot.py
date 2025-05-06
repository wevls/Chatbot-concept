import json
import re

#load the memory from the json file :)
try:
    with open('memory.json') as f:
        memory = json.load(f)
except FileNotFoundError:
    memory = {}

def save_memory():
    with open('memory.json', 'w') as f:
        json.dump(memory, f)

def respond(message):
    message = message.lower()

    if 'name is' in message:
        name = message.split('name is')[-1].strip().capitalize()
        memory['name'] = name
        save_memory()
        return f"Nice to meet you, {name}!"

    if 'my hobby is' in message:
        hobby = message.split('my hobby is')[-1].strip().capitalize()
        memory['hobby'] = hobby
        save_memory()
        return f"Cool! {hobby} sounds fun."

    if 'hello' in message:
        return f"Hello {memory.get('name', 'friend')}!"

    return "I don't understand that yet, but I'm learning!"

while True:
    msg = input("You: ")
    if msg.lower() in ['bye', 'exit']:
        print("Bot: Goodbye!")
        break
    print("Bot:", respond(msg))
