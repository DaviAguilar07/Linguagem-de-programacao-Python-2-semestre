import pandas as pd

data = {
    'nome': ['Produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto D'],
    'quantidade de itens comprados': [3, 1, 4, 3, 2],
    'receita total':  [120, 80, 60, 120, 90]
}

#Transformando o dicionário data em um dataframe (df), transformou o dicionário em uma tabela.
df = pd.DataFrame(data)

# Removendo as duplicidades
df.drop_duplicates(keep = 'last', inplace = True)

df['preço do item'] = df['receita total'] / df['quantidade de itens comprados']

itens_acima_de_50 = df[df['preço do item'] > 50]

print('Itens acima de 50 reais: ')
print(itens_acima_de_50)
