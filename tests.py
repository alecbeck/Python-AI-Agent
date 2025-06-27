import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
"""
class TestGet_Files_Info(unittest.TestCase):
	def test_calculator(self):
		self.assertEqual(get_files_info("calculator", "."), "- pkg: file_size=4096, is_dir=True\n- tests.py: file_size=1330, is_dir=False\n- main.py: file_size=564, is_dir=False")

	def test_calculator_pkg(self):
		self.assertEqual(get_files_info("calculator", "pkg"), "- __pycache__: file_size=4096, is_dir=True\n- render.py: file_size=753, is_dir=False\n- calculator.py: file_size=1720, is_dir=False")

	def test_calculator_bin(self):
		self.assertEqual(get_files_info("calculator", "/bin"),'Error: Cannot list "/bin" as it is outside the permitted working directory')

	def test_calculator_none_outside(self):
		self.assertEqual(get_files_info("calculator", "../"), 'Error: Cannot list "../" as it is outside the permitted working directory')

if __name__ == "__main__":
    unittest.main()
"""




#print(get_files_info("calculator", "."))
#print(get_files_info("calculator", "pkg"))
#print(get_files_info("calculator", "/bin"))
#print(get_files_info("calculator", "../"))

#print(get_file_content("calculator", "lorem.txt"))
#print(get_file_content("calculator", "main.py"))
#print(get_file_content("calculator", "pkg/calculator.py"))
#print(get_file_content("calculator", "/bin/cat"))

print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))