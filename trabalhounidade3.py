import sqlite3

conexao = sqlite3.connect('dados_vendas.db')
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS vendas1(
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT, 
    data_venda DATE, 
    produto TEXT, 
    categoria TEXT, 
    valor_venda REAL
)
""")

cursor.execute("""INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
    ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00), 
    ('2023-01-05', 'Produto B', 'Roupas', 350.00), 
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00), 
    ('2023-03-15', 'Produto D', 'Livros', 200.00), 
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00), 
    ('2023-04-02', 'Produto F', 'Roupas', 400.00), 
    ('2023-05-05', 'Produto G', 'Livros', 150.00), 
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00), 
    ('2023-07-20', 'Produto I', 'Roupas', 600.00), 
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00), 
    ('2023-09-30', 'Produto K', 'Livros', 300.00), 
    ('2023-10-05', 'Produto L', 'Roupas', 450.00), 
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00), 
    ('2023-12-20', 'Produto N', 'Livros', 250.00);
""")
conexao.commit()

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)# Lendo os dados
print(df_vendas.head())

#Criando um gráfico de média de valor_venda por categoria------------------------------------------

sns.set_style("whitegrid")# Definindo estilo
plt.figure(figsize=(10, 7))# Criando figura


# Criando a média de valor_venda por categoria
sns.barplot(x='categoria', y='valor_venda', data=df_vendas, palette='Set2')

# Personalizando rótulos
plt.xlabel('Categoria')
plt.ylabel('Valor médio de vendas')
plt.title('Valor médio de vendas por categoria')
plt.show()


#Criando um gráfico que exibe o valor máximo vendido durante o ano, entre essas categorias----------------------------------------------
sns.set_style('whitegrid')


df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda']) # Garantindo que data_venda seja datetime

df_total = df_vendas.groupby('data_venda', as_index=False)['valor_venda'].sum() # Agrupando por data para somar as vendas

plt.figure(figsize = (10, 7))

sns.lineplot(x='data_venda', y='valor_venda', data = df_vendas, marker = 'o')
plt.xlabel('Data de venda')
plt.ylabel('Total de venda')
plt.title('Valor total vendido por data')
plt.show()


#Criando um gráfico que demonstra quais são as principais categorias de venda (quantidade)
sns.set_style('whitegrid')
plt.figure(figsize=(10, 7))


sns.countplot(x='categoria', data=df_vendas, palette='Set2')# Gráfico de quantidade de vendas por categoria

plt.xlabel('\nCategoria')
plt.ylabel('Quantidade de vendas')
plt.title('Quantidade total de vendas por categoria')
plt.show()

