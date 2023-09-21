from abs_class import AbstractClass

class Filha(AbstractClass):
    def apresentar_metodos(self) -> None:
        print(self.atributo)

filha = Filha()
filha.apresentar_metodos()
filha.metodo('estou aqui')

#error
abstractClass = AbstractClass()
abstractClass.metodo('Fazendo algo')