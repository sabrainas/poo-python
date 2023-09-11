class Pessoa: #substantivos

    def __init__(self, name: str, idade: int) -> None:
        self.name = name
        self.idade = idade 
    
    def dirigir(self, veiculo: str) -> None: #verbos
        print('dirigindo um {}'.format(veiculo))
    
    def apresentar_idade(self) -> int:
        return self.idade