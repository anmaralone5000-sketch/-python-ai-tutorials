"""
OpenAI API Foundations: Build Your First AI Application
Chapter 4: Make Your Knowledge Base Searchable
Lesson 04_02: Build Semantic Search
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


# --- Search function ---

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


# --- Test searches ---

queries = [
    "how do I get a new computer?",
    "what are the core working hours?",
    "I need to submit receipts for a business dinner",
]

for query in queries:
    print(f"\n{'='*50}")
    print(f"Query: {query}")
    print('='*50)

    results = search(query, knowledge_base)

    for i, result in enumerate(results):
        print(f"\n--- Result {i+1} (Score: {result['score']:.4f}) ---")
        print(result["text"])