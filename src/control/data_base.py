"""
	DataBase
	---------------------------------
	version: 0.0.1
	date: Jun 18, 2016
	author: daniloax

"""
from control.read_text_file import read_text_file

class data_base:
	def __init__(self):
		self.read_text_file = read_text_file()
		
	def read_accounts(self, file_name, accounts):
		self.read_text_file.read_accounts(file_name, accounts)
