def agent_response(user_input):
    return f"You said: {user_input}"

user_message = input("Enter something: ")
print(agent_response(user_message))

def agent_response(user_input):
    if "hello" in user_input.lower():
        return "Hi there! I'm your AI Agent."
    elif "how are you" in user_input.lower():
        return "I'm just code, but I'm running perfectly!"
    else:
        return f"You said: {user_input}"

user_message = input("Enter something: ")
print(agent_response(user_message))

def agent_response(user_input):
    if "hello" in user_input.lower():
        return "Hi there! I'm your AI Agent."
    elif "how are you" in user_input.lower():
        return "I'm just code, but I'm running perfectly!"
    else:
        return f"You said: {user_input}"

print("🤖 AI Agent ready! Type 'exit' to stop.\n")

while True:
    user_message = input("You: ")
    if user_message.lower() == "exit":
        print("Agent: Goodbye! 👋")
        break
    print("Agent:", agent_response(user_message))
