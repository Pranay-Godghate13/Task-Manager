from crewai import Task
from agents.Task_agent import task_agent

assistant_analysis=Task(
    description=("You have to add tasks in my db after taking inputs about weather conditions."
                 "If weather is not suitable dont add any activity for that time slot."
                 "No two activities should be added for same time slot."
                 "Add activity in Database if all conditions are followed."),
    expected_output=(
                    "Aa clear, bullet-pointed summary of:\n"
                    "- Task added\n"
                    "- Weather condition\n"
                    "- Any immediate trends or observations."
                    ),
    inputs={
        "task": "Task description",
        "date": "Task date (DD-MM-YYYY)",
        "time": "Task time (HH:MM)",
        "status": "Task status (Scheduled/Pending/Completed)"
    },

    agent=task_agent
)