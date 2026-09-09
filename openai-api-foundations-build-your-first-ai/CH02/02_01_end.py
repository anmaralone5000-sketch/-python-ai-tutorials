"""
OpenAI API Foundations: Build Your First AI Application
Chapter 2: Extend the Responses API with Tools
Lesson 02_01: Search the Web and Get Structured Answers
"""

import os
import json
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

SCHEMA = {
    "type": "object",
    "properties": {
        "answer": {
            "type": "string",
            "description": "The answer to the employee's question"
        },
        "sources": {
            "type": "array",
            "items": {"type": "string"},
            "description": "URLs or references used to answer the question"
        },
        "confidence": {
            "type": "string",
            "enum": ["high", "medium", "low"],
            "description": "How confident the model is in the answer"
        }
    },
    "required": ["answer", "sources", "confidence"],
    "additionalProperties": False
}


# --- Web search without structured output ---

response = client.responses.create(
    model="gpt-5.5",
    instructions=INSTRUCTIONS,
    tools=[{"type": "web_search"}],
    input="Are there any known outages with Microsoft Teams right now?"
)

print("--- Web Search (Plain Text) ---")
print(response.output_text)
print()


# --- Web search with structured output ---

response = client.responses.create(
    model="gpt-5.5",
    instructions=INSTRUCTIONS,
    tools=[{"type": "web_search"}],
    input="Are there any known outages with Microsoft Teams right now?",
    text={
        "format": {
            "type": "json_schema",
            "name": "knowledge_response",
            "strict": True,
            "schema": SCHEMA
        }
    }
)

result = json.loads(response.output_text)

print("--- Web Search (Structured Output) ---")
print(f"Answer:     {result['answer']}")
print(f"Sources:    {result['sources']}")
print(f"Confidence: {result['confidence']}")