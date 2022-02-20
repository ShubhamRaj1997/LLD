class ExpanseMeta(object):
    def __init__(self, name , img, notes):
        self.__name = name
        self.__img = img
        self.__notes = notes
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def img(self):
        return self.__img
    
    @img.setter
    def img(self, value):
        self.__img = value
        
    @property
    def notes(self):
        return self.__notes
    
    @notes.setter
    def notes(self, value):
        self.__notes = value