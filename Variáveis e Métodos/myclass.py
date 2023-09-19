class MinhaClasse:
    estatico = 'lhama' #variavel de classe

    def __init__(self, estado):
        self.estado = estado

    def print_estatico(self):
        print(self.estatico)
    
    @classmethod
    def mudar_estatico(cls):
        MinhaClasse.estatico = 'Programador'

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)

obj1.mudar_estatico()
obj1.print_estatico()

print(obj1.estatico)