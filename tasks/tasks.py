import sys
from pathlib import Path
from crewai import Task
from tools import tools
from agents import agents

CLITool = tools.CLITool
CLIInstallProject = tools.CLIInstallProject
agent_cli_manager = agents.agent_cli_manager

task_cli_create_dir = Task(
    description='Create a directory called "workarea" in the root of this project',
    agent=agent_cli_manager,
    tools=[CLITool.execute_cli_command],
    expected_output='create a directory in the root of this project.'
)

task_clone_git_project = Task(
    description='Enter to the "workarea" directory located in the root of this project, and execute following command "git clone https://github.com/cigotete/react-template-app .".',
    agent=agent_cli_manager,
    tools=[CLIInstallProject.clone_and_install],
    expected_output='Cloned a bolderplate of a React project.'
)

task_install_project = Task(
    description='This task is associated with a tool that will install a react App.',
    agent=agent_cli_manager,
    tools=[CLIInstallProject.install],
    expected_output='A bolderplate of a React project was installed.',
)
