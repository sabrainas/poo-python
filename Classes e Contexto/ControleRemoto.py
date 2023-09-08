class ControleRemoto:
    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo
    
    def avancarCanal(self):
        print('Canal Avancado')

    def voltarCanal(self):
        print('Canal Voltado')

    def escolherCanal(self, canal):
        print('Alterado para o canal: {}'.format(canal))

controleSala = ControleRemoto('samsung', 'sala')
print(controleSala.comodo)
print(controleSala.televisao)
controleSala.avancarCanal()
controleSala.escolherCanal(13)