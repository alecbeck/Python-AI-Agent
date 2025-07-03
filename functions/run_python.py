import os
import subprocess

def run_python_file(working_directory, file_path):
	working_directory_abs = os.path.abspath(working_directory)
	target_file_path = os.path.abspath(os.path.join(working_directory_abs,file_path))
	output = ""
	try:
		if target_file_path.startswith(working_directory_abs):
			if os.path.exists(target_file_path):
				if target_file_path.endswith(".py"):
					result = subprocess.run(["python", target_file_path], text=True, timeout=30, cwd=working_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
					output = f'STDOUT:{result.stdout}\nSTDERR:{result.stderr}'
					#print(output)
					if result.returncode != 0:
						output += f'\nProcess exited with code {result.returncode}'					
					if result.stdout == "" and result.stderr == "":
						return f'No output produced.'
					else:
						return output
				else:
					return f'Error: "{file_path}" is not a Python file.'
			else:
				return f'Error: File "{file_path}" not found.'
		else:
			return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
	except Exception as e:
		return f'Error: executing Python file: {e}'
