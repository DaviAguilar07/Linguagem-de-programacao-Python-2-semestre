import matplotlib.pyplot as plt

class livro: #Orientado a objetos
    def __init__(self, nome, ano, estoque):
        self.nome = nome
        self.ano = ano
        self.estoque = estoque

    def __str__(self):
        return f'Nome: {self.nome}| Ano: {self.ano}| Estoque: {self.estoque}'#Vai ser inserido assim dentro do cadastro.

cadastro = []
ano_de_publi = []

def adicionar_cadastro(nome, ano, estoque):
    novo_livro = livro(nome, ano, estoque) #Essa linha que faz com que o cadastro seja inserido da maneira do def __str__
    cadastro.append(novo_livro)#Faz o append do return do def __str__
    ano_de_publi.append(ano)
    print(f'O livro {nome} foi adicionado á biblioteca.') #Só para imprimir o nome.


def imprimir_cadastro():
    for p in cadastro:
        print(p)

#Cadastrando os livros.
adicionar_cadastro('Pequeno Principe', 2000, 30)
adicionar_cadastro('Senhor dos Anéis', 2000, 50)
adicionar_cadastro('Pinóquio', 1990, 42)    

imprimir_cadastro()

#Facilitando o gráfico:

#Contagem de livros.
ano_unico = list(set(ano_de_publi)) #Deixa o ano como único. EX: Ano 2000 - 2 livros

contagem = list(ano_de_publi.count(ano) for ano in ano_unico) #Faz a contagem. Ex: De cima (2 livros).

#Construindo o gráfico.
plt.bar(ano_unico, contagem, color = 'royalblue')
plt.xlabel('\nAno de publicação')
plt.ylabel('Contagem')
plt.title('Gráfico da Biblioteca')