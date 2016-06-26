"""
	DataBase
	---------------------------------
	version: 0.0.1
	date: Jun 18, 2016
	author: daniloax

"""

from control.read_data_base import read_data_base
from control.read_text_file import read_text_file

class data_base:
	def __init__(self):
		self.read_data_base = read_data_base()
		self.read_text_file = read_text_file()
		
	def read_accounts(self, file_name, accounts):
		self.read_data_base.read_accounts(file_name, accounts)
		
	def create_account(self, file_name, account):
		return self.read_data_base.create_account(file_name, account)
	
