"""
OpenAI API Foundations: Build Your First AI Application
Chapter 3: Add Voice and Visuals
Lesson 03_01: Transcribe Voice Questions with the Audio API
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


# --- Transcribe an audio file ---
with open("data/employee_question.m4a", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )

print("--- Transcription ---")
print(transcript.text)
print()


# --- Feed the transcription into the knowledge assistant ---

response = client.responses.create(
    model="gpt-5.5",
    instructions=INSTRUCTIONS,
    input=transcript.text
)

print("--- Knowledge Assistant Answer ---")
print(response.output_text)