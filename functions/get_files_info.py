import os
from google.genai import types

def out_results(working_directory, directory):
	output = ""
	items = os.listdir(f"{working_directory}/{directory}")
	fullDir = f"{working_directory}/{directory}"
	for item in items:
		isDir = os.path.isdir(f"{fullDir}/{item}")
		size = os.path.getsize(f"{fullDir}/{item}")
		output += f"- {item}: file_size={size}, is_dir={isDir}\n"
	
	return output.rstrip()

def get_files_info(working_directory, directory=None):
	working_directory_abs = os.path.abspath(working_directory)
	if os.path.exists(working_directory_abs):
		target_dir_abs = os.path.abspath(os.path.join(working_directory_abs, directory))
		if target_dir_abs.startswith(working_directory_abs):
			if os.path.isdir(target_dir_abs):
				return out_results(working_directory, directory)
			else:
				return f'Error: "{directory}" is not a directory'
		else:
			return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
	else:
		return f'Error: "{working_directory}" does not exists'


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

#print(get_files_info("calculator", "."))
#print(get_files_info("calculator", "pkg"))
#print(get_files_info("calculator", "/bin"))
#print(get_files_info("calculator", "../"))