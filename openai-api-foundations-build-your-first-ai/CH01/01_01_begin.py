"""
OpenAI API Foundations: Build Your First AI Application
Chapter 1: Get Started with the Responses API
Lesson 01_01: Generate Answers from a Prompt

GOAL: Send your first request to the Responses API, then add
instructions to shape the model as a knowledge assistant.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# --- Your first API call ---

# TODO 1: Use client.responses.create() to send a request.
#   - Set model to "gpt-5.5"
#   - Set input to "What is a VPN and why would a company require one?"
#   - Print response.output_text

response = None  # Replace this line


# --- Shape the model with instructions ---

# TODO 2: Make a second call to client.responses.create(), but this
#   time add an instructions parameter that tells the model:
#   - It is an internal knowledge assistant for a technology company
#   - It should answer questions about company tools, policies, and
#     technical topics
#   - It should keep answers concise: 2-3 sentences max
#   - If it doesn't know the answer, it should suggest who to contact
#
#   Set input to "How do I reset my password?"
#   Print response.output_text

response = None  # Replace this line