lista = [35, 80, 100, 115, 210, 220]
print(f'O valor em dolar é: {lista}')

valor_em_dolar = 5.25

valor_em_real = list(map(lambda x: x * valor_em_dolar, lista))

print(f'O valor em real é: {valor_em_real}')

