import os
from google.genai import types

def get_file_content(working_directory, file_path):
	working_directory_abs = os.path.abspath(working_directory)
	target_file_path = os.path.abspath(os.path.join(working_directory_abs,file_path))
	#print(working_directory_abs)
	#print(target_file_path)
	if target_file_path.startswith(working_directory_abs):
		if os.path.isfile(target_file_path):
			file_content_string = ""
			with open(target_file_path, "r") as f:
				file_content_string = f.read(10000)
			
			#print(len(file_content_string))
			if len(file_content_string) == 10000:
				return f'{file_content_string} File "{target_file_path}" truncated at 10000 characters' 
			else:
				return file_content_string
		else:
			return f'Error: File not found or is not a regular file: "{file_path}"'
	else:
		return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'



schema_get_files_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Shows the first 10000 characters in a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to file, relative to the working directory.",
            ),
        },
    ),
)