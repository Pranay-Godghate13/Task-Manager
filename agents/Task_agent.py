from crewai import Agent,LLM
from tools.Task_Manager_Tool import add_task_to_db
from tools.Task_Manager_Tool import list_task
from tools.Task_Manager_Tool import delete_task

llm=LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.0,

)

task_agent=Agent(
    role="Task agent",
    goal="To update tasks in database",
    backstory=("You are working as a Personal assistant who has 15+ years of managiing schedule of many CEO's"
               ),
    llm=llm,
    tools=[add_task_to_db,list_task,delete_task],
    verbose=True
)