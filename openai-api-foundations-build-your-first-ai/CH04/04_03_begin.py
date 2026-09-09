"""
OpenAI API Foundations: Build Your First AI Application
Chapter 4: Make Your Knowledge Base Searchable
Lesson 04_03: Run the Complete Knowledge Search Tool

GOAL: Execute the full application end to end, tracing how each
API connects into a working tool that takes a question in any
format and returns a sourced, structured answer.
"""

import os
import json
import base64
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

os.makedirs("output", exist_ok=True)

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
            "description": "References used to answer the question"
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


# --- Reusable functions from previous lessons ---

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query, knowledge_base, top_k=3):
    query_response = client.embeddings.create(
        input=query,
        model="text-embedding-3-small"
    )
    query_embedding = query_response.data[0].embedding

    results = []
    for doc in knowledge_base:
        score = cosine_similarity(query_embedding, doc["embedding"])
        results.append({"text": doc["text"], "score": score})

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_k]


# --- Load the knowledge base ---

with open("data/knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)


# --- Build the answer function ---

# TODO 1: Write an answer_question function that:
#   - Calls search() to find relevant documents
#   - Joins the top results into a context string
#   - Calls client.responses.create() with instructions that
#     include the context and tell the model to answer ONLY
#     from the provided context
#   - Uses the SCHEMA for structured output
#   - Returns the parsed JSON result

def answer_question(question):
    pass  # Replace this


# --- Test with a text question ---

# TODO 2: Call answer_question with "How do I submit an expense report?"
#   Print the answer, confidence, and sources.

# Replace this block


# --- Test with a voice question ---

# TODO 3: Build the voice pipeline:
#   - Transcribe "data/employee_question.wav"
#   - Pass the transcription to answer_question()
#   - Convert the answer to speech, save to "output/answer.mp3"

# Replace this block


# --- Test with a visual diagram ---

# TODO 4: Generate a visual diagram:
#   - Call answer_question with "What are the steps to request a new laptop?"
#   - Use client.images.generate() to create a diagram from the answer
#   - Save to "output/steps_diagram.png"

# Replace this block