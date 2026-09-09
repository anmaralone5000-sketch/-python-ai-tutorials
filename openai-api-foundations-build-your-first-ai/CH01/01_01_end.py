"""
OpenAI API Foundations: Build Your First AI Application
Chapter 1: Get Started with the Responses API
Lesson 01_01: Generate Answers from a Prompt
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()  # Reads OPENAI_API_KEY from environment

# --- Your first API call ---

response = client.responses.create(
    model="gpt-5.5",
    input="What is a VPN and why would a company require one?"
)

print(response.output_text)


# --- Shape the model with instructions ---

response = client.responses.create(
    model="gpt-5.5",
    instructions="""
        You are an internal knowledge assistant for a technology company.
        Answer employee questions about company tools, policies, and
        technical topics. Keep answers concise: 2-3 sentences max.
        If you don't know the answer, say so and suggest who to contact.
    """,
    input="How do I reset my password?"
)

print(response.output_text)