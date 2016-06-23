"""
	User
	---------------------------------
	version: 0.0.1
	date: Jun 18, 2016
	author: daniloax

"""

class User:
	def __init__(self, name):
		self.name = name
		
	def getName(self):
		return self.name
	
	def setName(self, name):
		self.name = name
	
