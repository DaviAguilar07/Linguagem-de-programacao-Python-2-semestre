import pandas as pd
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(type(df))
print(len(df))

#Calculando a média dos passageiros
print(f'A média de idade das vitima era de {df["Age"].mean():.2f} anos')

#Calculando a idade da pessoa mais velha e o nome (idade = valor, nome = indice)
idx_max = df['Age'].idxmax()
print(f'A vitima mais velha tinha {df['Age'].max()} anos e se chamava {df.loc[idx_max, 'Name']}.')

#Calculando a idade e nome da pessoa mais nova e o nome (idade = valor, nome = indice)
idx_min = df['Age'].idxmin()
print(f'A vitima mais nova tinha {df["Age"].min()} anos e se chamava {df.loc[idx_min, 'Name']}.')
