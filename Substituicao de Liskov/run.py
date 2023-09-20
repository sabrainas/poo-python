class PessoaA:
    def se_apresentar(self):
        print('Ola, sou a pessoa A')
    
class PessoaB:
    def __init__(self):
        super().__init__()

pessoa = PessoaA()
pessoa.se_apresentar()

def apresentar():
    print('Estou alterando esse método')

pessoa.se_apresentar = apresentar
pessoa.se_apresentar()