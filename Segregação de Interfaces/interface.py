from abc import ABC, abstractmethod

class Ave(ABC):
    @abstractmethod
    def comer(self):
        raise 'should implement comer method'
    
    @abstractmethod
    def voar(self):
        raise 'should implement voar method'
    
    @abstractmethod
    def gritar(self):
        raise 'should implement gritar method'