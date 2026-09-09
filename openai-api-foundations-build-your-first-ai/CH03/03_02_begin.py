"""
OpenAI API Foundations: Build Your First AI Application
Chapter 3: Add Voice and Visuals
Lesson 03_02: Read Answers Aloud with the Audio API

GOAL: Convert the knowledge tool's answer into audio so employees
can listen on the go using the text-to-speech endpoint.
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

os.makedirs("output", exist_ok=True)


# --- Convert text to speech ---

answer = "You can use a personal device to connect to the company VPN, but you need to complete the BYOD enrollment form through the IT Self-Service Portal and enable full-disk encryption. Personal devices receive limited network access."

# TODO 1: Use client.audio.speech.with_streaming_response.create()
#   to convert the answer text to speech.
#   - Set model to "gpt-4o-mini-tts"
#   - Set voice to "coral"
#   - Set input to the answer variable
#   - Use response.stream_to_file("output/answer.mp3")
#   - Print a confirmation message

# Replace this block


# --- Full pipeline: voice in, voice out ---

# TODO 2: Build the complete voice pipeline.
#   Step 1: Transcribe the employee's voice question
#   - Open "data/employee_question.wav" in binary mode
#   - Use client.audio.transcriptions.create() with model="whisper-1"
#   - Print the transcription
#
#   Step 2: Get the answer from the knowledge assistant
#   - Use client.responses.create() with transcript.text as input
#   - Print the answer
#
#   Step 3: Convert the answer to speech
#   - Use client.audio.speech.with_streaming_response.create()
#   - Save to "output/full_pipeline_answer.mp3"
#   - Print a confirmation message

# Replace this block