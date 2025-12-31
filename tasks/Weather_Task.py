from crew import Task
from agents.Weather_Agent import weather_agent

get_weather_analysis=Task(
    description=("You check the weather of a city, analyse it with your expertise and tell the user whether the activity is suitable"
                 "for the weather condition."),
    expected_output=(
        "Aa clear, bullet-pointed summary of:\n"
        "- Weather condition.\n"
        "- Temperature\n"
        "- Any immediate ttrends or observations."
    ),
    agent=[weather_agent]
)