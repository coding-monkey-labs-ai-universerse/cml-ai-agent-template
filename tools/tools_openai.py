"""
Project: Coding Monkey Labs AI Universe
File: tools_openai.py
-------------------------
Description: [Add file description]

Created by: [Your Name]
Last Modified: [Date]

Dependencies:
    - [List major dependencies]

Usage:
    [Brief usage instructions]
"""

from crewai_tools import YoutubeChannelSearchTool
from dotenv import load_dotenv

load_dotenv() 

# Initialize the tool with a specific Youtube channel handle to target your search
yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@maheshk172')
