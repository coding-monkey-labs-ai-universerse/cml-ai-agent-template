"""
Project: Coding Monkey Labs AI Universe
File: crew.py
-------------------------
Description: [Add file description]

Created by: [Your Name]
Last Modified: [Date]

Dependencies:
    - [List major dependencies]

Usage:
    [Brief usage instructions]
"""

from crewai import Crew,Process
from agents import agents_google_gemini
from tasks import tasks_google_gemini

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[agents_google_gemini.news_researcher_gemini, agents_google_gemini.news_writer_gemini],
    tasks=[tasks_google_gemini.research_task, tasks_google_gemini.write_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'Latest AI Agents'})
print(result)