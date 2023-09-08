class MinhaClasse: 
    
    def __init__(self, att):
        self.meu_atributo = 'Ola mundo'
        self.meu_atributo2 = att

    def meuMetodo(self): #self sempre irá se referenciar a classe
        print('Estou no metodo!')

    def meuMetodo2(self, num, mult):
        return num * mult
    
objeto = MinhaClasse('meu atributo')
print(objeto.meu_atributo2)

#att = print(objeto.meu_atributo)
#resultado = objeto.meuMetodo2(2, 3)
#print(resultado)
#objeto = MinhaClasse()
#objeto.meuMetodo()