import os
import sys
import getopt
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.run_python import schema_run_python_file
from functions.get_file_content import schema_get_files_content
from functions.write_file import schema_write_file

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

if len(sys.argv) < 2:
	print("Please enter a argument and try again")
	exit(1)
if len(sys.argv[1:]) > 1:
	argumentList = sys.argv[2:]
else:
	argumentList = list()


options = "v"
long_options = ["verbose"]
is_verbose = False

arguments, values = getopt.getopt(argumentList, options, long_options)

for argument, value in arguments:
	print(argument)
	if argument in ("-v", "--verbose"):
		is_verbose = True

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
		schema_run_python_file,
		schema_get_files_content,
		schema_write_file,
    ]
)

config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
)


messages = [types.Content(role="user", parts=[types.Part(text=sys.argv[1])])]
client = genai.Client(api_key=api_key)

#print(config)

response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages, config=config)

if response.function_calls:
	for function_call in response.function_calls:
		print(f"Calling function: {function_call.name}({function_call.args})")
		#print(function_call.args)
else:
	print(response.text)

if is_verbose:
	print("\n")
	print(f"User prompt: {sys.argv[1]}")
	print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
	print(f"Response tokens: {response.usage_metadata.candidates_token_count }")
