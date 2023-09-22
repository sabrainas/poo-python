from interface import Repositorio

class MySqlRepositorio(Repositorio):
    def inserir(self, dado) -> None:
        print('Inserindo {} no banco MySql'.format(dado))
    
    def deletar(self, dado) -> None:
        print('Removendo {} no banco MySql'.format(dado))
        