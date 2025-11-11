import time

class CalculatorTool:
    def run(self, expression):
        try:
            return eval(expression)
        except Exception as e:
            return f"Error: {e}"

class TranslatorTool:
    def run(self, text):
        translations = {"hello": "hola", "bye": "adiós", "thanks": "gracias"}
        return translations.get(text.lower(), "Translation not found")

class ToolRegistry:
    def __init__(self):
        self.tools = {
            "calculator": CalculatorTool(),
            "translator": TranslatorTool()
        }

    def get_tool(self, name):
        return self.tools.get(name)

class AIAgent:
    def __init__(self):
        self.registry = ToolRegistry()
        print("🤖 Hello! I can now use a Tool Registry to access tools dynamically.")
        print(f"Available tools: {list(self.registry.tools.keys())}")

    def run(self):
        while True:
            query = input("\nAsk me something (or type 'exit' to quit): ").lower()
            if query == "exit":
                print("Goodbye! 👋")
                break

            if "add" in query or "subtract" in query or "multiply" in query or "divide" in query:
                tool = self.registry.get_tool("calculator")
                expr = query.replace("add", "+").replace("subtract", "-").replace("multiply", "*").replace("divide", "/")
                result = tool.run(expr)
                print(f"🧮 Result: {result}")

            elif "translate" in query:
                tool = self.registry.get_tool("translator")
                word = query.replace("translate", "").strip()
                result = tool.run(word)
                print(result)

            else:
                print("I’m not sure how to handle that yet. Try a math or translation query!")

if __name__ == "__main__":
    agent = AIAgent()
    agent.run()
