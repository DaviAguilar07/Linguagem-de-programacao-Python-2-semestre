import pandas as pd

dados = {
    'Nome': ['Luisa', 'Jonas', 'Paulo', 'Mariana'],
    'Idade': [25, 23, 40, 21]
    }

serie_idade = pd.Series(dados['Idade'], index = dados['Nome'])
print('A série de dados é:')
print(serie_idade)

print('-'*10, 'Cálculo', '-'*10)
print(f'A idade média dos clientes é de {serie_idade.mean()} anos')
print(f'O cliente mais velho tem {serie_idade.max()}.')
print(f'O cliente mais novo tem {serie_idade.min()}.')
