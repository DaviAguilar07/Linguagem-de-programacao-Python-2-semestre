class veiculo:
        def __init__(self, marca, modelo, ano):
            self.marca = marca
            self.modelo = modelo
            self.ano = ano
            self.velocidade = 0
        def acelerar(self, incremento):
              self.velocidade += incremento
        def frear(self, decremento):
              self.velocidade -= decremento
        def status(self):
              return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} Km/h.'

class carro(veiculo):
                def __init__(self, marca, modelo, ano, potencia):
                    super().__init__(marca, modelo, ano) # O super() é como se fosse um copia e cola de totas as atribuições do self. Isso diminui linhas de código.
                    self.potencia = potencia

                def acelerar(self, incremento):
                    self.velocidade += incremento + self.potencia

class bicicleta(veiculo):
                def __init__(self, marca, modelo, ano, tipo):
                        super().__init__(marca, modelo, ano) # O super() é como se fosse um copia e cola de totas as atribuições do self. Isso diminui linhas de código.
                        self.tipo = tipo
                def status(self):
                        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Tipo: {self.tipo}, Velocidade: {self.velocidade} Km/h.'

carro1 = carro('Toyota', 'Sedan', 2022, 130)
bicicleta1 = bicicleta('BMX', 'Freestyle', '2015', 'Street')

carro1.acelerar(80)
bicicleta1.acelerar(20)

print(f'Status do carro: ')
print(f'{carro1.status()}')

print(f'Status da bicicleta: ')
print(f'{bicicleta1.status()}')
