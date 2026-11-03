# ------------------------------------------------------------
# VARIÁVEIS GLOBAIS
# Guardam o "estado" do programa, ou seja, os dados que precisam
# continuar existindo enquanto o usuário navega pelo menu.
# ------------------------------------------------------------
notas = []            # lista que guarda todas as notas cadastradas
soma_notas = 0        # soma de todas as notas da lista
qtd_notas = 0         # quantidade de notas da lista
media_notas = None    # média das notas; None significa "ainda não foi calculada"
situaçao = None       # "Aprovado" ou "Reprovado"; None significa "ainda não foi calculada"


# ------------------------------------------------------------
# FUNÇÃO 1: calculo_media
# Recebe a soma das notas e a quantidade de notas.
# Devolve (return) a média, que é soma / quantidade.
# Obs.: se qtd_notas for 0 acontece divisão por zero, por isso
# a opção 2 do menu só chama esta função se houver notas.
# ------------------------------------------------------------
def calculo_media(notas_somadas, qtd_notas):

    media = notas_somadas / qtd_notas   # divisão da soma pela quantidade
    return media                        # devolve o resultado para quem chamou a função


# ------------------------------------------------------------
# FUNÇÃO 2: situaçao_notas
# Recebe a média e devolve a situação do aluno.
# Regra: média maior ou igual a 7 é Aprovado, senão Reprovado.
# ------------------------------------------------------------
def situaçao_notas(media_notas):
    if media_notas >= 7:        # a média atingiu o mínimo para aprovação?
        return "Aprovado"       # sim: devolve "Aprovado"
    else:
        return "Reprovado"      # não: devolve "Reprovado"


# ------------------------------------------------------------
# LOOP PRINCIPAL
# "while True" cria um laço infinito: o menu aparece de novo
# depois de cada ação, até o usuário escolher a opção 5, que
# usa "break" para sair do laço e encerrar o programa.
# ------------------------------------------------------------
while True:
    # Cabeçalho do menu.
    # "-"*30 repete o traço 30 vezes, formando uma linha.
    # "{:^30}".format(...) centraliza o texto em um espaço de 30 caracteres.
    print("-"*30)
    print("{:^30}".format('Cadastro de notas'))
    print("-"*30)

    # Opções que o usuário pode escolher.
    print("1. Cadastrar notas.")
    print("2. Calcular média.")
    print("3. Ver situação.")
    print("4. Relatório final.")
    print("5. Sair do programa.")

    # input() sempre devolve texto (string); int() converte para número inteiro,
    # para podermos comparar com 1, 2, 3, 4 e 5 logo abaixo.
    opçao = int(input("Escolha: "))

    # --------------------------------------------------------
    # OPÇÃO 1: CADASTRAR NOTAS
    # O usuário digita várias notas seguidas. O menu só volta
    # quando ele digitar "s".
    # --------------------------------------------------------
    if opçao == 1:
        # Laço interno: repete o pedido de nota até aparecer um "break".
        # Por isso o menu não é mostrado a cada nota cadastrada.
        while True:
            # Lemos como texto (sem converter ainda), porque o usuário
            # pode digitar "s" em vez de um número.
            valor = input("Insira a sua nota (ou 's' para voltar ao menu): ")

            # .lower() transforma em minúscula, então "S" e "s" funcionam.
            if valor.lower() == "s":
                break   # sai só do laço interno e volta ao menu

            # Se chegou aqui, o usuário digitou uma nota: converte o texto para
            # número com casas decimais (float), pois notas podem ser 7.5, 8.25...
            nota = float(valor)

            # Validação: nota negativa não faz sentido.
            # "continue" pula o resto desta repetição e volta a pedir a nota,
            # sem guardar o valor inválido na lista.
            if nota < 0:
                print("Número inválido.")
                continue

            # Chegando aqui, a nota é válida: adiciona no final da lista.
            notas.append(nota)

            # Atualiza a soma e a quantidade a cada nota nova, para que a
            # opção 2 sempre trabalhe com os valores mais recentes.
            soma_notas = sum(notas)   # sum() soma todos os itens da lista
            qtd_notas = len(notas)    # len() conta quantos itens a lista tem

    # --------------------------------------------------------
    # OPÇÃO 2: CALCULAR MÉDIA
    # Chama a função calculo_media e mostra o resultado.
    # --------------------------------------------------------
    elif opçao == 2:
        # Se a lista estiver vazia, não dá para calcular a média
        # (seria uma divisão por zero). Avisa e volta ao menu.
        if not notas:
            print('Cadastre as notas primeiro.')
        else:
            # Chama a função passando a soma e a quantidade,
            # e guarda o resultado em media_notas.
            media_notas = calculo_media(soma_notas, qtd_notas)

            # :.2f formata o número com 2 casas decimais (ex.: 7.50).
            print(f"A média das notas é: {media_notas:.2f}.")

    # --------------------------------------------------------
    # OPÇÃO 3: VER SITUAÇÃO
    # A situação depende da média. Então, antes de chamar a
    # função, verificamos se a média já foi calculada.
    # --------------------------------------------------------
    elif opçao == 3:
        # "is None" testa se a variável ainda não recebeu nenhuma média.
        if media_notas is None:
            print("Calcule a média das notas primeiro.")
        else:
            # Chama a função, guarda o resultado em situaçao
            # (a opção 4 vai reutilizar esse valor) e mostra na tela.
            situaçao = situaçao_notas(media_notas)
            print(situaçao)

    # --------------------------------------------------------
    # OPÇÃO 4: RELATÓRIO FINAL
    # Junta tudo: notas, média e situação.
    # --------------------------------------------------------
    elif opçao == 4:
        # Primeira parte: mostra as notas, se existirem.
        if not notas:                   # "not notas" é verdadeiro quando a lista está vazia
            print("Nenhuma nota cadastrada.")
        else:
            print(f"As notas foram: {notas}.")

        # Segunda parte: mostra a média e a situação, se a média já foi calculada.
        if media_notas is None:
            print("Calcule a média das notas primeiro.")
        else:
            print(f"A média foi: {media_notas:.2f}.")
            print(f"A situação: {situaçao}.")

    # --------------------------------------------------------
    # OPÇÃO 5: SAIR
    # --------------------------------------------------------
    elif opçao == 5:
        print("Encerrando o programa.")
        break   # sai do while principal, e como não há mais código, o programa termina

    # --------------------------------------------------------
    # QUALQUER OUTRO NÚMERO
    # O "else" pega tudo que não foi 1, 2, 3, 4 ou 5
    # (por exemplo, 0, 7 ou -3) e avisa o usuário.
    # --------------------------------------------------------
    else:
        print("Número inválido.")
