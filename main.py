import os

import game

if __name__ == "__main__":
    tabuleiro = [" "] * 9
    
    # Variável para controlar o turno.
    # True é turno do jogador
    # False é turno da máquina
    turno = True

    # Quando sair desse loop, ou há vencedor, ou há empate
    while game.verificar_vencedor(tabuleiro) == 0:
        os.system('clear')
        game.print_tabuleiro(tabuleiro)

        if turno == True:
            temp = 0
            while temp == 0:
                casa = game.receber_input_da_casa()
                # Decrementa 1 na casa pois o array é de 0 ~ 8 :)
                casa -= 1
                aux = game.jogador_fazendo_jogada(tabuleiro, casa)
                # Se aux for number, a casa estava ocupada e é atribuido o 0 a temp novamente 
                # Se aux não for number, a casa estava livre, e aux está armazenando o valor do tabuleiro
                if type(aux) == int:
                    temp = aux
                else:
                    tabuleiro = aux
                    temp = 1
        else:
            tabuleiro = game.pc_fazendo_jogada(tabuleiro)

        turno = not turno

    game.printar_vencedor(tabuleiro)
