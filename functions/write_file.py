import os
from google.genai import types

def write_file(working_directory, file_path, content):
	working_directory_abs = os.path.abspath(working_directory)
	target_file_path = os.path.abspath(os.path.join(working_directory_abs,file_path))
	if target_file_path.startswith(working_directory_abs):
		with open(target_file_path, "w") as f:
			f.write(content)
		return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
	else:
		return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content to file give, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file name of the file to write to. This will cretae a file if it doesn't exist already, or overwite the current file.",
            ),
			"content": types.Schema(
				type=types.Type.STRING,
				description="The content that will be writtent to the file."
			)
        },
    ),
)