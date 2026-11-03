notas = [8.5, 6.4, 7.0, 7.8, 6.0]

def calcular_media(notas): #Faz o processo de cálculo da média.
    soma = sum(notas)
    cont = len(notas)
    media = soma / cont
    return media

arredondar_media = lambda media: round(media, 2) #Usa o lambda para arredondar a média.

media = calcular_media(notas) #Designa um número.
media_arredondada = arredondar_media(media) #Designa um número.

def situacao(numarredondado): #Faz o processamento da situação do aluno.
    if numarredondado >= 7:
        return "Aprovado"
    elif numarredondado >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

resultado_situacao = situacao(media_arredondada) #Designa um número.

print(f"As notas foram: {notas}.\n")
print(f"A média das notas foi: {media_arredondada}.\n")
print(f"A situação é: {resultado_situacao}.\n")
