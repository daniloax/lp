'''
Created on 25 de jun de 2016

'''

import sqlite3

from model.account import account
from model.activity import activity
from model.alarm import alarm
from model.user import user

class read_data_base:
    
    QUERY_USER_SELECT = "SELECT * FROM user"
    QUERY_USER_INSERT = "INSERT INTO user (name, email, password) VALUES (?, ?, ?)"
    QUERY_ACTIVITY_CLOSE = "UPDATE activity SET active = 0 WHERE id = ?"
    QUERY_ACTIVITY_OPEN = "UPDATE activity SET active = 1 WHERE id = ?"
    QUERY_ACTIVITY_INSERT = "INSERT INTO activity (title, description, active, date, hour, fk_user_id) VALUES (?, ?, ?, ?, ?, ?)"
    QUERY_ACTIVITIES_SELECT = "SELECT * FROM activity WHERE fk_user_id = ?"
    QUERY_ALARM_CLOSE = "UPDATE alarm SET active = 0 WHERE id = ?"
    QUERY_ALARM_OPEN = "UPDATE alarm SET active = 1 WHERE id = ?"
    QUERY_ALARM_INSERT = "INSERT INTO alarm (reminder, interval, repeat, active, fk_activity_id) VALUES (?, ?, ?, ?, ?)"
    QUERY_ALARMS_SELECT = "SELECT * FROM alarm WHERE fk_activity_id = ?"

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
        
    def open_activity(self, data_base, activity_identifier):
        self.open_connection(data_base)
        cursor = self.conn.cursor()
        cursor.execute(self.QUERY_ACTIVITY_OPEN,(
                       activity_identifier,))
        
        self.conn.commit()
        self.close_connection()
        
    def create_alarm(self, data_base, alarm):
        
        self.open_connection(data_base)
        cursor = self.conn.cursor()
        cursor.execute(self.QUERY_ALARM_INSERT,(
                       alarm.get_reminder(),
                       alarm.get_interval(),
                       alarm.get_repeat(),
                       alarm.get_active(),
                       alarm.get_fk_activity_id()))
        
        self.conn.commit()
        self.close_connection()
        
        return cursor.lastrowid
        
    def close_alarm(self, data_base, alarm_identifier):
        self.open_connection(data_base)
        cursor = self.conn.cursor()
        cursor.execute(self.QUERY_ALARM_CLOSE,(
                       alarm_identifier,))
        
        self.conn.commit()
        self.close_connection()
        
    def open_alarm(self, data_base, alarm_identifier):
        self.open_connection(data_base)
        cursor = self.conn.cursor()
        cursor.execute(self.QUERY_ALARM_OPEN,(
                       alarm_identifier,))
        
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
        
    def read_alarms(self, data_base, activity_identifier, alarms):
        
        self.open_connection(data_base)
        cursor = self.conn.cursor()
        cursor.execute(self.QUERY_ALARMS_SELECT, (activity_identifier,))
        result_set = cursor.fetchall()
        
        for result in result_set:
            record = alarm(result[0], result[3], result[5], result[2], result[1], result[4])
            alarms.append(record)
            
        self.close_connection()
        

"""read_data_base = read_data_base()
accounts = []
read_data_base.read_accounts("../../gera.db", accounts)"""