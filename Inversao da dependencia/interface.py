from abc import ABC, abstractmethod

class Repositorio(ABC):
    @abstractmethod
    def inserir(self, dado) -> None:
        pass
    @abstractmethod
    def deletar(self, dado) -> None:
        pass