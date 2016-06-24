"""
	Gera
	---------------------------------
	version: 0.0.1
	date: Jun 18, 2016
	author: daniloax
"""

import string, sys

from model.gera_data_base import gera_data_base
from model.keypad import keypad
from model.screen import screen

class gera:
	
	"""	
	 " construtor sem argumentos de Radar inicializa as variaveis de instancia
	 "
	"""
	def __init__(self):
		
		self.user_authenticated = False
		self.current_account_identifier = 0
		self.gera_data_base = gera_data_base()
		self.keypad = keypad()
		self.screen = screen()
	
	"""	
	 " inicia o gera
	 "
	"""
	def run(self):
		
		while True:
			
			self.screen.display_message("\nWelcome!")
			self.process_requests()
			
			while not self.user_authenticated:
				self.authenticate_user()
				
			self.screen.display_message("\nHi, {}!".format(self.gera_data_base.get_user(self.current_account_identifier).get_name()))
			
			self.perform_transactions()
				
			self.user_authenticated = False;
			self.current_account_identifier = 0;
			
	
	"""	
	 " exibe o menu de opcoes e retorna uma selecao de entrada
	 "
	"""
	def display_menu_option(self):
		
		while True:
			
			self.screen.display_message("\nMenu option")
			self.screen.display_message("[1] Sign in")
			self.screen.display_message("[2] Sign up")
			self.screen.display_message("[3] End of run")
			self.screen.display_message( "\n? " )
			user_type = self.keypad.get_input()
			
			if user_type < 1 or user_type > 3:
				break
				
			return user_type
	
	"""	
	 " executa o menu de opcoes e processa requisicoes
	 "
	"""
	def process_requests(self):
		
		menu_option = self.display_menu_option()
		
		if menu_option == 1:
			self.gera_data_base.read_accounts()

		elif menu_option == 2:
			self.screen.display_message("\nSIGN_UP")
		
		elif menu_option == 3:
			self.screen.display_message("\nExiting the system...")
			sys.exit()
			
	"""	
	 " tenta autenticar o usuario contra o banco de dados
	 "
	"""
	def authenticate_user(self):
		
		self.screen.display_message("\nPlease enter your account identifier:")
		identifier = self.keypad.get_input()
		self.screen.display_message("\nEnter your password:")
		password = self.keypad.get_input()
		
		self.user_authenticated = self.gera_data_base.authenticate_user(identifier, password)
		
		if (self.user_authenticated):
			self.current_account_identifier = identifier
			
		else:
			self.screen.display_message("\nInvalid account number or password. Please try again.")
	
	"""	
	 " exibe o menu principal e retorna uma selecao de entrada
	 "
	"""
	def display_main_menu(self):
		
		while True:
			
			self.screen.display_message("\nMain menu:")
			self.screen.display_message("[1] Activity create ")
			self.screen.display_message("[2] Alarm create")
			self.screen.display_message("[3] Exit\n")
			self.screen.display_message("Enter a choice: ")
			
			user_type = self.keypad.get_input()
			
			if user_type < 1 or user_type > 3:
				break
			
			return user_type

		
	"""	
	 " executa o menu principal e realiza transacoes
	 "
	"""
	def perform_transactions(self):
		
		user_exited = False
		
		while (not user_exited):
			
			main_menu_selection = self.display_main_menu() 
			
			if main_menu_selection == 1:
				self.screen.display_message("\nMenu selection [{}]".format(main_menu_selection))
	
			elif main_menu_selection == 2:
				self.screen.display_message("\nMenu selection [{}]".format(main_menu_selection))
			
			elif main_menu_selection == 3:
				self.screen.display_message("\nGoodbye!")
				user_exited = True
				sys.exit()