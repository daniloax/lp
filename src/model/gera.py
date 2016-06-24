"""
	Gera
	---------------------------------
	version: 0.0.1
	date: Jun 18, 2016
	author: daniloax
"""

import sys

from model.gera_data_base import gera_data_base
from model.keypad import keypad
from model.screen import screen

class gera:
	
	def __init__(self):
		
		self.user_authenticated = False
		self.current_account_number = 0
		self.gera_data_base = gera_data_base()
		self.keypad = keypad()
		self.screen = screen()
	
	def run(self):
		
		while True:
			
			self.screen.display_message("\nWelcome!");
			self.process_requests()
			user_authenticated = False;
			current_account_number = 0;
			
	def display_menu_option(self):
		
		while True:
			
			self.screen.display_message("\nMenu option")
			self.screen.display_message("[1] Sign in")
			self.screen.display_message("[2] Sign up")
			self.screen.display_message("[3] End of run")
			self.screen.display_message( "? " )
			user_type = self.keypad.get_input()
			
			if user_type < 1 or user_type > 3:
				break
				
			return user_type
		
	def process_requests(self):
		
		menu_option = self.display_menu_option()
		
		if menu_option == 1:
			self.gera_data_base.read_accounts()

		elif menu_option == 2:
			self.screen.display_message("\nSIGN_UP")
		
		elif menu_option == 3:
			self.screen.display_message("\nExiting the system...")
			sys.exit()
