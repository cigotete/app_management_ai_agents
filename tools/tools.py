from interpreter import interpreter
from langchain.tools import tool

interpreter.auto_run = True
interpreter.llm.model = "openai/gpt-3.5-turbo-0125" #gpt-4-1106-preview

class CLITool:
    @tool("Executor")
    def execute_cli_command(command: str):
        """Create and Execute code using Open Interpreter."""
        result = interpreter.chat(command)
        return result


