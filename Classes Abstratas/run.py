from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def metodo_abstrato(self) -> None:
        pass