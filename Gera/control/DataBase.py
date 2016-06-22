"""
	DataBase
	---------------------------------
	version: 0.0.1
	date: Jun 18, 2016
	author: daniloax

"""

from account import Account
from readTextFile import ReadTextFile

class DataBase:
	def __init__(self):
		self.readTextFile = ReadTextFile
		
	def readAccounts(self, fileName):
		readTextFile.readAccounts(fileName)
