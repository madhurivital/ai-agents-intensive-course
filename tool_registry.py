# tool_registry.py
# Simulated MCP Tool Registry for Day 2

from agent_with_tools import calculator_tool, translator_tool

# Dictionary of available tools
TOOLS = {
    "calculator": calculator_tool,
    "translator": translator_tool
}

def get_tool(name):
    """
    Returns the tool function by name.
    """
    return TOOLS.get(name, None)

def list_tools():
    """
    Lists all available tools.
    """
    return list(TOOLS.keys())
