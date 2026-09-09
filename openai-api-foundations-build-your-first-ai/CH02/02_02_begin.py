"""
OpenAI API Foundations: Build Your First AI Application
Chapter 2: Extend the Responses API with Tools
Lesson 02_02: Call Your Own Functions

GOAL: Define a custom function that looks up employee records,
handle the model's function call, execute your code, and return
results back into the response.
"""

import os
import json
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

# --- Mock employee database ---

EMPLOYEES = {
    "E001": {"name": "Maria Santos", "department": "Engineering",
             "role": "Senior Developer", "location": "Austin"},
    "E002": {"name": "James Chen", "department": "Marketing",
             "role": "Content Manager", "location": "New York"},
    "E003": {"name": "Priya Patel", "department": "IT Support",
             "role": "Help Desk Lead", "location": "Atlanta"},
}

def lookup_employee(employee_id):
    employee = EMPLOYEES.get(employee_id)
    if employee:
        return json.dumps(employee)
    return json.dumps({"error": f"No employee found with ID {employee_id}"})


# --- Define the function as a tool ---

# TODO 1: Create a tools list with one function tool.
#   - Set type to "function"
#   - Set name to "lookup_employee"
#   - Set description to "Look up an employee's info by their
#     employee ID. Returns name, department, role, and location."
#   - Set parameters to a JSON schema with one property:
#     employee_id (type: string, description: "The employee ID, e.g. E001")
#   - Set required to ["employee_id"]
#   - Set additionalProperties to False
#   - Set strict to True

tools = []  # Replace this line


# --- Send the request ---

# TODO 2: Use client.responses.create() with the tools list.
#   - Set model to "gpt-5.5"
#   - Set instructions to INSTRUCTIONS
#   - Set tools to your tools list
#   - Set input to "Can you look up the info for employee E001?"

response = None  # Replace this line


# --- Handle the function call ---

# TODO 3: Loop through response.output and find the function_call item.
#   - Parse the arguments with json.loads(item.arguments)
#   - Call lookup_employee() with the employee_id from the arguments
#   - Store the result and the call_id

# Replace this block
call_id = None
result = None


# --- Send the function result back ---

# TODO 4: Use client.responses.create() to send the result back.
#   - Set model to "gpt-5.5"
#   - Set instructions to INSTRUCTIONS
#   - Set previous_response_id to response.id
#   - Set input to a list with one item:
#     {
#         "type": "function_call_output",
#         "call_id": call_id,
#         "output": result
#     }
#   - Print final_response.output_text

final_response = None  # Replace this line