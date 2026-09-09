"""
OpenAI API Foundations: Build Your First AI Application
Chapter 3: Add Voice and Visuals
Lesson 03_02: Read Answers Aloud with the Audio API
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

print("--- Text to Speech ---")

answer = "You can use a personal device to connect to the company VPN, but you need to complete the BYOD enrollment form through the IT Self-Service Portal and enable full-disk encryption. Personal devices receive limited network access."

with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="coral",
    input=answer
) as response:
    response.stream_to_file("output/answer.mp3")

print("Audio saved to output/answer.mp3")
print()


# --- Full pipeline: voice in, voice out ---

print("--- Full Voice Pipeline ---")

# Step 1: Transcribe the voice question
with open("data/employee_question.m4a", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )

print(f"Employee asked: {transcript.text}")

# Step 2: Get the answer from the knowledge assistant
response = client.responses.create(
    model="gpt-5.5",
    instructions=INSTRUCTIONS,
    input=transcript.text
)

print(f"Answer: {response.output_text}")

# Step 3: Convert the answer to speech
with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="coral",
    input=response.output_text
) as speech_response:
    speech_response.stream_to_file("output/full_pipeline_answer.mp3")

print("Audio answer saved to output/full_pipeline_answer.mp3")