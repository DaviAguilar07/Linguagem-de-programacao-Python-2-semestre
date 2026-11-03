
nota1 = float(input("Digite a sua 1° nota: "))
nota2 = float(input("Digite a sua 2° nota: "))
nota3 = float(input("Digite a sua 3° nota: "))
nota4 = float(input("Digite a sua 4° nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

# Forma automatizada:

# soma = 0
# for i in range (1,5):
#         nota = float(input("Digite a sua {}° nota: ".format(i)))

#         soma += nota

# media = soma / 4

if media >= 6:
        situaçao = 'Aprovado'
else:
        situaçao = 'Reprovado'

print("A média de suas notas é ", media)
print(f"{situaçao}")
