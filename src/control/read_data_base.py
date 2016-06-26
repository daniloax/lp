'''
Created on 25 de jun de 2016

@author: ska
'''

import sqlite3

from model.account import account
from model.user import user

class read_data_base:
    
    QUERY_USER_SELECT = "SELECT * FROM user"
    QUERY_USER_INSERT = "INSERT INTO user (name, email, password) VALUES (?, ?, ?)"

    def __init__(self):
        self.conn = None
        
    def open_connection(self, data_base):
        self.conn = sqlite3.connect(data_base)
        
    def close_connection(self):
        self.conn.close()
        
    def create_account(self, data_base, account):
        
        self.open_connection(data_base)
        cursor = self.conn.cursor()
        cursor.execute(self.QUERY_USER_INSERT,(
                       account.get_user().get_name(),
                       account.get_user().get_email(),
                       account.get_password()))
        
        self.conn.commit()
        self.close_connection()
        
        return cursor.lastrowid
        
    def read_accounts(self, data_base, accounts):
        
        self.open_connection(data_base)
        cursor = self.conn.cursor()
        cursor.execute(self.QUERY_USER_SELECT)
        result_set = cursor.fetchall()
        
        for result in result_set:
            new_user = user(result[1],result[2])
            record = account(result[0], result[3], new_user)
            accounts.append(record)
            
        self.close_connection()
            

"""read_data_base = read_data_base()
accounts = []
read_data_base.read_accounts("../../gera.db", accounts)"""