from produtos import Produto
from carrinho import CarrinhoDeCompras

car = CarrinhoDeCompras()
monitor = Produto('Monitor', 1000)
cerveja = Produto('Cerveja', 5)
tv = Produto('TV', 1200)

car.adicionar_produtos(monitor)
car.adicionar_produtos(cerveja)
car.adicionar_produtos(tv)

car.finalizar_compra()