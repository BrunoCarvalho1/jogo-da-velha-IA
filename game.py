import random
import os

# Retorna 1 se o X ganhar.
# Retorna -1 se o O ganhar.
# Retorna 0 se não houver vencedores
def verificar_linha(tabuleiro):
    # Linha 1
    if tabuleiro[0] == "X" and tabuleiro[1] == "X" and tabuleiro[2] == "X":
        return 1

    # Linha 2
    if tabuleiro[3] == "X" and tabuleiro[4] == "X" and tabuleiro[5] == "X":
        return 1

    # Linha 3
    if tabuleiro[6] == "X" and tabuleiro[7] == "X" and tabuleiro[8] == "X":
        return 1

    # Linha 1
    if tabuleiro[0] == "O" and tabuleiro[1] == "O" and tabuleiro[2] == "O":
        return -1

    # Linha 2
    if tabuleiro[3] == "O" and tabuleiro[4] == "O" and tabuleiro[5] == "O":
        return -1

    # Linha 3
    if tabuleiro[6] == "O" and tabuleiro[7] == "O" and tabuleiro[8] == "O":
        return -1

    return 0


# Retorna 1 se o X ganhar.
# Retorna -1 se o O ganhar.
# Retorna 0 se não houver vencedores
def verificar_coluna(tabuleiro):
    # Coluna 1
    if tabuleiro[0] == "X" and tabuleiro[3] == "X" and tabuleiro[6] == "X":
        return 1

    # Coluna 2
    if tabuleiro[1] == "X" and tabuleiro[4] == "X" and tabuleiro[7] == "X":
        return 1

    # Coluna 3
    if tabuleiro[2] == "X" and tabuleiro[5] == "X" and tabuleiro[6] == "X":
        return 1

    # Coluna 1
    if tabuleiro[0] == "O" and tabuleiro[3] == "O" and tabuleiro[6] == "O":
        return -1

    # Coluna 2
    if tabuleiro[1] == "O" and tabuleiro[4] == "O" and tabuleiro[7] == "O":
        return -1

    # Coluna 3
    if tabuleiro[2] == "O" and tabuleiro[5] == "O" and tabuleiro[6] == "O":
        return -1

    return 0

# Retorna 1 se o X ganhar.
# Retorna -1 se o O ganhar.
# Retorna 0 se não houver vencedores
def verificar_diagonal(tabuleiro):
    # Diagonal principal
    if tabuleiro[0] == "X" and tabuleiro[4] == "X" and tabuleiro[8] == "X":
        return 1

    # Diagonal secundária
    if tabuleiro[2] == "X" and tabuleiro[4] == "X" and tabuleiro[6] == "X":
        return 1

    # Diagonal principal
    if tabuleiro[0] == "O" and tabuleiro[4] == "O" and tabuleiro[8] == "O":
        return -1

    # Diagonal secundária
    if tabuleiro[2] == "O" and tabuleiro[4] == "O" and tabuleiro[6] == "O":
        return -1

    return 0


# Retorna 1 se o X ganhar.
# Retorna -1 se o O ganhar.
# Retorna 0 se não houver vencedores
# Retorna 2 se houver empate
def verificar_vencedor(tabuleiro):
    if verificar_linha(tabuleiro) != 0:
        return verificar_linha(tabuleiro)

    if verificar_coluna(tabuleiro) != 0:
        return verificar_coluna(tabuleiro)

    if verificar_diagonal(tabuleiro) != 0:
        return verificar_diagonal(tabuleiro)

    # Verifica empate
    temp = 0
    for i in range(9):
        if tabuleiro[i] != " ":
            temp += 1
        
        if temp == 9:
            return 2

    return 0


# Imprime o tabuleiro
def print_tabuleiro(tabuleiro):
    for i in range(9):
        if i == 3 or i == 6:
            print()

        print("", tabuleiro[i], "", end="", sep="|")

    print()


# Retorna True se a casa estiver ocupada
def verificar_casa(tabuleiro, casa):
    if tabuleiro[casa] != " ":
        return True


# Faz uma jogada aleatória
def jogada_aleatoria(tabuleiro):
    temp = random.randint(0, 8)
    while verificar_casa(tabuleiro, temp) == True:
        temp = random.randint(0, 8)

    tabuleiro[temp] = "O"

    return tabuleiro


# Permite o PC fazer uma jogada
def pc_fazendo_jogada(tabuleiro):
    tabuleiro = jogada_aleatoria(tabuleiro)

    return tabuleiro


# Retorna 0 se a casa estiver ocupada
# Retorna o tabuleiro se a jogada foi feita com sucesso
def jogador_fazendo_jogada(tabuleiro, casa):
    if verificar_casa(tabuleiro, casa):
        print('Casa já ocupada')
        return 0

    tabuleiro[casa] = "X"

    return tabuleiro


def receber_input_da_casa():
    casa = 0
    aux = -1
    while aux == -1:
        casa = int(input('Digite uma casa de 1 a 9: '))
        if casa < 1 or casa > 9:
            print('Casa inválida')
            continue

        aux = 0

    return casa


def printar_vencedor(tabuleiro):
    if verificar_vencedor(tabuleiro) == 1:
        os.system('clear')
        print_tabuleiro(tabuleiro)
        print('Jogador venceu!')

    if verificar_vencedor(tabuleiro) == -1:
        os.system('clear')
        print_tabuleiro(tabuleiro)
        print('Máquina venceu!')

    if verificar_vencedor(tabuleiro) == 2:
        os.system('clear')
        print_tabuleiro(tabuleiro)
        print('Empate')
