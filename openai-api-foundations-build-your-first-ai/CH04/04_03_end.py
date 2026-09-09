"""
OpenAI API Foundations: Build Your First AI Application
Chapter 4: Make Your Knowledge Base Searchable
Lesson 04_03: Run the Complete Knowledge Search Tool
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

print(f"Loaded {len(knowledge_base)} documents")
print()


# --- Answer function ---

def answer_question(question):
    results = search(question, knowledge_base)
    context = "\n\n".join([r["text"] for r in results])

    response = client.responses.create(
        model="gpt-5.5",
        instructions=f"""
            You are an internal knowledge assistant for a technology company.
            Answer the employee's question using ONLY the context provided below.
            If the context doesn't contain the answer, say so.
            Keep answers concise: 2-3 sentences max.

            Context:
            {context}
        """,
        input=question,
        text={
            "format": {
                "type": "json_schema",
                "name": "knowledge_response",
                "strict": True,
                "schema": SCHEMA
            }
        }
    )

    return json.loads(response.output_text)


# === TEXT QUESTION ===

print("=" * 50)
print("TEXT QUESTION")
print("=" * 50)

result = answer_question("How do I submit an expense report?")
print(f"Answer:     {result['answer']}")
print(f"Confidence: {result['confidence']}")
print(f"Sources:    {result['sources']}")
print()


# === VOICE QUESTION ===

print("=" * 50)
print("VOICE QUESTION")
print("=" * 50)

with open("data/employee_question.m4a", "rb") as f:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=f
    )

print(f"Transcription: {transcript.text}")

result = answer_question(transcript.text)
print(f"Answer:        {result['answer']}")
print(f"Confidence:    {result['confidence']}")

with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="coral",
    input=result["answer"]
) as speech:
    speech.stream_to_file("output/answer.mp3")

print("Audio saved to output/answer.mp3")
print()


# === VISUAL DIAGRAM ===

print("=" * 50)
print("VISUAL DIAGRAM")
print("=" * 50)

result = answer_question("What are the steps to request a new laptop?")
print(f"Answer: {result['answer']}")

img_result = client.images.generate(
    model="gpt-image-1",
    prompt=f"Create a clean step-by-step infographic: {result['answer']}. Numbered steps, simple icons, modern corporate style.",
    size="1024x1536",
    quality="medium"
)

image_bytes = base64.b64decode(img_result.data[0].b64_json)
with open("output/steps_diagram.png", "wb") as f:
    f.write(image_bytes)

print("Diagram saved to output/steps_diagram.png")
print()
print("=" * 50)
print("COMPLETE: All four APIs working together.")
print("=" * 50)