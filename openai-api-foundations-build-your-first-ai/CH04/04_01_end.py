"""
OpenAI API Foundations: Build Your First AI Application
Chapter 4: Make Your Knowledge Base Searchable
Lesson 04_01: Turn Documents into Embeddings
"""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

os.makedirs("data", exist_ok=True)


# --- Create a single embedding ---

print("--- Single Embedding ---")

response = client.embeddings.create(
    input="How do I reset my company email password?",
    model="text-embedding-3-small"
)

embedding = response.data[0].embedding
print(f"Dimensions: {len(embedding)}")
print(f"First 5 values: {embedding[:5]}")
print()


# --- Embed a knowledge base ---

print("--- Knowledge Base ---")

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

response = client.embeddings.create(
    input=documents,
    model="text-embedding-3-small"
)

knowledge_base = []
for i, doc in enumerate(documents):
    knowledge_base.append({
        "text": doc,
        "embedding": response.data[i].embedding
    })

print(f"Embedded {len(knowledge_base)} documents")

with open("data/knowledge_base.json", "w") as f:
    json.dump(knowledge_base, f)

print("Knowledge base saved to data/knowledge_base.json")