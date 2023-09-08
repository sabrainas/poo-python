class Calculadora:
    def calcular(self, op, num1, num2):
        if op == '+':
            return self.__adicao(num1, num2)
        elif op == '-':
            return self.__subtracao(num1, num2)
        else:
            print('operação invalida')

def __adicao(self, num1, num2):
    return num1 + num2

def __subtracao(self, num1, num2):
    return num1 - num2

calculadora = Calculadora()
resultado = calculadora.calcular('+', 3, 2)
print(resultado)