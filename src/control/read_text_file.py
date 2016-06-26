"""
	ReadTextFile
	---------------------------------
	version: 0.0.1
	date: Jun 22, 2016
	author: daniloax

"""

from model.account import account
from model.user import user

class read_text_file:
	def __init__(self):
		self.input_file = None
		
	def open_file(self, file_name):
		self.input_file = open(file_name, 'r')
		
	def read_accounts(self, file_name, accounts):

		self.open_file(file_name)
		
		for line in self.input_file:
			user_account = line.split()
			new_user = user(user_account[2], user_account[3])
			record = account(int(user_account[0]), int(user_account[1]), new_user)
			#print(record.get_identifier(), record.get_password(), record.get_user().get_name(), record.get_user().get_email())
			accounts.append(record)
			
		
		"""for line in self.input_file:
			account, password, user_name, email = (item.strip() for item in line.split(" ", 3))
			info[account] = dict(zip(('password', "user_name", 'email'),(password, user_name, email)))
	
		print('info:')
		for account, record in info.items():
			print('  account %r:' % account)
			for field, value in record.items():
				print('    %s: %s' % (field, value))"""