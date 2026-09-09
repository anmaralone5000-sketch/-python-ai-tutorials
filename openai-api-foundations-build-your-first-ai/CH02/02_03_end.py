"""
OpenAI API Foundations: Build Your First AI Application
Chapter 2: Extend the Responses API with Tools
Lesson 02_03: Pull Documentation Through MCP
"""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

CONTEXT7_API_KEY = os.getenv("CONTEXT7_API_KEY")

INSTRUCTIONS = """
    You are an internal knowledge assistant for a technology company.
    Answer employee questions about company tools, policies, and
    technical topics. Keep answers concise: 2-3 sentences max.
    If you don't know the answer, say so and suggest who to contact.
"""

# --- Employee lookup from previous lesson ---

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

employee_tool = {
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

mcp_tool = {
    "type": "mcp",
    "server_label": "context7",
    "server_url": "https://mcp.context7.com/mcp",
    "require_approval": "never",
    "headers": {
        "Authorization": f"Bearer {CONTEXT7_API_KEY}"
    }
}


# --- MCP only ---

print("--- MCP Documentation Search ---")

response = client.responses.create(
    model="gpt-5",
    instructions=INSTRUCTIONS,
    tools=[mcp_tool],
    input="How do I set up authentication in Next.js?"
)

print(response.output_text)
print()


# --- MCP + Function Calling combined ---

print("--- Combined: Function + MCP ---")

response = client.responses.create(
    model="gpt-5",
    instructions=INSTRUCTIONS,
    tools=[employee_tool, mcp_tool],
    input="What team does employee E003 work on, and can you find the latest docs on Python FastAPI?"
)

# Collect all function call outputs, then send them back in one request.
function_outputs = []
for item in response.output:
    if item.type == "function_call":
        args = json.loads(item.arguments)
        result = lookup_employee(args["employee_id"])
        function_outputs.append({
            "type": "function_call_output",
            "call_id": item.call_id,
            "output": result
        })

if function_outputs:
    response = client.responses.create(
        model="gpt-5",
        instructions=INSTRUCTIONS,
        tools=[employee_tool, mcp_tool],
        previous_response_id=response.id,
        input=function_outputs
    )

print(response.output_text)