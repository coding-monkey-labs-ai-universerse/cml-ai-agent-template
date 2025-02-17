"""
Project: Coding Monkey Labs AI Universe
File: tools_google_gemini.py
-------------------------
Description: [Add file description]

Created by: [Your Name]
Last Modified: [Date]

Dependencies:
    - [List major dependencies]

Usage:
    [Brief usage instructions]
"""

## https://serper.dev/

from dotenv import load_dotenv
from crewai_tools import SerperDevTool
import os


# load_dotenv("./environments/.env.gemini")
load_dotenv()

# initialize the Environment vars 
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# Initialize the tool for internet searching capabilities
serper_tool = SerperDevTool()