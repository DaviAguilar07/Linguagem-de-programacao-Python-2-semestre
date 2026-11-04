class pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero
    def cumprimentar(self):
        return f'Oi, meu nome é {self.nome}.'
    def aniversario(self):
        self.idade += 1

pessoa1 = pessoa('João', 30, 'Masculino')

print(pessoa1.cumprimentar())
pessoa1.aniversario() #Aciona a função de aniversário
print(f'Fiz meu aniversário, agora tenho {pessoa1.idade} anos de idade.') #Será impresso 31, pois o aniversário foi chamado antes.
print(f'Sou do gênero {pessoa1.genero}')

