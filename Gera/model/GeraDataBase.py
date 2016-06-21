"""
	GeraDataBase
	---------------------------------
	version: 0.0.1
	date: Jun 21, 2016
	author: daniloax
	
"""

from control.DataBase import DataBase

class Gera:
	
	def __init__(self):
		self.dataBase = DataBase()
		
	def getUser(self, account):
		return getAccount(account).getName()
	
	def getAccount(self, account):
		return account
