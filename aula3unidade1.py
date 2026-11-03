filmes = [1, 2, 3, 4, 5]
cont = 0
soma = 0
print(f"Digite uma nota (de 1 a 5) para cada filme. Ou digite 0 para sair do programa.\n")

for filme in filmes:
    nota = int(input(f"Digite uma nota para o filme {filme}: "))

    if nota == 0:
        print("O programa foi encerrado.\n")
        break
    elif nota < 1 or nota > 5:
        print("Nota inválida.\n")
        continue
    else:
        print(f"Você classificou o filme {filme} com {nota} estrelas.\n")

    cont += 1
    soma += nota

media = soma / cont

print("Ao final a média das estrelas para os filmes foi de {:.2f}".format(media))
