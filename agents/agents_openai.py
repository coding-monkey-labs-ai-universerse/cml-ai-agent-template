"""
Project: Coding Monkey Labs AI Universe
File: agents_openai.py
-------------------------
Description: [Add file description]

Created by: [Your Name]
Last Modified: [Date]

Dependencies:
    - [List major dependencies]

Usage:
    [Brief usage instructions]
"""

from crewai import Agent
from tools import tools_openai
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]=os.getenv("OPENAI_MODEL_NAME")

print(os.getenv("OPENAI_API_KEY"))
print(os.getenv("OPENAI_MODEL_NAME"))


## Create a senior blog content researcher
blog_researcher_openai=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verboe=True,
    memory=True,
    backstory=(
       "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion" 
    ),
    tools=[tools_openai.yt_tool],
    allow_delegation=True
)

## creating a senior blog writer agent with YT tool

blog_writer_openai=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[tools_openai.yt_tool],
    allow_delegation=False


)


