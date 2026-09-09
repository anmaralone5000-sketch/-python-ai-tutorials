"""
OpenAI API Foundations: Build Your First AI Application
Chapter 4: Make Your Knowledge Base Searchable
Lesson 04_01: Turn Documents into Embeddings

GOAL: Convert company documents into vector representations and
store them for retrieval using the Embeddings API.
"""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

os.makedirs("data", exist_ok=True)


# --- Create a single embedding ---

# TODO 1: Use client.embeddings.create() to embed a single sentence.
#   - Set input to "How do I reset my company email password?"
#   - Set model to "text-embedding-3-small"
#   - Get the embedding from response.data[0].embedding
#   - Print the number of dimensions: len(embedding)
#   - Print the first 5 values: embedding[:5]

response = None  # Replace this block


# --- Embed a knowledge base ---

documents = [
    "To reset your email password, go to the IT Self-Service Portal at itportal.globex.internal and click 'Reset Password'. You will need to verify your identity with MFA.",
    "New laptop requests must be submitted through the IT Self-Service Portal. Your manager must approve the request. Standard processing time is 5-7 business days.",
    "The company VPN uses GlobalProtect. Download it from the IT Self-Service Portal. Personal devices must complete BYOD enrollment before connecting.",
    "Globex offers three health insurance plans: Basic, Standard, and Premium. Open enrollment runs from November 1-15 each year. Contact HR at hr@globex.com for details.",
    "Engineering teams use GitHub for source control, Jenkins for CI/CD, and Jira for project tracking. Access is provisioned through your manager.",
    "Remote work is available for most roles. Employees must maintain core hours of 10am-3pm in their local time zone. All remote workers need a stable internet connection and a dedicated workspace.",
    "Expense reports must be submitted within 30 days of the expense. Use the Concur app to photograph receipts and submit claims. Approvals typically take 3-5 business days.",
    "The company holiday schedule includes 10 paid holidays per year. Additional PTO is accrued at a rate of 1.5 days per month for full-time employees.",
]

# TODO 2: Embed all documents in a single API call.
#   - Use client.embeddings.create() with input=documents
#     and model="text-embedding-3-small"
#   - Build a knowledge_base list where each item is a dict with:
#     {"text": doc, "embedding": response.data[i].embedding}
#   - Print the number of documents embedded
#   - Save the knowledge_base to "data/knowledge_base.json"
#     using json.dump()

knowledge_base = []  # Replace this block