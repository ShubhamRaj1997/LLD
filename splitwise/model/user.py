import itertools


class User(object):
    itr = itertools.count()

    def __init__(self, name, email, phone):
        self._id = next(self.itr)
        self.__name = name
        self.__email = email
        self.__phone = phone
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, value):
        self.__phone = value
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value



    
        