"""
OpenAI API Foundations: Build Your First AI Application
Chapter 1: Get Started with the Responses API
Lesson 01_02: Analyze Screenshots and Documents

GOAL: Pass images and PDF files to the Responses API so the
knowledge assistant can interpret screenshots and company documents.
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

# TODO 1: Read and base64 encode the error screenshot.
#   - Open "data/error.png" in binary mode ("rb")
#   - Encode it: base64.b64encode(f.read()).decode("utf-8")

image_base64 = None  # Replace this line

# TODO 2: Use client.responses.create() to send the image to the model.
#   - Set model to "gpt-5.5"
#   - Set instructions to INSTRUCTIONS
#   - Set input to a list with one message (role: "user")
#   - The message content should have two items:
#       1. An input_text asking "I'm getting this error. What does
#          it mean and how do I fix it?"
#       2. An input_image with image_url set to
#          f"data:image/png;base64,{image_base64}"
#   - Print response.output_text

response = None  # Replace this line


# --- Analyze a PDF document ---

# TODO 3: Read and base64 encode the company VPN policy PDF.
#   - Open "data/company_vpn_policy.pdf" in binary mode ("rb")
#   - Encode it: base64.b64encode(f.read()).decode("utf-8")

pdf_base64 = None  # Replace this line

# TODO 4: Use client.responses.create() to send the PDF to the model.
#   - Set model to "gpt-5.5"
#   - Set instructions to INSTRUCTIONS
#   - Set input to a list with one message (role: "user")
#   - The message content should have two items:
#       1. An input_text asking "According to this policy, can I use
#          a personal device to connect to the company VPN?"
#       2. An input_file with:
#          - filename: "company_vpn_policy.pdf"
#          - file_data: f"data:application/pdf;base64,{pdf_base64}"
#   - Print response.output_text

response = None  # Replace this line