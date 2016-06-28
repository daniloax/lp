'''
Created on 26 de jun de 2016

@author: ska
'''

class alarm:

    def __init__(self, identifier, reminder, interval, repeat, active, fk_activity_id):
        self.identifier = identifier
        self.reminder = reminder
        self.interval = interval
        self.repeat = repeat
        self.active = active
        self.fk_activity_id = fk_activity_id

    def get_identifier(self):
        return self.identifier
    
    def set_identifier(self, identifier):
        self.identifier = identifier
        
    def get_reminder(self):
        return self.reminder
    
    def set_reminder(self, reminder):
        self.reminder = reminder
        
    def get_interval(self):
        return self.interval
    
    def set_interval(self, interval):
        self.interval = interval
        
    def get_repeat(self):
        return self.repeat
    
    def set_repeat(self, repeat):
        self.repeat = repeat
        
    def get_active(self):
        return self.active
    
    def set_active(self, active):
        self.active = active
        
    def get_fk_activity_id(self):
        return self.fk_activity_id
    
    def set_fk_activity_id(self, fk_activity_id):
        self.fk_activity_id = fk_activity_id