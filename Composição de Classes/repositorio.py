from insert import Insert
from select import Select

class Repositorio:
    def __init__(self):
        self.__insert = Insert()
        self.__select = Select()
    
    def select_by_id(self): 
        self.__select.select_one()