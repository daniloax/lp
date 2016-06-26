'''
Created on 26 de jun de 2016

@author: ska
'''

class activity:

    def __init__(self, identifier, title, description, date, hour, fk_user_id):
        self.identifier = identifier
        self.title = title
        self.description = description
        self.date = date
        self.hour = hour
        self.fk_user_id = fk_user_id
        
    def get_identifier(self):
        return self.identifier
    
    def set_identifier(self, identifier):
        self.identifier = identifier
        
    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title
        
    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description
        
    def get_date(self):
        return self.date
    
    def set_date(self, date):
        self.date = date
        
    def get_hour(self):
        return self.hour
    
    def set_hour(self, hour):
        self.hour = hour
        
    def get_fk_user_id(self):
        return self.fk_user_id
    
    def set_fk_user_id(self, fk_user_id):
        self.fk_user_id = fk_user_id