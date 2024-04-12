from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from tasks import tasks
task_cli_create_dir = tasks.task_cli_create_dir
task_clone_install_project = tasks.task_clone_install_project
task_install_project = tasks.task_install_project

from agents import agents
agent_cli_manager = agents.agent_cli_manager

llm = ChatOpenAI(model="gpt-3.5-turbo-0125") #gpt-4-1106-preview

cli_crew = Crew(
    agents=[
      agent_cli_manager
      ],
    tasks=[
      #task_cli_create_dir,
      task_install_project
      ],
    process=Process.sequential,
    manager_llm=llm
)

result = cli_crew.kickoff()
print(result)