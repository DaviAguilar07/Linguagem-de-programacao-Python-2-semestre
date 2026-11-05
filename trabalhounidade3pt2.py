# Importando as bibliotecas necessárias
import sqlite3              # Biblioteca para trabalhar com banco de dados SQLite
import seaborn as sns       # Biblioteca para visualização de dados (gráficos estatísticos)
import pandas as pd         # Biblioteca para manipulação e análise de dados em DataFrames
import matplotlib.pyplot as plt  # Biblioteca para criação de gráficos

# Conectando ao banco de dados SQLite (se não existir, será criado automaticamente)
conexao = sqlite3.connect('dados_vendas.db')
cursor = conexao.cursor()   # Criando um cursor para executar comandos SQL

# Criando a tabela 'vendas1' caso ela não exista
cursor.execute("""CREATE TABLE IF NOT EXISTS vendas1(
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,  -- Chave primária, gerada automaticamente
    data_venda DATE,                             -- Data da venda
    produto TEXT,                                -- Nome do produto vendido
    categoria TEXT,                              -- Categoria do produto (ex: Eletrônicos, Roupas, Livros)
    valor_venda REAL                             -- Valor da venda
)
""")

# Inserindo registros de vendas fictícios na tabela
# Obs: se rodar o código várias vezes, os dados serão duplicados (poderia usar DELETE antes para limpar)
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
conexao.commit()  # Confirmando as alterações no banco

#---------------------------------------------------------------------------------------------------------------------

# Lendo os dados da tabela 'vendas1' diretamente para um DataFrame do Pandas
df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)
print(df_vendas.head())  # Exibindo as primeiras linhas para conferência

# ========================= GRÁFICO 1 =========================
# Média de valor de vendas por categoria

sns.set_style("whitegrid")        # Definindo estilo visual dos gráficos
plt.figure(figsize=(10, 7))       # Definindo tamanho da figura

# Criando gráfico de barras com a média de vendas por categoria
sns.barplot(x='categoria', y='valor_venda', data=df_vendas, palette='Set2')

# Personalizando rótulos e título
plt.xlabel('Categoria')
plt.ylabel('Valor médio de vendas')
plt.title('Valor médio de vendas por categoria')
plt.show()

# ========================= GRÁFICO 2 =========================
# Valor total vendido ao longo do ano (por data)

sns.set_style('whitegrid')

# Convertendo a coluna 'data_venda' para o tipo datetime (necessário para gráficos temporais)
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])

# Agrupando os valores por data (somando vendas realizadas no mesmo dia)
df_total = df_vendas.groupby('data_venda', as_index=False)['valor_venda'].sum()

plt.figure(figsize=(10, 7))

# Criando gráfico de linha para mostrar evolução das vendas
sns.lineplot(x='data_venda', y='valor_venda', data=df_total, marker='o')
plt.xlabel('Data de venda')
plt.ylabel('Total de venda')
plt.title('Valor total vendido por data')
plt.show()

# ========================= GRÁFICO 3 =========================
# Quantidade de vendas por categoria

sns.set_style('whitegrid')
plt.figure(figsize=(10, 7))

# Criando gráfico de contagem (quantidade de registros por categoria)
sns.countplot(x='categoria', data=df_vendas, palette='Set2')

plt.xlabel('\nCategoria')
plt.ylabel('Quantidade de vendas')
plt.title('Quantidade total de vendas por categoria')
plt.show()

# ========================= ANÁLISE DOS DADOS =========================

# Calculando estatísticas gerais
total_vendas = df_vendas['valor_venda'].sum()     # Soma de todas as vendas
media_vendas = df_vendas['valor_venda'].mean()    # Média dos valores de venda
maior_venda = df_vendas['valor_venda'].max()      # Maior valor de venda registrado
menor_venda = df_vendas['valor_venda'].min()      # Menor valor de venda registrado

print('-----Analisando os dados-----')
print(f"\nTotal de vendas: R$ {total_vendas:.2f}")
print(f"Média das vendas: R$ {media_vendas:.2f}")
print(f"Maior venda: R$ {maior_venda:.2f}")
print(f"Menor venda: R$ {menor_venda:.2f}")


# ========================= ANÁLISE DOS GRÁFICOS =========================
print('\n========== ANÁLISE DOS GRÁFICOS ==========')

# ------------------ Gráfico 1 - Valor médio de vendas por categoria ------------------
# Aqui calculamos a média de vendas por categoria usando o método groupby do Pandas.
media_por_categoria = df_vendas.groupby('categoria')['valor_venda'].mean()

# Identificamos qual categoria tem a maior média de vendas
categoria_maior_media = media_por_categoria.idxmax()  # Retorna o nome da categoria com maior média
maior_media = media_por_categoria.max()               # Retorna o valor da maior média

# Identificamos qual categoria tem a menor média de vendas
categoria_menor_media = media_por_categoria.idxmin()  # Retorna o nome da categoria com menor média
menor_media = media_por_categoria.min()               # Retorna o valor da menor média

# Exibindo os resultados da análise do gráfico 1
print('\nGráfico 1 - Valor médio de vendas por categoria:')
print(f'A categoria {categoria_maior_media} apresentou a maior média de vendas, '
      f'com aproximadamente R$ {maior_media:.2f} por venda.')
print(f'A categoria {categoria_menor_media} apresentou a menor média de vendas, '
      f'com aproximadamente R$ {menor_media:.2f} por venda.')

# ------------------ Gráfico 2 - Valor total vendido por data ------------------
# Aqui analisamos o DataFrame df_total, que contém a soma das vendas agrupadas por data.
# Usamos idxmax() para encontrar a linha onde ocorreu a maior venda.
data_maior_venda = df_total.loc[df_total['valor_venda'].idxmax(), 'data_venda']
maior_venda_data = df_total['valor_venda'].max()  # Valor da maior venda registrada

# Exibindo os resultados da análise do gráfico 2
print('\nGráfico 2 - Valor total vendido por data:')
print(f'A maior venda registrada ocorreu em {data_maior_venda.strftime("%d/%m/%Y")}, '
      f'com o valor de R$ {maior_venda_data:.2f}.')
print('O gráfico de linha permite observar a variação dos valores das vendas '
      'ao longo do período analisado.')

# ------------------ Gráfico 3 - Quantidade de vendas por categoria ------------------
# Aqui usamos value_counts() para contar quantas vezes cada categoria aparece no DataFrame.
quantidade_por_categoria = df_vendas['categoria'].value_counts()

# Identificamos a categoria mais vendida e sua quantidade
categoria_mais_vendida = quantidade_por_categoria.idxmax()  # Categoria com maior quantidade de vendas
quantidade_mais_vendida = quantidade_por_categoria.max()    # Número de vendas dessa categoria

# Exibindo os resultados da análise do gráfico 3
print('\nGráfico 3 - Quantidade de vendas por categoria:')
print(f'A categoria {categoria_mais_vendida} apresentou a maior quantidade '
      f'de vendas, com {quantidade_mais_vendida} vendas registradas.')
print('Esse gráfico permite identificar quais categorias possuem maior '
      'frequência de vendas.')

# ========================= CONCLUSÃO GERAL =========================
# Aqui fazemos um resumo final da análise, explicando o que cada gráfico mostrou
# e como essas informações podem ser úteis para a empresa.
print('\n========== CONCLUSÃO DA ANÁLISE ==========')
print('Os três gráficos permitem analisar diferentes aspectos do desempenho das vendas.')
print('O primeiro gráfico mostra o valor médio das vendas por categoria, '
      'o segundo apresenta a variação dos valores vendidos ao longo das datas '
      'e o terceiro mostra a quantidade de vendas realizadas por categoria.')
# Sugestão breve para a empresa
print('\n========== SUGESTÃO PARA A EMPRESA ==========')
print('A empresa deve priorizar investimentos em Eletrônicos, '
      'fortalecer promoções em Roupas para aumentar o ticket médio '
      'e repensar estratégias para Livros, que tiveram menor desempenho.')
# Encerrando a conexão com o banco de dados para liberar recursos
conexao.close()
