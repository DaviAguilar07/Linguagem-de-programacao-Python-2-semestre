class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_barulho(self):
        pass  # Método genérico, será sobrescrito nas subclasses, deixa em branco (deixa passar sem nada).

class Cachorro(Animal):
    def fazer_barulho(self):
        return "latir" #Insere um valor ao pass.

class Gato(Animal):
    def fazer_barulho(self):
        return "miar" #Insere um valor ao pass.

rex = Cachorro("Rex")
whiskers = Gato("Whiskers")

print(f'O {rex.nome} faz {rex.fazer_barulho()}.')
print(f'O {whiskers.nome} faz {whiskers.fazer_barulho()}.')
