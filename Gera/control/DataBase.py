"""
	DataBase
	---------------------------------
	version: 0.0.1
	date: Jun 18, 2016
	author: daniloax

"""

import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import model.Account
from control.ReadTextFile import ReadTextFile

class DataBase:
	def __init__(self):
		self.readTextFile = ReadTextFile()
		
	def readAccounts(self, fileName, accounts):
		readTextFile.readAccounts(fileName, accounts)
