import pandas as pd
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(type(df))
print(len(df))

#Calculando os dados
print(f'A média de idade da tripulação era de: {df['Age'].mean():.2f} anos.')

idx_max = df['Age'].idxmax()
print(f'O mais velho tinha {df['Age'].max()} anos e se chamava {df.loc[idx_max, "Name"]}.')

idx_min = df['Age'].idxmin()
print(f'O mais novo tinha {df['Age'].min()} anos e se chamava {df.loc[idx_min, "Name"]}.')
