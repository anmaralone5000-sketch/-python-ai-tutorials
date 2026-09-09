"""
OpenAI API Foundations: Build Your First AI Application
Chapter 2: Extend the Responses API with Tools
Lesson 02_01: Search the Web and Get Structured Answers

GOAL: Attach the web search tool to the Responses API and define
a JSON schema that forces the model to return structured answers
with source citations and confidence scores.
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


# --- Add web search ---

# TODO 1: Use client.responses.create() with the web search tool.
#   - Set model to "gpt-5.5"
#   - Set instructions to INSTRUCTIONS
#   - Set tools to [{"type": "web_search"}]
#   - Set input to "Are there any known outages with Microsoft Teams right now?"
#   - Print response.output_text

response = None  # Replace this line


# --- Add structured output ---

# TODO 2: Make the same web search call, but add a text parameter
#   that defines a JSON schema for the response.
#   - Set text to:
#     {
#         "format": {
#             "type": "json_schema",
#             "name": "knowledge_response",
#             "strict": True,
#             "schema": {
#                 "type": "object",
#                 "properties": {
#                     "answer": {
#                         "type": "string",
#                         "description": "The answer to the employee's question"
#                     },
#                     "sources": {
#                         "type": "array",
#                         "items": {"type": "string"},
#                         "description": "URLs or references used"
#                     },
#                     "confidence": {
#                         "type": "string",
#                         "enum": ["high", "medium", "low"],
#                         "description": "How confident the model is"
#                     }
#                 },
#                 "required": ["answer", "sources", "confidence"],
#                 "additionalProperties": False
#             }
#         }
#     }
#   - Parse the response with json.loads(response.output_text)
#   - Print the answer, sources, and confidence fields separately

response = None  # Replace this line