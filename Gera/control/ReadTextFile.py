"""
	ReadTextFile
	---------------------------------
	version: 0.0.1
	date: Jun 22, 2016
	author: daniloax

"""
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import model.Account
import model.User

class ReadTextFile:
	def __init__(self):
		self.fileInput = None
		
	def openFile(self, fileName):
		self.fileInput = open(fileName, 'r')
		
	def readAccounts(self, fileName, accounts):
		record = Account();
		self.openFile(fileName)
		
