#Cálculo de desconto
def calcular_desconto(valor, percentual):
    if percentual < 0 or percentual > 100:
        return None

    desconto = valor * (percentual / 100)
    return valor - desconto

#Registro de vendas. É bom para comprovar o funcionamento do desconto.
def registro_vendas(produto, valor):
    print(f"O item {produto}, custa {valor:.2f}.\n")

#Fiz quase igual a loja PVD, só não usei lambda. Que seria aqui, se eu usasse.

print("-"*30)
print('{:^30}'.format('Calculadora de descontos'))
print("-"*30)

total_vendas = 0
qtd_vendas = 0

while True:

    print("1. Registro de produto.")
    print("2. Valor final da compra.")
    print("3. Sair do programa.")
    opçao = int(input("Escolha: "))

    if opçao == 3:
        print("Saindo...")
        break
    

    elif opçao == 1:
            produto = input("Qual o nome do produto? ")
            valor = float(input("Qual o valor do produto? R$"))
            desconto = float(input("Qual a (%) de desconto? "))

            valor_final = calcular_desconto(valor, desconto)

            if valor_final == None:
                 print("Desconto inválido.")
            else: 
                valor_final = calcular_desconto(valor, desconto)
                registro_vendas(produto, valor_final)
                total_vendas += valor_final
                qtd_vendas += 1

    elif opçao == 2:
        print(f"Foram comprados {qtd_vendas} itens e o valor final da compra foi de R${total_vendas:.2f}.")

    else:
        print("Valor inválido.")

