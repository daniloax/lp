"""
	Account
	---------------------------------
	version: 0.0.1
	date: Jun 18, 2016
	author: daniloax

"""

from model.user import user

class account:
	
	def __init__(self, account_number, password, name):
		self.account_number = account_number
		self.password = password
		self.user = user(name)
		
	def get_account(self):
		return self.account
		
	def set_account(self, account_number):
		self.account_number = account_number
		
	def get_user(self):
		return self.user
		
	def set_user(self, user):
		self.user = user
		
	def get_password(self):
		return self.password
		
	def set_password(self, password):
		self.password = password
		
	def validate_password(self, password):
		if password == self.password:
			return True
		else:
			return False
