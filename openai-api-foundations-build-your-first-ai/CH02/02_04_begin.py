"""
OpenAI API Foundations: Build Your First AI Application
Chapter 2: Extend the Responses API with Tools
Lesson 02_04: Stream Responses to Your Users

GOAL: Use server-sent events to stream answers from the Responses
API so employees see results as they are generated.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

INSTRUCTIONS = """
    You are an internal knowledge assistant for a technology company.
    Answer employee questions about company tools, policies, and
    technical topics. Keep answers concise: 2-3 sentences max.
    If you don't know the answer, say so and suggest who to contact.
"""


# --- Stream a response ---

# TODO 1: Use client.responses.create() with stream=True.
#   - Set model to "gpt-5.5"
#   - Set instructions to INSTRUCTIONS
#   - Set input to "Explain the company's data backup policy in detail."
#   - Set stream to True
#   - Loop through the stream with: for event in stream:
#   - Check if event.type == "response.output_text.delta"
#   - If so, print event.delta with end="" and flush=True
#   - Print a newline after the loop

stream = None  # Replace this line


# --- Handle lifecycle events ---

# TODO 2: Make the same streaming call, but this time handle
#   three event types:
#   - "response.created" -> print "[Response started]"
#   - "response.output_text.delta" -> print event.delta
#     (with end="" and flush=True)
#   - "response.completed" -> print a newline, then
#     print "[Response complete]"

stream = None  # Replace this line