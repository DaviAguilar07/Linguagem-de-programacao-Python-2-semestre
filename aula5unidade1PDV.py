#Processamento do desconto
def calcular_desconto(valor, percentual):
    if percentual < 0 or percentual > 100:
        return None
    
    desconto = valor * (percentual / 100)
    return valor - desconto

#Processamento do registro de vendas
def registro_vendas(produto, valor_final):
    print(f"O item: {produto}, custa: R${valor_final}.")

#Arredondamento
arredondar = lambda v: round(v,2)

#Começa a impressão ao usuário:
print("-"*30)
print('{:^30}'.format('Comércio - BH'))
print("-"*30)

total_vendas = 0
qtd_vendas = 0

while True:
    print("1. Registrar produto.")
    print("2. Gerar relatório da compra.")
    print("3. Sair do programa.")
    opçao = int(input("Escolha uma opção: "))

    if opçao == 3:
        print("Saindo...")
        break

    elif opçao == 1:
        produto = input("Qual o produto? ")
        valor = float(input("Qual o valor? "))
        percentual = float(input("Qual o desconto? "))

        valor_final = calcular_desconto(valor, percentual) #Valor final é igual ao pós desconto.

        if valor_final == None:
            print(f"Valor inválido. Insira um número de 0 a 100.")
        else:
            valor_final = calcular_desconto(valor, percentual) #Valor final é igual ao pós desconto.
            registro_vendas(produto, valor_final)
            total_vendas += valor_final
            qtd_vendas += 1

    elif opçao == 2:
        print(f"Foram vendidos {qtd_vendas} itens. Valor final: R${arredondar(total_vendas)}.")
    else: 
        print("Opção inválida.")

