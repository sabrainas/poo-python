class Casa:
    def __init__(self) -> None:
        self.__endereco = 'Rua dos Limoeiros'
        self.__proprietario = None 
    
    def acender_luzes(self) -> None:
        print('Estou acendendo as luzes')
    
    def get_endereco(self) -> str:
        return self.__endereco
    
    def set_proprietario(self, proprietario: any) -> None:
        self.__proprietario = proprietario
    
    def get_proprietario(self) -> any:
        return self.__proprietario