"""
	GeraDataBase
	---------------------------------
	version: 0.0.1
	date: Jun 21, 2016
	author: daniloax
	
"""

import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from control.DataBase import DataBase

class GeraDataBase:
	
	def __init__(self):
		self.dataBase = DataBase()
		self.accounts = []
		
	def getUser(self, account):
		return getAccount(account).getName()
	
	def getAccount(self, account):
		for currentAccount in self.accounts:
			if currentAccount == account:
				return currentAccount
		return None
		
	def getAccounts(self):
		return self.accounts
		
	def authenticateUser(self, account, password):
		userAccount = getAccount(account)
		if userAccount != None:
			return userAccount.validatePassword(password)
		else:
			return False
			
	def getUser(self, account):
		return getAccount(account).getUser()
		
	def readAccounts(self):
		self.dataBase.readAccounts("account.txt", self.accounts)
		
		
