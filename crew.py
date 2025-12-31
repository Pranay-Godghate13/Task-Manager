from crewai import Crew

from tasks.Assistant_Task import assistant_analysis
from tasks.Weather_Task import get_weather_analysis
from agents.Task_agent import task_agent
from agents.Weather_Agent import weather_agent

task_crew=Crew(
    agents=[weather_agent,task_agent],
    tasks=[get_weather_analysis,assistant_analysis],
    verbose=True
)