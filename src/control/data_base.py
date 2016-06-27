"""
	DataBase
	---------------------------------
	version: 0.0.1
	date: Jun 18, 2016
	author: daniloax

"""

from control.read_data_base import read_data_base
from control.read_text_file import read_text_file

class data_base:
	def __init__(self):
		self.read_data_base = read_data_base()
		self.read_text_file = read_text_file()
		
	def read_accounts(self, file_name, accounts):
		self.read_data_base.read_accounts(file_name, accounts)
		
	def read_activities(self, file_name, account_identifier, activities):
		self.read_data_base.read_activities(file_name, account_identifier, activities)
		
	def read_alarms(self, file_name, activity_identifier, alarms):
		self.read_data_base.read_alarms(file_name, activity_identifier, alarms)
		
	def create_account(self, file_name, account):
		return self.read_data_base.create_account(file_name, account)
	
	def create_activity(self, file_name, activity):
		return self.read_data_base.create_activity(file_name, activity)
	
	def close_activity(self, file_name, activity_identifier):
		self.read_data_base.close_activity(file_name, activity_identifier)
	
	def open_activity(self, file_name, activity_identifier):
		self.read_data_base.open_activity(file_name, activity_identifier)
		
	def create_alarm(self, file_name, alarm):
		return self.read_data_base.create_alarm(file_name, alarm)
	
	def close_alarm(self, file_name, alarm_identifier):
		self.read_data_base.close_alarm(file_name, alarm_identifier)
		
	def open_alarm(self, file_name, alarm_identifier):
		self.read_data_base.open_alarm(file_name, alarm_identifier)