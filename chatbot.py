import re

def get_response(message, memory):
    msg = message.lower().strip()

    if 'name is' in msg:
        name = msg.split('name is')[-1].strip().capitalize()
        memory['name'] = name
        return f"Nice to meet you, {name}!"

    if 'my hobby is' in msg:
        hobby = msg.split('my hobby is')[-1].strip().capitalize()
        memory['hobby'] = hobby
        return f"{hobby} sounds interesting!"

    if 'hello' in msg or 'hi' in msg:
        return f"Hello {memory.get('name', 'there')}!"

    if 'what is my hobby' in msg:
        return f"Your hobby is {memory.get('hobby', 'unknown')}."

    return "I don't understand that yet."
