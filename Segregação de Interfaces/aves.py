from interface import Ave

class Canario(Ave):
    def comer(self):
        print('Estou comendo')

    def voar(self):
        print('Estou voando')
    
    def gritar(self):
        print('Estou gritando')

class Pinguim(Ave):
    def comer(self):
        print('Estou comendo!')
    
    def voar(self):
        None
    def gritar(self):
        print('Estou gritanddo')