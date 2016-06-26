"""
	Gera
	---------------------------------
	version: 0.0.1
	date: Jun 18, 2016
	author: daniloax
"""

import sys

from model.account import account
from model.activity import activity
from model.gera_data_base import gera_data_base
from model.keypad import keypad
from model.user import user
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
			
			self.gera_data_base.read_activities(self.current_account_identifier)
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
			user_type = int(self.keypad.get_input())
			
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
			self.create_account()
			self.process_requests()
		
		elif menu_option == 3:
			self.screen.display_message("\nExiting the system...")
			sys.exit()
			
	"""	
	 " tenta autenticar o usuario contra o banco de dados
	 "
	"""
	def authenticate_user(self):
		
		self.screen.display_message("\nPlease enter your account identifier:")
		identifier = int(self.keypad.get_input())
		self.screen.display_message("\nEnter your password:")
		password = "{}".format(self.keypad.get_input())
		
		self.user_authenticated = self.gera_data_base.authenticate_user(identifier, password)
		
		if (self.user_authenticated):
			self.current_account_identifier = identifier
			
		else:
			self.screen.display_message("\nInvalid account number or password. Please try again.")
			
	"""	
	 " cadastra um novo usuario no banco de dados
	 "
	"""
	def create_account(self):
		
		self.screen.display_message("\nPlease enter your name:")
		name = self.keypad.get_input()
		self.screen.display_message("\nEnter your email:")
		email = self.keypad.get_input()
		self.screen.display_message("\nEnter your password:")
		password = self.keypad.get_input()
		
		new_user = user(name, email)
		new_account = account(None, password, new_user)
		
		new_user_identifier = self.gera_data_base.create_account(new_account)
		
		self.screen.display_message("\nAccount registered successfully!")
		self.screen.display_message("\nUse your account identifier \'{}\' to sign in!".format(new_user_identifier))
		
	"""	
	 " cadastra uma nova atividade no banco de dados
	 "
	"""
	def create_activity(self):
		
		self.screen.display_message("\nPlease enter your activity title:")
		title = self.keypad.get_input()
		self.screen.display_message("\nEnter your activity description:")
		description = self.keypad.get_input()
		self.screen.display_message("\nEnter your activity date:")
		date = self.keypad.get_input()
		self.screen.display_message("\nEnter your activity hour:")
		hour = self.keypad.get_input()
		
		new_activity = activity(None, title, description, date, hour, self.current_account_identifier)
		
		new_activity_identifier = self.gera_data_base.create_activity(new_activity)
		
		self.screen.display_message("\nActivity created successfully!")
		self.screen.display_message("\nUse your activity identifier \'{}\' to manage it!".format(new_activity_identifier))
	
	"""	
	 " exibe o menu principal e retorna uma selecao de entrada
	 "
	"""
	def display_main_menu(self):
		
		while True:
			
			self.screen.display_message("\nMain menu:")
			self.screen.display_message("[1] Activity")
			self.screen.display_message("[2] Exit\n")
			self.screen.display_message("Enter a choice: ")
			
			user_type = int(self.keypad.get_input())
			
			if user_type < 1 or user_type > 2:
				break
			
			return user_type
		
	"""	
	 " exibe o menu de atividades e retorna uma selecao de entrada
	 "
	"""
	def display_activity_menu(self):
		
		while True:
			
			self.screen.display_message("\nActivity menu:")
			self.screen.display_message("[1] Activity create")
			self.screen.display_message("[2] Activity view")
			self.screen.display_message("[3] Activity update")
			self.screen.display_message("[4] Activity close")
			self.screen.display_message("[5] Activities list")
			self.screen.display_message("[6] Exit\n")
			self.screen.display_message("Enter a choice: ")
			
			user_type = int(self.keypad.get_input())
			
			if user_type < 1 or user_type > 6:
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
				self.perform_activity_transactions()
	
			elif main_menu_selection == 2:
				self.screen.display_message("\nGoodbye {}!".format(self.gera_data_base.get_user(self.current_account_identifier).get_name()))
				user_exited = True
				
	"""	
	 " executa o menu de atividades e realiza transacoes
	 "
	"""
	def perform_activity_transactions(self):
		
		menu_returned = False
		
		while (not menu_returned):
	
			activity_menu_selection = self.display_activity_menu()
			
			if activity_menu_selection == 1:
				self.create_activity()
				
			elif activity_menu_selection == 2:
				self.view_activity()
				
			elif activity_menu_selection == 3:
				self.update_activity()
				
			elif activity_menu_selection == 4:
				self.close_activity()
				
			elif activity_menu_selection == 5:
				self.list_activities()
				
			elif activity_menu_selection == 6:
				self.screen.display_message("\nReturning to main menu...")
				menu_returned = True
	
	"""	
	 " lista as atividades do usuario atual
	 "
	"""
	def list_activities(self):
		print('\nactivities:\n')
		for activity in self.gera_data_base.get_activities():
			self.screen.display_message("  activity: {}".format(activity.get_title().encode('iso8859-1')))
			self.screen.display_message("    identifier: {}".format(activity.get_identifier()))
			self.screen.display_message("    date: {}".format(activity.get_date()))
			self.screen.display_message("    hour: {}\n".format(activity.get_hour()))
	
	"""	
	 " visualiza atividade
	 "
	"""
	def view_activity(self):
		self.screen.display_message("\nPlease enter your activity identifier:")
		activity_identifier = self.keypad.get_input()
		activity = self.gera_data_base.get_activity(activity_identifier)
		print('\ninfo:\n')
		self.screen.display_message("  activity: {}".format(activity.get_title().encode('iso8859-1')))
		self.screen.display_message("    description: {}".format(activity.get_description().encode('iso8859-1')))
		self.screen.display_message("    date: {}".format(activity.get_date()))
		self.screen.display_message("    hour: {}\n".format(activity.get_hour()))