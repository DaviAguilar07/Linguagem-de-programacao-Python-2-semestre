# Descobrindo os gastos dos clientes 
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='whitegrid') # Vai fixar a cor para todo gráfico

df = sns.load_dataset('tips') # É uma função utilizada para demonstrar as funcionalidades do seaborn, manipulando a contagem de gorjetas.
plt.figure(figsize=(8, 5)) # Tamanho da figura

sns.barplot(x = 'time', y = 'total_bill', data = df, estimator = sum, ci = None, palette = 'Set2')

plt.xlabel('Período (Time)')
plt.ylabel('Total de Gastos')
plt.title('Total de Gastos por Período (Almoço ou Jantar)')

plt.show()
#------------------------------------------------------------------------------------------------------------------------------------------
#Descobrindo quantos clientes almoçaram/jantaram
plt.figure(figsize=(8, 5))

sns.barplot(x='time', y='total_bill', data=df)#, #estimator=sum, ci=None, palette=“Set2”)

plt.xlabel('Período (Time)')
plt.ylabel('Média de Gastos')
plt.title('Média de Gastos por Período (Almoço ou Jantar)')

plt.show()
#------------------------------------------------------------------------------------------------------------------------------------------
#Descobrindo a media de gorjeta por minuto
plt.figure(figsize=(8, 5))

sns.barplot(x='time', y='tip', data=df, palette='Set3')

plt.xlabel('Período (Time)')
plt.ylabel('Média da Gorjeta')
plt.title('Média da Gorjeta por Período (Almoço ou Jantar)')

plt.show()
