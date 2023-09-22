from typing import Type 
from interface import Repositorio 

class Usuario:
    def __init__(self, repositorio: Type[Repositorio]) -> None:
        self.__repositorio = repositorio
        self.__repositorio

    def armazenar_dados(self, dado: any) -> None:
        self.__repositorio.inserir(dado)
    
    def remover_dado(self, dado: any) -> None:
        self.__repositorio.__deletar(dado)
