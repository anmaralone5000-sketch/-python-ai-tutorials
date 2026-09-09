"""
OpenAI API Foundations: Build Your First AI Application
Chapter 3: Add Voice and Visuals
Lesson 03_03: Generate Visual Explainers with the Images API
"""

import os
import base64
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


# --- Generate a simple image ---

print("--- Simple Diagram ---")

result = client.images.generate(
    model="gpt-image-1",
    prompt="A simple step-by-step diagram showing how to connect to a company VPN: Step 1 Open GlobalProtect, Step 2 Enter credentials, Step 3 Approve MFA, Step 4 Connected. Clean, professional infographic style with numbered steps.",
    size="1024x1024",
    quality="medium"
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

with open("output/vpn_steps.png", "wb") as f:
    f.write(image_bytes)

print("Image saved to output/vpn_steps.png")
print()


# --- Generate a diagram from a knowledge assistant answer ---

print("--- Dynamic Diagram from Answer ---")

# Step 1: Get a process answer
response = client.responses.create(
    model="gpt-5.5",
    instructions=INSTRUCTIONS,
    input="What are the steps to request a new laptop?"
)

answer = response.output_text
print(f"Answer: {answer}")

# Step 2: Generate a visual diagram of the steps
image_prompt = f"Create a clean, professional step-by-step infographic diagram that visualizes this process: {answer}. Use numbered steps, simple icons, and a modern corporate style."

result = client.images.generate(
    model="gpt-image-1",
    prompt=image_prompt,
    size="1024x1536",
    quality="medium"
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

with open("output/laptop_request_steps.png", "wb") as f:
    f.write(image_bytes)

print("Diagram saved to output/laptop_request_steps.png")