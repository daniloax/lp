"""
	User
	---------------------------------
	version: 0.0.1
	date: Jun 18, 2016
	author: daniloax

"""

class user:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		
	def get_name(self):
		return self.name
	
	def set_name(self, name):
		self.name = name
	
	def get_email(self):
		return self.email
	
	def set_email(self, email):
		self.email = email