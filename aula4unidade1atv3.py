#Processamento do número primo:
def primo(a):
    tot = 0
    if a > 1:
        for i in range(1, a + 1):
            if a % i == 0:
                tot += 1 #O contador garante a verificação do número primo.
        if tot == 2:
            return True
        else:
            return False
    else:
        return False

#Recolhendo o número desejado pelo usuário:
num = int(input("Digite um número: "))

resultado = primo(num)

#Exibindo ao usuário se é ou não um número primo:
if resultado:
    print(f"O {num} é primo.\n")
else:
    print(f"O {num} não é primo.\n")
