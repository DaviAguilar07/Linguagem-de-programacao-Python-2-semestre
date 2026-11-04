# Importando a biblioteca Matplotlib para gerar gráficos
import matplotlib.pyplot as plt

# Definição da classe 'livros' que representa cada livro no sistema
class livros:
    # Método construtor (__init__) que inicializa os atributos do livro
    def __init__(self, titulo, autor, genero, estoque):
        self.titulo = titulo      # Armazena o título do livro
        self.autor = autor        # Armazena o nome do autor
        self.genero = genero      # Armazena o gênero literário
        self.estoque = estoque    # Armazena a quantidade disponível em estoque
    
    # Método especial __str__ que define como o objeto será exibido ao ser impresso
    def __str__(self):
        # Retorna uma string formatada com todas as informações do livro
        return f'Título: {self.titulo}| Autor: {self.autor}| Gênero: {self.genero}| Estoque: {self.estoque}'


# Lista que vai armazenar todos os objetos da classe 'livros' cadastrados
livros_cadastro = []

# Lista auxiliar que vai armazenar apenas os gêneros dos livros cadastrados
generos_cadastro = []

# Função para adicionar novos livros ao sistema
def adicionar_livros(titulo, autor, genero, estoque):
    # Cria um novo objeto da classe 'livros' com os dados fornecidos
    novo_livro = livros(titulo, autor, genero, estoque)
    # Adiciona o objeto criado à lista principal de livros
    livros_cadastro.append(novo_livro)
    # Adiciona o gênero do livro à lista de gêneros (para facilitar o gráfico depois)
    generos_cadastro.append(genero)

# Função para imprimir todos os livros cadastrados
def imprimir_livro():
    # Percorre a lista de livros e imprime cada um usando o método __str__
    for p in livros_cadastro:
        print(p)

# Cadastro inicial de alguns livros para teste do sistema
adicionar_livros("Dom Casmurro", "Machado de Assis", "Romance", 5)
adicionar_livros("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Fantasia", 8)
adicionar_livros("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia", 4)
adicionar_livros("1984", "George Orwell", "Ficção científica", 6)
adicionar_livros("O Hobbit", "J.R.R. Tolkien", "Fantasia", 3)

# Impressão estética para separar a listagem dos livros
print('-='*20, 'Lista de livros', '-='*20) # Cria uma linha decorativa com título
print() # Quebra de linha para deixar o resultado mais organizado

# Chama a função que imprime todos os livros cadastrados
imprimir_livro()

print() # Quebra de linha para separar visualmente as seções

print(f'-----Realizando busca de livro-----')

# Função para buscar um livro pelo título
def buscar_livro(titulo):
    # Percorre a lista de livros cadastrados
    for p in livros_cadastro:
        # Verifica se o título do livro corresponde ao título buscado
        if p.titulo == titulo:
            # Se encontrar, imprime o resultado formatado
            print(f'Resultado: {p}.')
            return
    # Caso não encontre o título, será impresso
    print(f'Livro não encontrado.')

# Teste da função de busca: procurando "Dom Casmurro"
buscar_livro('Dom Casmurro')

# Preparação dos dados para o gráfico
# 'set' remove duplicidades da lista de gêneros, deixando apenas valores únicos
generos_unico = list(set(generos_cadastro))

#Essa linha cria uma lista chamada contagem, onde cada elemento representa quantos exemplares existem em estoque para cada gênero literário.
contagem = [sum(l.estoque for l in livros_cadastro if l.genero == gen) for gen in generos_unico]

# Criação do gráfico de barras
plt.bar(generos_unico, contagem, color = 'royalblue') # Barras azuis
plt.xlabel('\nGêneros') # Rótulo do eixo X
plt.ylabel('Contagem')  # Rótulo do eixo Y
plt.title('Sistema de Gerenciamento de Livros') # Título do gráfico
plt.show() # Exibe o gráfico
