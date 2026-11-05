import pandas as pd

url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
dfs = pd.read_html(url)

#Imprimindo o tipo e a quantidade de tabelas no site.
print(type(dfs))
print(len(dfs))

#Imprimindo o cabeçalho das colunas das tabelas.
df_bancos = dfs[0]
print(df_bancos.shape)
print(df_bancos.dtypes)
print(df_bancos.head())
