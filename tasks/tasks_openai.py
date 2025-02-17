"""
Project: Coding Monkey Labs AI Universe
File: tasks_openai.py
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
from tools import tools_openai
from agents import agents_openai



## Research Task
research_task = Task(
  description=(
    "Identify the video {topic}."
    "Get detailed information about the video from the channel video."
  ),
  expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.',
  tools=[tools_openai.yt_tool],
  agent=agents_openai.blog_researcher_openai,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "get the info from the youtube channel on the topic {topic}."
  ),
  expected_output='Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog',
  tools=[tools_openai.yt_tool],
  agent=agents_openai.blog_writer_openai,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)