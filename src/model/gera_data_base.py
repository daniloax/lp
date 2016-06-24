"""
	GeraDataBase
	---------------------------------
	version: 0.0.1
	date: Jun 21, 2016
	author: daniloax
	
"""

from control.data_base import data_base

class gera_data_base:
	
	def __init__(self):
		self.data_base = data_base()
		self.accounts = []
		
	def get_user(self, account):
		return self.get_account(account).get_name()
	
	def get_account(self, account):
		for current_account in self.accounts:
			if current_account == account:
				return current_account
		return None
		
	def get_accounts(self):
		return self.accounts
		
	def authenticate_user(self, account, password):
		user_account = self.get_account(account)
		if user_account != None:
			return user_account.validate_password(password)
		else:
			return False
		
	def read_accounts(self):
		self.data_base.read_accounts("account.txt", self.accounts)
		
		
