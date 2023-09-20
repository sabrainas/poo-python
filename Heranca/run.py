class Mae:
    def __init__(self, endereco) -> None:
        self.endereco = endereco
    
    def comer(self) -> None: 
        print('Estou comendo!!')
    
    def estudar(self) -> None:
        print('Estou estudando')

class Filha(Mae):
    def __init__(self, endereco):
        super().__init__(endereco)
    
    def brincar(self, brinquedo: str) -> None:
        print('estou brincando com {}'.format(brinquedo))

ana = Mae('Rua Elvira')
clara = Filha('Rua do Bolo')
clara.brincar('boneca')