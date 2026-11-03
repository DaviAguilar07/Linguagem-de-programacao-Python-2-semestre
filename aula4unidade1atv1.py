def par(numero):
    if numero % 2 == 0:
        return True
    else: 
        return False


num = int(input("Insira um número para saber se é par ou ímpar: "))

mostrando_par = par(num)

if mostrando_par == True:
    print(f"O número {num} é par.\n")
else: 
    print(f"O número {num} é ímpar.\n")
    
