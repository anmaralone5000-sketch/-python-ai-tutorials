"""
OpenAI API Foundations: Build Your First AI Application
Chapter 3: Add Voice and Visuals
Lesson 03_01: Transcribe Voice Questions with the Audio API

GOAL: Transcribe an employee's voice question into text using
the speech-to-text endpoint, then feed it into the knowledge
assistant for an answer.
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

# TODO 1: Open the audio file and transcribe it.
#   - Open audio file in binary mode ("rb")
#   - Use client.audio.transcriptions.create()
#     with model="whisper-1" and file=audio_file
#   - Print transcript.text

transcript = None  # Replace this block


# --- Feed the transcription into the knowledge assistant ---

# TODO 2: Use client.responses.create() to answer the
#   transcribed question.
#   - Set model to "gpt-5.5"
#   - Set instructions to INSTRUCTIONS
#   - Set input to transcript.text
#   - Print response.output_text

response = None  # Replace this line