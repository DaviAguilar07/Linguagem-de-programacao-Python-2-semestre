import matplotlib.pyplot as plt

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril',
         'Maio', 'Junho', 'Julho', 'Agosto',
         'Setembro', 'Outubro', 'Novembro', 'Dezembro']

vendas = []

for c in range(1, 13):
    vendas.append(int(input(f'Quantas vendas vocês realizarm no {c}° mês do ano? ')))

plt.bar(meses, vendas, color='royalblue')

plt.xlabel('Mês')
plt.ylabel('Vendas (em unidades)')
plt.title('Quadro de Registros')

plt.xticks(rotation=45)  # Rotaciona os meses para melhor visualização
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Linhas horizontais

plt.tight_layout()       # Ajusta o layout para não cortar textos

plt.show()
