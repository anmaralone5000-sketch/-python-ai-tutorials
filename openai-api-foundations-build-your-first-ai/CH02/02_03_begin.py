"""
OpenAI API Foundations: Build Your First AI Application
Chapter 2: Extend the Responses API with Tools
Lesson 02_03: Pull Documentation Through MCP

GOAL: Connect to the Context7 MCP server from a Responses API
call so the knowledge tool can search third-party technical
documentation without writing custom integration code.
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


# --- Connect to an MCP server ---

# TODO 1: Use client.responses.create() with an MCP tool.
#   - Set model to "gpt-5"
#   - Set instructions to INSTRUCTIONS
#   - Set tools to a list with one MCP tool:
#     {
#         "type": "mcp",
#         "server_label": "context7",
#         "server_url": "https://mcp.context7.com/mcp",
#         "require_approval": "never",
#         "headers": {
#             "Authorization": f"Bearer {CONTEXT7_API_KEY}"
#         }
#     }
#   - Set input to "How do I set up authentication in Next.js?"
#   - Print response.output_text

response = None  # Replace this line


# --- Combine MCP with function calling ---

# Employee lookup function from the previous lesson
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

# TODO 2: Use client.responses.create() with BOTH the employee
#   function tool AND the Context7 MCP tool in the same tools list.
#   - Set input to "What team does employee E003 work on, and can
#     you find the latest docs on Python FastAPI?"
#   - The model may return multiple function calls. Collect all
#     outputs into a list:
#     function_outputs = []
#     for item in response.output:
#         if item.type == "function_call":
#             args = json.loads(item.arguments)
#             result = lookup_employee(args["employee_id"])
#             function_outputs.append({
#                 "type": "function_call_output",
#                 "call_id": item.call_id,
#                 "output": result
#             })
#   - If function_outputs is not empty, send them all back in one
#     call using previous_response_id and input=function_outputs
#   - Print the final response.output_text

response = None  # Replace this line