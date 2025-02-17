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
from agents import agents_openai
from tasks import tasks_openai

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[agents_openai.blog_researcher_openai, agents_openai.blog_writer_openai],
  tasks=[tasks_openai.research_task, tasks_openai.write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'AI VS ML VS DL vs Data Science'})
print(result)