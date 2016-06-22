"""
	ReadTextFile
	---------------------------------
	version: 0.0.1
	date: Jun 22, 2016
	author: daniloax

"""

class ReadTextFile:
	def __init__(self):
		self.fileInput = None
		
	def openFile(self, fileName):
		self.fileInput = open(fileName, 'r')
		
	def readFile(self):
		self.fileInput.read()
		
readTextFile = ReadTextFile()
readTextFile.openFile("account.txt")
readTextFile.readLine()
