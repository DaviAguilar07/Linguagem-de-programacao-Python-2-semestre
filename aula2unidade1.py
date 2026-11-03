idade = int(input("Qual a sua idade? "))

if idade < 12:
    print("A recomendação é: Toy Story\n")
elif idade >= 12 and idade < 18:
    print("A recomendação é: Guardiões da galáxia\n")
else: 
    print("A recomendação é: No limite do amanhã\n")

ingressos_existentes = 15
valoringresso = 20

ingressos_solicitados = int(input("Quantos ingressos você irá comprar (20 reais cada ingresso)? "))

valortotal = ingressos_solicitados * valoringresso

if ingressos_existentes >= ingressos_solicitados:
    print("Compra efetuada com sucesso. Valor: R${}\n".format(valortotal))
elif ingressos_existentes < ingressos_solicitados:
    print("Quantidade de ingressos indisponível.\n") 
   