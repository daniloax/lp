"""
	Account
	---------------------------------
	version: 0.0.1
	date: Jun 18, 2016
	author: daniloax

"""

import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import model.User

class Account:
	
	def __init__(self, accountNumber, password, name):
		self.accountNumber = accountNumber
		self.password = password
		self.user = User(name)
		
	def getAccount(self):
		return self.account
		
	def setAccount(self, accountNumber):
		self.accountNumber = accountNumber
		
	def getUser(self):
		return self.user
		
	def setUser(self, user):
		self.user = user
		
	def getPassword(self):
		return self.password
		
	def setPassword(self, password):
		self.password = password
		
	def validatePassword(self, password):
		if password == self.password:
			return True
		else:
			return False
