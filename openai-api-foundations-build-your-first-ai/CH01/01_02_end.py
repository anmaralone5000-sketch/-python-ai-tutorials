"""
OpenAI API Foundations: Build Your First AI Application
Chapter 1: Get Started with the Responses API
Lesson 01_02: Analyze Screenshots and Documents
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


# --- Analyze an image ---

with open("data/error.png", "rb") as f:
    image_base64 = base64.b64encode(f.read()).decode("utf-8")

response = client.responses.create(
    model="gpt-5.5",
    instructions=INSTRUCTIONS,
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "I'm getting this error. What does it mean and how do I fix it?"
                },
                {
                    "type": "input_image",
                    "image_url": f"data:image/png;base64,{image_base64}"
                }
            ]
        }
    ]
)

print("--- Image Analysis ---")
print(response.output_text)
print()


# --- Analyze a PDF document ---

with open("data/company_vpn_policy.pdf", "rb") as f:
    pdf_base64 = base64.b64encode(f.read()).decode("utf-8")

response = client.responses.create(
    model="gpt-5.5",
    instructions=INSTRUCTIONS,
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "According to this policy, can I use a personal device to connect to the company VPN?"
                },
                {
                    "type": "input_file",
                    "filename": "company_vpn_policy.pdf",
                    "file_data": f"data:application/pdf;base64,{pdf_base64}"
                }
            ]
        }
    ]
)

print("--- PDF Analysis ---")
print(response.output_text)