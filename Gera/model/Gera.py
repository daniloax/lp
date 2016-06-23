"""
	Gera
	---------------------------------
	version: 0.0.1
	date: Jun 18, 2016
	author: daniloax
"""

import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from GeraDataBase import GeraDataBase
from Keypad import Keypad
from Screen import Screen

class Gera:
	
	def __init__(self):
		
		self.userAuthenticated = False
		self.currentAccountNumber = 0
		self.geraDataBase = GeraDataBase()
		self.keypad = Keypad()
		self.screen = Screen()
	
	def run(self):
		
		while True:
			
			self.screen.displayMessage("\nWelcome!");
			self.processRequests()
			userAuthenticated = False;
			currentAccountNumber = 0;
			
	def displayMenuOption(self):
		
		while True:
			
			self.screen.displayMessage("\nMenu option")
			self.screen.displayMessage("[1] Sign in")
			self.screen.displayMessage("[2] Sign up")
			self.screen.displayMessage("[3] End of run")
			self.screen.displayMessage( "? " )
			userType = self.keypad.getInput()
			
			if userType < 1 or userType > 3:
				break
				
			return userType
		
	def processRequests(self):
		
		menuOption = self.displayMenuOption()
		
		if menuOption == 1:
			self.geraDataBase.readAccounts()

		elif menuOption == 2:
			self.screen.displayMessage("\nSIGN_UP")
		
		elif menuOption == 3:
			self.screen.displayMessage("\nExiting the system...")
			sys.exit()
