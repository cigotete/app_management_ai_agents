from langchain_openai import ChatOpenAI
from crewai import Agent
from tools import tools

CLITool = tools.CLITool
CLIInstallProject = tools.CLIInstallProject

llm = ChatOpenAI(model="gpt-3.5-turbo-0125") #gpt-4-1106-preview

agent_software_eng = Agent(
    role='Software Engineer',
    goal='Design software application',
    backstory='Expert in software architecture and software engineering.',
    verbose=True,
    llm=llm
)

agent_cli_manager = Agent(
    role='Software Devops',
    goal='Ability to perform CLI management operations, execute using Exector Tool, CLI clone and install project or CLI Install Project',
    backstory='Expert in command line executions or operations, executing commands, or also creating and executing code and command line operations.',
    tools=[
      CLITool.execute_cli_command,
      CLIInstallProject.install,
      CLIInstallProject.clone_and_install
      ],
    verbose=True,
    llm=llm 
)