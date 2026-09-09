"""
OpenAI API Foundations: Build Your First AI Application
Chapter 2: Extend the Responses API with Tools
Lesson 02_04: Stream Responses to Your Users
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

print("--- Basic Streaming ---")

stream = client.responses.create(
    model="gpt-5.5",
    instructions=INSTRUCTIONS,
    input="Explain the company's data backup policy in detail.",
    stream=True
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)

print()
print()


# --- Handle lifecycle events ---

print("--- Streaming with Lifecycle Events ---")

stream = client.responses.create(
    model="gpt-5.5",
    instructions=INSTRUCTIONS,
    input="What tools does the engineering team use for CI/CD?",
    stream=True
)

for event in stream:
    if event.type == "response.created":
        print("[Response started]")
    elif event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()
        print("[Response complete]")