"""
OpenAI API Foundations: Build Your First AI Application
Chapter 2: Extend the Responses API with Tools
Lesson 02_02: Call Your Own Functions
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

tools = [
    {
        "type": "function",
        "name": "lookup_employee",
        "description": "Look up an employee's info by their employee ID. Returns name, department, role, and location.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "string",
                    "description": "The employee ID, e.g. E001"
                }
            },
            "required": ["employee_id"],
            "additionalProperties": False
        },
        "strict": True
    }
]


# --- Send the request ---

response = client.responses.create(
    model="gpt-5.5",
    instructions=INSTRUCTIONS,
    tools=tools,
    input="Can you look up the info for employee E001?"
)

print("--- Model requested a function call ---")


# --- Handle the function call ---

for item in response.output:
    if item.type == "function_call":
        print(f"Function: {item.name}")
        print(f"Arguments: {item.arguments}")
        print()

        args = json.loads(item.arguments)
        result = lookup_employee(args["employee_id"])

        print(f"Function result: {result}")
        print()


        # --- Send the function result back ---

        final_response = client.responses.create(
            model="gpt-5.5",
            instructions=INSTRUCTIONS,
            previous_response_id=response.id,
            input=[
                {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": result
                }
            ]
        )

        print("--- Final Answer ---")
        print(final_response.output_text)