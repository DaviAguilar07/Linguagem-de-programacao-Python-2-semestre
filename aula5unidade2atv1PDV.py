import matplotlib.pyplot as plt

class produto:
    def __init__(self, nome, preço, categoria, estoque):
        self.nome = nome
        self.preço = preço
        self.categoria = categoria
        self.estoque = estoque
    #Definimos com o produto aparece quando é impresso.
    def __str__(self):
        return f'Nome: {self.nome}| Preço: {self.preço}| Categoria: {self.categoria}| Estoque: {self.estoque}'


catalogo = []
categorias = []

def adicionar_produto(nome, preço, categoria, estoque):
        novo_produto = produto(nome, preço, categoria, estoque)
        catalogo.append(novo_produto)
        categorias.append(categoria)
        print(f'Produto {nome} adicionado ao catálogo.')

def lista_catalogo():
        print(f'---Catálogo da loja PDV---')
        for produto in catalogo:
            print(produto)

#Cadastrar produtos.
adicionar_produto('Notebook', 3500, 'Informática', 25)
adicionar_produto('Mesa', 1000, 'Móveis', 20)
adicionar_produto('Vassoura', 50, 'Doméstico', 60)
adicionar_produto('Televisão', 4000, 'Informática', 20)
adicionar_produto('Cadeira', 400, 'Móveis', 80)

lista_catalogo()

print()
#Removendo produto.

def remover_produto(nome):
     for p in catalogo:
          if p.nome == nome:
               catalogo.remove(p)
               categorias.remove(p.categoria)
               print(f'Produto {nome} removido do catálogo.')
               return
          
remover_produto('Mesa')
lista_catalogo()

#Construindo o gráfico.

#Gráfico por categoria.
categorias_unicas = list(set(categorias))

#Contagem de produtos em cada categoria.
contagem = list(categorias.count(cat) for cat in categorias_unicas)

plt.bar(categorias_unicas, contagem, color='royalblue')
plt.xlabel('\nCategorias')
plt.ylabel('Contagem')
plt.title('Gráfico de produtos na loja PDV')
