"""
OpenAI API Foundations: Build Your First AI Application
Chapter 4: Make Your Knowledge Base Searchable
Lesson 04_02: Build Semantic Search

GOAL: Implement cosine similarity search so employees can find
relevant documents by asking natural language questions instead
of guessing keywords.
"""

import os
import json
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


# --- Load the knowledge base ---

with open("data/knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)

print(f"Loaded {len(knowledge_base)} documents")


# --- Cosine similarity ---

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# --- Build the search function ---

# TODO 1: Write a search function that takes a query, embeds it,
#   and finds the most relevant documents.
#   - Use client.embeddings.create() to embed the query
#     with model="text-embedding-3-small"
#   - Loop through knowledge_base and calculate
#     cosine_similarity between the query embedding and
#     each document's embedding
#   - Store results as a list of dicts: {"text": ..., "score": ...}
#   - Sort by score (highest first)
#   - Return the top top_k results

def search(query, knowledge_base, top_k=3):
    pass  # Replace this


# --- Test the search ---

# TODO 2: Run three search queries and print the results:
#   - "how do I get a new computer?"
#   - "what are the core working hours?"
#   - "I need to submit receipts for a business dinner"
#   For each result, print the rank, score, and document text.

# Replace this block