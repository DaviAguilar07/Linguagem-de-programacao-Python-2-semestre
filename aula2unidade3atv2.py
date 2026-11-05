import pandas as pd

nomes = []
idades = []

qtd = int(input('Quantas pessoas deseja cadastrar? '))

for i in range(qtd):
    nome = str(input(f'Qual o nome da {i+1}° pessoa? '))
    idade = int(input(f'Idade: '))

    nomes.append(nome)
    idades.append(idade)

dados = {
    'Nome':nomes, 
    'Idade': idades
}

series_idades = pd.Series(dados['Idade'], index = dados['Nome'])
print('-'*5, 'Lista', '-'*5)
print(series_idades)

print('-'*5, 'Cálculo', '-'*5)
print(f'A média das idades é de {series_idades.mean():.2f}.')
print(f'O mais velho tem {series_idades.max()} anos e se chama {series_idades.idxmax()}.') #Imprime o valor máximo e imprime o indice correspondente 
print(f'O mais novo tem {series_idades.min()} anos e se chama {series_idades.idxmin()}.') #Imprime o valor máximo e imprime o indice correspondente 

