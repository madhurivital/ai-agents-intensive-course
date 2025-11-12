# agent_with_memory.py

import json
import os

# File to store memory
MEMORY_FILE = "memory.json"

# Load memory if exists, else create new structure
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        try:
            memory_data = json.load(f)
        except json.JSONDecodeError:
            memory_data = {"conversations": []}
else:
    memory_data = {"conversations": []}

print("🤖 Hello! I now have session memory and can summarize past chats.")

def summarize(conversations):
    """Simple summary of last few messages"""
    if not conversations:
        return "We haven’t talked yet."
    topics = [c.get("user", "") for c in conversations[-5:]]
    return f"Recently, we talked about: {', '.join(topics)}"

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    memory_data["conversations"].append({"user": user_input})

    if "remember" in user_input.lower():
        reply = summarize(memory_data["conversations"])
    else:
        reply = "Got it! I'll keep that in mind."

    memory_data["conversations"].append({"agent": reply})
    print("Agent:", reply)

    # Save memory after every response
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory_data, f, indent=4)
