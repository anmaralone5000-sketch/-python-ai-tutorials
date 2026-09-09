"""
OpenAI API Foundations: Build Your First AI Application
Chapter 3: Add Voice and Visuals
Lesson 03_03: Generate Visual Explainers with the Images API

GOAL: Create step-by-step visual diagrams when the answer
involves a process or workflow using the Images API.
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

# TODO 1: Use client.images.generate() to create a diagram.
#   - Set model to "gpt-image-1"
#   - Set prompt to a description of a step-by-step VPN connection
#     diagram (e.g. "A simple step-by-step diagram showing how to
#     connect to a company VPN: Step 1 Open GlobalProtect, Step 2
#     Enter credentials, Step 3 Approve MFA, Step 4 Connected.
#     Clean, professional infographic style with numbered steps.")
#   - Set size to "1024x1024"
#   - Set quality to "medium"
#   - Decode the image: base64.b64decode(result.data[0].b64_json)
#   - Save to "output/vpn_steps.png"

result = None  # Replace this block


# --- Generate a diagram from a knowledge assistant answer ---

# TODO 2: Build the two-step pipeline.
#   Step 1: Ask the knowledge assistant a process question
#   - Use client.responses.create() with input
#     "What are the steps to request a new laptop?"
#   - Print the answer
#
#   Step 2: Generate a visual diagram from the answer
#   - Build an image prompt that includes the answer text and
#     asks for a clean infographic style
#   - Use client.images.generate() with model="gpt-image-1",
#     size="1024x1536", quality="medium"
#   - Decode and save to "output/laptop_request_steps.png"

# Replace this block