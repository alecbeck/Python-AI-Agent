import os

def write_file(working_directory, file_path, content):
	working_directory_abs = os.path.abspath(working_directory)
	target_file_path = os.path.abspath(os.path.join(working_directory_abs,file_path))
	if target_file_path.startswith(working_directory_abs):
		with open(target_file_path, "w") as f:
			f.write(content)
		return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
	else:
		return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'