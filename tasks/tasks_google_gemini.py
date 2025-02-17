"""
Project: Coding Monkey Labs AI Universe
File: tasks_google_gemini.py
-------------------------
Description: [Add file description]

Created by: [Your Name]
Last Modified: [Date]

Dependencies:
    - [List major dependencies]

Usage:
    [Brief usage instructions]
"""

from crewai import Task
from tools import tools_google_gemini
from agents import agents_google_gemini

# Research task
research_task = Task(
  description=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
  ),
  expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
  tools=[tools_google_gemini.serper_tool],
  agent=agents_google_gemini.news_researcher_gemini,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tools_google_gemini.serper_tool],
  agent=agents_google_gemini.news_writer_gemini,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)