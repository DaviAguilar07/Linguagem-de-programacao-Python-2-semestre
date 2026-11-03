#Inserção das variáveis que serão utilizadas no programa
notas= []
soma_notas = 0
qtd_notas = 0
media_notas = None
situaçao = None

#Primeira função, ela será utilizada para calcular a media das notas inseridas pelo usuário
def calculo_media(notas_somadas, qtd_notas):

    media = notas_somadas / qtd_notas
    return media

#Segunda função, será utilizada para determinar a situação do aluno, de acordo com sua média.
def situaçao_notas(media_notas):
    if media_notas >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

while True:
    #Aqui é realizado um menu para o usuário interagir com o que tiver interesse.
    print("-"*30)
    print("{:^30}".format('Cadastro de notas'))
    print("-"*30)

    print("1. Cadastrar notas.")
    print("2. Calcular média.")
    print("3. Ver situação.")
    print("4. Relatório final.")
    print("5. Sair do programa.")
    opçao = int(input("Escolha: "))

#Caso o usuário escolha a opção 1, ele terá que fazer a inserção das notas. Após a inserção o programa seguirá para o processamento.
#O processamento será feito para somar todas as notas inseridas e contar quantas notas foram inseridas.
    if opçao == 1:
        nota = float(input("Insira a sua nota: "))
        #Caso a nota seja menor que zero, o programa avisrá ao usuário sobre o número inválido e irá pular essa iteração.
        #Pois, ao pular a iteração o programa não irá atribuir a lista (notas) e não vai fazer nenhum tipo de processamento desse dado irregular.
        if nota < 0:
            print("Número inválido.")
            continue
        notas.append(nota)
        soma_notas = sum(notas) #Soma todas as notas inseridas
        qtd_notas = len(notas) #Conta todas as notas inseridas

#A opção 2 faz o chamado á função de cálculo de média. Depois da função fazer o processamento, o programa imprime a média das notas.
    elif opçao == 2:
        media_notas = calculo_media(soma_notas, qtd_notas)
        print(f"A média das notas é: {media_notas:.2f}.")

#A opção 3 faz o chamado á função de exibição da situação do aluno. Antes ela analisa (atrvés de estrutura condicional) se a média das notas foi calculada.
#Pois, a situação só pode ser calculada se houver a média das notas.
    elif opçao == 3:
        if media_notas is None:
            print("Calcule a média das notas primeiro.")
        else:
            situaçao = situaçao_notas(media_notas)
            print(situaçao)

#A opção 4 analisa primeiramente se há notas cadastradas, se não houver ele avisará ao aluno. Caso as notas foram cadastradas, elas serão impressas.
#Após a impressão das notas, o programa analisa se a média das notas está calculada no programa. Caso não ele pedirá para calcular.
#Caso a média tenha sido calculada, seguirá o programa. O programa exibirá a média das notas e a situação.(Pois a situação depnde da média das notas)
    elif opçao == 4:
        if not notas:
            print("Nenhuma nota cadastrada.")
        else:
            print(f"As notas foram: {notas}.")
        if media_notas is None:
            print("Calcule a média das notas primeiro.")
        else: 
            print(f"A média foi: {media_notas:.2f}.")
            print(f"A situação: {situaçao}.")

#Caso o usuário escolha a opção 5, o programa será encerrado.
    elif opçao == 5:
        print("Encerrando o programa.")
        break

#Caso o usuário insira um número que não esteja dentre as opções do menu, ele será avisado sobre o número inválido.
    else:
        print("Número inválido.")
   
