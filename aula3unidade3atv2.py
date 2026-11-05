import pandas as pd
#Criando os dados em dicionário (chave e valor)
dados = {
    'Nome': ['Pente', 'Torneira', 'Lustre', 'Pente', 'Bola'],
    'Tipo': ['Pessoal', 'Doméstico', 'Doméstico', 'Pessoal', 'Brinquedo'],
    'Quantidade': [4, 2, 1, 4, 2],
    'Valor final': [30, 300, 400, 30, 40]
}

#Transformando em tabela
df = pd.DataFrame(dados)

# Calcular valor unitário
df['Valor unitário'] = df['Valor final'] / df['Quantidade']

# Calcular quais são os produtos que tem o valor unitário acima de 50 reais
acima_50 = df[df['Valor unitário'] > 50]

print('Produtos que custam mais que 50 reais:')
print(acima_50)