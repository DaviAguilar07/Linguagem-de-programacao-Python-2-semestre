
class produto:
    def __init__(self, nome, marca, preço, tipo):
            self.nome = nome
            self.marca = marca
            self.preço = preço
            self.tipo = tipo

    def aplicar_desconto(self, percentual):
          self.preço = self.preço - (self.preço * percentual / 100)

    def status(self):
          return f'Nome: {self.nome}, marca: {self.marca}, preço: {self.preço}, tipo: {self.tipo}'

celular = produto('Iphone 18', 'Iphone', 20000, 'SmartPhone')

percentual = float(input('Qual o desconto oferecido pela loja (em %)? '))

celular.aplicar_desconto(percentual)

print(celular.status())

