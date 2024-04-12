from interpreter import interpreter
from langchain.tools import tool

interpreter.auto_run = True
interpreter.llm.model = "openai/gpt-3.5-turbo-0125" #gpt-4-1106-preview
interpreter.llm.context_window = 16385
interpreter.llm.max_tokens = 4096
interpreter.llm.max_retries = 4

class CLITool:
    @tool("Executor")
    def execute_cli_command(command: str):
        """Create and Execute code using Open Interpreter."""
        result = interpreter.chat(command)
        return result


class CLIInstallProject():
    @tool("CLI clone and install project")
    def clone_and_install():
        """Create directory, enter to it, clone project and install it."""
        import subprocess
        processes = subprocess.run("mkdir workarea && cd workarea && git clone https://github.com/cigotete/react-template-app . && npm install", shell=True)
        return processes
    
    @tool("CLI Install Project")
    def install():
        """Create directory, enter to it, and install React project."""
        import subprocess
        processes = subprocess.run("mkdir workarea && cd workarea && npm create vite@latest . --yes -- --template react && npm install && echo 'finished'", shell=True)
        return processes


