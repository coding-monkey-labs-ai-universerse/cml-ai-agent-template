"""
Project: Coding Monkey Labs AI Universe
File: agents_google_gemini.py
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
from tools import tools_google_gemini
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from litellm import LLM 

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME")

## call the gemini models
# llm=ChatGoogleGenerativeAI(model=GEMINI_MODEL_NAME,
#                            verbose=True,
#                            temperature=0.5,
#                            google_api_key=GOOGLE_API_KEY,
#                            provider="google")


# llm=ChatGoogleGenerativeAI(model="models/gemini-1.5-flash",
#                            verbose=True,
#                            temperature=0.5,
#                            google_api_key=GOOGLE_API_KEY,
#                            provider="google")

llm1 = LLM(model="models/gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)

news_researcher_gemini = Agent(
    role="Senior Researcher",
    goal='Unccover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."

    ),
    tools=[],
    llm=llm1,
    allow_delegation=True

)

news_writer_gemini = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tools_google_gemini.serper_tool],
  llm=llm1,
  allow_delegation=False
)

