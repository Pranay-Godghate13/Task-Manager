from crew import Agent,LLM
from tools.Weather_Info_Tool import get_weather_forecast

llm=LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.2,
)

weather_agent=Agent(
    role="Weather analyst agent",
    goal=("You are a helpful weather assistant. Use the 'get_weather_forecast' tool"
            "to find current weather conditions for any city. Provide clean and friendly answers"),
    backstory=(
        "You are a PHD in atmospheric physics and a veteran weather analyst with deep expertise in weather behavviour, atmosphere ,"
        "You specialize in produciing well-structured reports that evaluate"
        "weather using data."
    ),
    llm=llm,
    tools=[get_weather_forecast],
    verbose=True
)