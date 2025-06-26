import os
import sys
import getopt
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

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


messages = [types.Content(role="user", parts=[types.Part(text=sys.argv[1])])]
client = genai.Client(api_key=api_key)

responce = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

print(responce.text)

if is_verbose:
	print("\n")
	print(f"User prompt: {sys.argv[1]}")
	print(f"Prompt tokens: {responce.usage_metadata.prompt_token_count}")
	print(f"Response tokens: {responce.usage_metadata.candidates_token_count }")
