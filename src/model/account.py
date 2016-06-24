"""
	Account
	---------------------------------
	version: 0.0.1
	date: Jun 18, 2016
	author: daniloax

"""

from model.user import user

class account:
	
	def __init__(self, identifier, password, user):
		self.identifier = identifier
		self.password = password
		self.user = user
		
	def get_identifier(self):
		return self.identifier
		
	def set_identifier(self, identifier):
		self.identifier = identifier
		
	def get_password(self):
		return self.password
		
	def set_password(self, password):
		self.password = password
		
	def get_user(self):
		return self.user
		
	def set_user(self, user):
		self.user = user
		
	def validate_password(self, password):
		if password == self.password:
			return True
		else:
			return False
