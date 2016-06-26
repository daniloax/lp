"""
	GeraDataBase
	---------------------------------
	version: 0.0.1
	date: Jun 21, 2016
	author: daniloax
	
"""

from control.data_base import data_base

class gera_data_base:
	
	DATA_BASE = ["../../account.txt", "../../gera.db"]
	
	def __init__(self):
		self.data_base = data_base()
		self.accounts = []
		self.activities = []
		
	def get_user(self, account_identifier):
		return self.get_account(account_identifier).get_user()
	
	def get_account(self, account_identifier):
		for current_account in self.accounts:
			if (current_account.get_identifier() == account_identifier):
				return current_account
		return None
	
	def get_activity(self, activity_identifier):
		for current_activity in self.activities:
			if (current_activity.get_identifier() == activity_identifier):
				return current_activity
		return None
		
	def get_accounts(self):
		return self.accounts
	
	def get_activities(self):
		return self.activities
		
	def authenticate_user(self, account_identifier, password):
		account = self.get_account(account_identifier)
		if account is not None:
			return account.validate_password(password)
		else:
			return False
		
	def create_account(self, account):
		return self.data_base.create_account(self.DATA_BASE[1], account)
	
	def create_activity(self, activity):
		return self.data_base.create_activity(self.DATA_BASE[1], activity)
	
	def read_accounts(self):
		self.data_base.read_accounts(self.DATA_BASE[1], self.accounts)
		
	def read_activities(self, account_identifier):
		self.data_base.read_activities(self.DATA_BASE[1], account_identifier, self.activities)
			
		
		
		
