class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf 

    def print_cpf(self):
        print(self.__cpf)

    def correr(self):
        print('Estou correndo')

    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentarDocumento()
        print('bebendo...')
    
    def __apresentarDocumento(self):
        print(self.__cpf)

sabrina = Pessoa('Sabrina', 19, '872193817')
#print(sabrina.nome)
#print(sabrina.idade)
#sabrina.print_cpf()

sabrina.beber('cerveja')