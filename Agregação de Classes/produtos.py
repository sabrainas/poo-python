class Produto:
    def __init__(self, prod_nome: str, prod_valor: int) -> None:
        self.__prod_nome = prod_nome
        self.__prod_valor = prod_valor

    def informacoes_produto(self) -> None:
        print('Produto: {} / valor: R${},00'.format(self.__prod_nome, self.__prod_valor))