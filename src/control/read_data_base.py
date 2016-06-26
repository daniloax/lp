'''
Created on 25 de jun de 2016

@author: ska
'''

import sqlite3

from model.account import account
from model.activity import activity
from model.user import user

class read_data_base:
    
    QUERY_USER_SELECT = "SELECT * FROM user"
    QUERY_USER_INSERT = "INSERT INTO user (name, email, password) VALUES (?, ?, ?)"
    QUERY_ACTIVITY_CLOSE = "UPDATE activity SET active = 0 WHERE id = ?"
    QUERY_ACTIVITY_INSERT = "INSERT INTO activity (title, description, active, date, hour, fk_user_id) VALUES (?, ?, ?, ?, ?, ?)"
    QUERY_ACTIVITIES_SELECT = "SELECT * FROM activity WHERE fk_user_id = ?"

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
    
    def create_activity(self, data_base, activity):
        
        self.open_connection(data_base)
        cursor = self.conn.cursor()
        cursor.execute(self.QUERY_ACTIVITY_INSERT,(
                       activity.get_title(),
                       activity.get_description(),
                       activity.get_active(),
                       activity.get_date(),
                       activity.get_hour(),
                       activity.get_fk_user_id()))
        
        self.conn.commit()
        self.close_connection()
        
        return cursor.lastrowid
    
    def close_activity(self, data_base, activity_identifier):
        self.open_connection(data_base)
        cursor = self.conn.cursor()
        cursor.execute(self.QUERY_ACTIVITY_CLOSE,(
                       activity_identifier,))
        
        self.conn.commit()
        self.close_connection()
        
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
        
    def read_activities(self, data_base, account_identifier, activities):
        
        self.open_connection(data_base)
        cursor = self.conn.cursor()
        cursor.execute(self.QUERY_ACTIVITIES_SELECT, (account_identifier,))
        result_set = cursor.fetchall()
        
        for result in result_set:
            record = activity(result[0],result[1], result[2], result[6], result[3], result[4], result[5])
            activities.append(record)
            
        self.close_connection()
            

"""read_data_base = read_data_base()
accounts = []
read_data_base.read_accounts("../../gera.db", accounts)"""