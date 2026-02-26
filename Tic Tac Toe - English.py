import random
import time
import os
import platform

continuar = contraAmigo = difFacil = 1
contraComputador = difMedio = 2
maqContraMaq = difDificil = 3
maxJogadas = 9

# VERIFIES IF THE COORDINATES PLACED BY THE USER IS AVAILABLE OR NOT.
def verificarCoordenada(jogadaUser):
    coordenadaValida = None

    for coordenada in jogadaUser:
        if(((coordenada != 'A') and (coordenada != 'B') and (coordenada != 'C') and 
           (coordenada != '1') and (coordenada != '2') and (coordenada != '3')) or (len(jogadaUser) != 2)):
            coordenadaValida = False
            break
        else:
            coordenadaValida = True
     
    return coordenadaValida

# WITH THE COORDINATES, PUTS THE PLAYERS PIECE ON THE BOARD.
#       A       B       C
#   ┌───────┬───────┬───────┐
# 1 │ {[0]} │ {[3]} │ {[6]} │
#   ├───────┼───────┼───────┤
# 2 │ {[1]} │ {[4]} │ {[7]} │
#   ├───────┼───────┼───────┤
# 3 │ {[2]} │ {[5]} │ {[8]} │
#   └───────┴───────┴───────┘
def posicionarJogada(jogadaUser, listaCoordenadas, jogadorMomento):
    if('A' in jogadaUser):
        if('1' in jogadaUser):
            listaCoordenadas[0] = jogadorMomento
        elif('2' in jogadaUser):
            listaCoordenadas[1] = jogadorMomento
        else:
            listaCoordenadas[2] = jogadorMomento
    elif('B' in jogadaUser):
        if('1' in jogadaUser):
            listaCoordenadas[3] = jogadorMomento
        elif('2' in jogadaUser):
            listaCoordenadas[4] = jogadorMomento
        else:
            listaCoordenadas[5] = jogadorMomento
    else:
        if('1' in jogadaUser):
            listaCoordenadas[6] = jogadorMomento
        elif('2' in jogadaUser):
            listaCoordenadas[7] = jogadorMomento
        else:
            listaCoordenadas[8] = jogadorMomento
    
    return listaCoordenadas

# VERIFIES IF THE COORDINATES PLACED BY THE USER WAS ALREADY USED.
def verificarJogada(casaJogador, casasUsadas):
    casaUsada = None

    if(casaJogador in casasUsadas):
        casaUsada = True
    else:
        casaUsada = False
        casasUsadas.append(casaJogador)

    return casaUsada, casasUsadas

# BASED ON THE BOARDS OCCUPIED HOUSES, VERIFIES IF A PLAYER HAS WON OR NOT.
def verificarVitoria(coordenadasUsadas, jogadorX, jogadorO):
    vitoria = True
    vencedor = None
    
    if((coordenadasUsadas[0] == coordenadasUsadas[1] == coordenadasUsadas[2] == jogadorX) or
       (coordenadasUsadas[3] == coordenadasUsadas[4] == coordenadasUsadas[5] == jogadorX) or 
       (coordenadasUsadas[6] == coordenadasUsadas[7] == coordenadasUsadas[8] == jogadorX) or
       (coordenadasUsadas[0] == coordenadasUsadas[3] == coordenadasUsadas[6] == jogadorX) or
       (coordenadasUsadas[1] == coordenadasUsadas[4] == coordenadasUsadas[7] == jogadorX) or
       (coordenadasUsadas[2] == coordenadasUsadas[5] == coordenadasUsadas[8] == jogadorX) or
       (coordenadasUsadas[0] == coordenadasUsadas[4] == coordenadasUsadas[8] == jogadorX) or
       (coordenadasUsadas[6] == coordenadasUsadas[4] == coordenadasUsadas[2] == jogadorX)):
        vencedor = jogadorX
    elif((coordenadasUsadas[0] == coordenadasUsadas[1] == coordenadasUsadas[2] == jogadorO) or
         (coordenadasUsadas[3] == coordenadasUsadas[4] == coordenadasUsadas[5] == jogadorO) or 
       (coordenadasUsadas[6] == coordenadasUsadas[7] == coordenadasUsadas[8] == jogadorO) or
       (coordenadasUsadas[0] == coordenadasUsadas[3] == coordenadasUsadas[6] == jogadorO) or
       (coordenadasUsadas[1] == coordenadasUsadas[4] == coordenadasUsadas[7] == jogadorO) or
       (coordenadasUsadas[2] == coordenadasUsadas[5] == coordenadasUsadas[8] == jogadorO) or
       (coordenadasUsadas[0] == coordenadasUsadas[4] == coordenadasUsadas[8] == jogadorO) or
       (coordenadasUsadas[6] == coordenadasUsadas[4] == coordenadasUsadas[2] == jogadorO)):
        vencedor = jogadorO
    else:
        vitoria = False
    
    return vitoria, vencedor

# FUNCTION THAT WILL DETERMINE THE COMPUTER INTELLIGENCE LEVEL.
def jogadaComputador(casasUsadas, casasDisponiveis, pecaMaquina, pecaAdversario, tabuleiroAtual, nivelDificuldade):
    jogadaContraRealizada = jogadaSimplesRealizada  = vitoriaGarantida = False
    casaVazia = " "
    facil = 1
    medio = 2
    dificil = 3
    movimentoComputador = None
    listaPossiveisJogadasContra = []
    listaPossiveisJogadasVitoria = []
    listaPossiveisJogadasSimples = []
    
    # IN CASE THE COMPUTER STARTS THE GAME, IT WILL CHOOSE A RANDOM HOUSE ON THE BOARD.
    if(len(casasUsadas) == 0):
        movimentoComputador = random.choice(casasDisponiveis)
    else:
        # VERIFIES WHICH HOUSES ARE AVAILABE TO USE ON THE BOARD.
        for casa in casasUsadas:
            for casas in casasDisponiveis:
                if(casa == casas):
                    casasDisponiveis.remove(casa)

        # IN CASE THE COMPUTER'S DIFFICULTY LEVEL IS HARD, IT WILL IDENTIFY 
        # IF THE USER NEEDS AT LEAST 1 HOUSE TO WIN.
        # IF THAT HAPPENS, THE COMPUTER WILL KEEP THE HOUSES THAT CAN MAKE THE USER
        # WIN IN A LIST AND WILL CHOOSE BETWEEN ONE OF THEM TO STOP THE USERS VICTORY.
        if(nivelDificuldade == dificil):
            if(tabuleiroAtual[0] == pecaAdversario):
                if(tabuleiroAtual[1] == pecaAdversario):
                    if(tabuleiroAtual[2] == casaVazia):
                        listaPossiveisJogadasContra.append("A3")
                elif(tabuleiroAtual[2] == pecaAdversario):
                    if(tabuleiroAtual[1] == casaVazia):
                        listaPossiveisJogadasContra.append("A2")
                
                if(tabuleiroAtual[3] == pecaAdversario):
                    if(tabuleiroAtual[6] == casaVazia):
                        listaPossiveisJogadasContra.append("C1")
                elif(tabuleiroAtual[6] == pecaAdversario):
                    if(tabuleiroAtual[3] == casaVazia):
                        listaPossiveisJogadasContra.append("B1")
                
                if(tabuleiroAtual[4] == pecaAdversario):
                    if(tabuleiroAtual[8] == casaVazia):
                        listaPossiveisJogadasContra.append("C3")
                elif(tabuleiroAtual[8] == pecaAdversario):
                    if(tabuleiroAtual[4] == casaVazia):
                        listaPossiveisJogadasContra.append("B2")
            
            if(tabuleiroAtual[1] == pecaAdversario):
                if(tabuleiroAtual[0] == pecaAdversario):
                    if(tabuleiroAtual[2] == casaVazia):
                        # IF THIS HOUSE IS ALREADY IN THE LIST, IT WON'T BE ADDED
                        if("A3" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("A3")
                elif(tabuleiroAtual[2] == pecaAdversario):
                    if(tabuleiroAtual[0] == casaVazia):
                        listaPossiveisJogadasContra.append("A1")
                
                if(tabuleiroAtual[4] == pecaAdversario):
                    if(tabuleiroAtual[7] == casaVazia):
                        listaPossiveisJogadasContra.append("C2")
                elif(tabuleiroAtual[7] == pecaAdversario):
                    if(tabuleiroAtual[4] == casaVazia):
                        if("B2" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("B2")
            
            if(tabuleiroAtual[2] == pecaAdversario):
                if(tabuleiroAtual[0] == pecaAdversario):
                    if(tabuleiroAtual[1] == casaVazia):
                        if("A2" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("A2")
                elif(tabuleiroAtual[1] == pecaAdversario):
                    if(tabuleiroAtual[0] == casaVazia):
                        if("A1" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("A1")
                
                if(tabuleiroAtual[5] == pecaAdversario):
                    if(tabuleiroAtual[8] == casaVazia):
                        if("C3" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("C3")
                elif(tabuleiroAtual[8] == pecaAdversario):
                    if(tabuleiroAtual[5] == casaVazia):
                        listaPossiveisJogadasContra.append("B3")
                
                if(tabuleiroAtual[4] == pecaAdversario):
                    if(tabuleiroAtual[6] == casaVazia):
                        if("C1" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("C1")
                elif(tabuleiroAtual[6] == pecaAdversario):
                    if(tabuleiroAtual[4] == casaVazia):
                        if("B2" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("B2")

            if(tabuleiroAtual[3] == pecaAdversario):
                if(tabuleiroAtual[0] == pecaAdversario):
                    if(tabuleiroAtual[6] == casaVazia):
                        if("C1" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("C1")
                elif(tabuleiroAtual[6] == pecaAdversario):
                    if(tabuleiroAtual[0] == casaVazia):
                        if("A1" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("A1")
                
                if(tabuleiroAtual[4] == pecaAdversario):
                    if(tabuleiroAtual[5] == casaVazia):
                        if("B3" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("B3")
                elif(tabuleiroAtual[5] == pecaAdversario):
                    if(tabuleiroAtual[4] == casaVazia):
                        if("B2" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("B2")
            
            if(tabuleiroAtual[4] == pecaAdversario):
                if(tabuleiroAtual[0] == pecaAdversario):
                    if(tabuleiroAtual[8] == casaVazia):
                        if("C3" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("C3")
                elif(tabuleiroAtual[8] == pecaAdversario):
                    if(tabuleiroAtual[0] == casaVazia):
                        if("A1" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("A1")
                
                if(tabuleiroAtual[1] == pecaAdversario):
                    if(tabuleiroAtual[7] == casaVazia):
                        if("C2" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("C2")
                elif(tabuleiroAtual[7] == pecaAdversario):
                    if(tabuleiroAtual[1] == casaVazia):
                        if("A2" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("A2")
                
                if(tabuleiroAtual[2] == pecaAdversario):
                    if(tabuleiroAtual[6] == casaVazia):
                        if("C1" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("C1")
                elif(tabuleiroAtual[6] == pecaAdversario):
                    if(tabuleiroAtual[2] == casaVazia):
                        if("A3" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("A3")
                
                if(tabuleiroAtual[3] == pecaAdversario):
                    if(tabuleiroAtual[5] == casaVazia):
                        if("B3" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("B3")
                elif(tabuleiroAtual[5] == pecaAdversario):
                    if(tabuleiroAtual[3] == casaVazia):
                        if("B1" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("B1")

            if(tabuleiroAtual[5] == pecaAdversario):
                if(tabuleiroAtual[2] == pecaAdversario):
                    if(tabuleiroAtual[8] == casaVazia):
                        if("C3" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("C3")
                elif(tabuleiroAtual[8] == pecaAdversario):
                    if(tabuleiroAtual[2] == casaVazia):
                        if("A3" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("A3")
                
                if(tabuleiroAtual[3] == pecaAdversario):
                    if(tabuleiroAtual[4] == casaVazia):
                        if("B2" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("B2")
                elif(tabuleiroAtual[4] == pecaAdversario):
                    if(tabuleiroAtual[3] == casaVazia):
                        if("B1" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("B1")
            
            if(tabuleiroAtual[6] == pecaAdversario):
                if(tabuleiroAtual[0] == pecaAdversario):
                    if(tabuleiroAtual[3] == casaVazia):
                        if("B1" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("B1")
                elif(tabuleiroAtual[3] == pecaAdversario):
                    if(tabuleiroAtual[0] == casaVazia):
                        if("A1" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("A1")
                
                if(tabuleiroAtual[4] == pecaAdversario):
                    if(tabuleiroAtual[2] == casaVazia):
                        if("A3" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("A3")
                elif(tabuleiroAtual[2] == pecaAdversario):
                    if(tabuleiroAtual[4] == casaVazia):
                        if("B2" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("B2")
                
                if(tabuleiroAtual[7] == pecaAdversario):
                    if(tabuleiroAtual[8] == casaVazia):
                        if("C3" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("C3")
                elif(tabuleiroAtual[8] == pecaAdversario):
                    if(tabuleiroAtual[7] == casaVazia):
                        if("C2" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("C2")
            
            if(tabuleiroAtual[7] == pecaAdversario):
                if(tabuleiroAtual[6] == pecaAdversario):
                    if(tabuleiroAtual[8] == casaVazia):
                        if("C3" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("C3")
                elif(tabuleiroAtual[8] == pecaAdversario):
                    if(tabuleiroAtual[6] == casaVazia):
                        if("C1" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("C1")
                
                if(tabuleiroAtual[1] == pecaAdversario):
                    if(tabuleiroAtual[4] == casaVazia):
                        if("B2" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("B2")
                elif(tabuleiroAtual[4] == pecaAdversario):
                    if(tabuleiroAtual[1] == casaVazia):
                        if("A2" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("A2")
            
            if(tabuleiroAtual[8] == pecaAdversario):
                if(tabuleiroAtual[6] == pecaAdversario):
                    if(tabuleiroAtual[7] == casaVazia):
                        if("C2" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("C2")
                elif(tabuleiroAtual[7] == pecaAdversario):
                    if(tabuleiroAtual[6] == casaVazia):
                        if("C1" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("C1")
                
                if(tabuleiroAtual[4] == pecaAdversario):
                    if(tabuleiroAtual[0] == casaVazia):
                        if("A1" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("A1")
                elif(tabuleiroAtual[0] == pecaAdversario):
                    if(tabuleiroAtual[4] == casaVazia):
                        if("B2" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("B2")
                
                if(tabuleiroAtual[6] == pecaAdversario):
                    if(tabuleiroAtual[7] == casaVazia):
                        if("C2" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("C2")
                elif(tabuleiroAtual[7] == pecaAdversario):
                    if(tabuleiroAtual[6] == casaVazia):
                        if("C1" not in listaPossiveisJogadasContra):
                            listaPossiveisJogadasContra.append("C1")

            # THE COMPUTER WILL KEEP THE HOUSES IT HAS FOUND AND, IF THE LIST HAS AT LEAST
            # 1 ITEM, THE COMPUTRE WILL MARK IT
            if(len(listaPossiveisJogadasContra) > 0):
                jogadaContraRealizada = True

        # IN CASE THE COMPUTER DIFFICULTY LEVEL IS MEDIUM OR HARD, IT WILL
        # IDENTIFY IF THERE'S ANY HOUSE THAT HAS IT'S PIECE AND, WHICH OTHERS
        # HOUSES IT CAN USE TO WIN.
        # IF THERE'S AT LEAST 1 HOUSE THAT WILL MAKE THE COMPUTER WIN, IT WILL ADD TO A LIST.
        if(nivelDificuldade >= medio):
            if(tabuleiroAtual[0] == pecaMaquina):
                if(tabuleiroAtual[1] == pecaMaquina):
                    if(tabuleiroAtual[2] == casaVazia):
                        listaPossiveisJogadasVitoria.append("A3")
                if(tabuleiroAtual[2] == pecaMaquina):
                    if(tabuleiroAtual[1] == casaVazia):
                        listaPossiveisJogadasVitoria.append("A2")
                else:
                    if(tabuleiroAtual[1] == tabuleiroAtual[2] == casaVazia):
                        escolha = ["A2", "A3"]
                        listaPossiveisJogadasSimples.extend(escolha)

                if(tabuleiroAtual[3] == pecaMaquina):
                    if(tabuleiroAtual[6] == casaVazia):
                        listaPossiveisJogadasVitoria.append("C1")
                if(tabuleiroAtual[6] == pecaMaquina):
                    if(tabuleiroAtual[3] == casaVazia):
                        listaPossiveisJogadasVitoria.append("B1")
                else:
                    if(tabuleiroAtual[3] == tabuleiroAtual[6] == casaVazia):
                        escolha = ["B1", "C1"]
                        listaPossiveisJogadasSimples.extend(escolha)

                if(tabuleiroAtual[4] == pecaMaquina):
                    if(tabuleiroAtual[8] == casaVazia):
                        listaPossiveisJogadasVitoria.append("C3")
                if(tabuleiroAtual[8] == pecaMaquina):
                    if(tabuleiroAtual[4] == casaVazia):
                        listaPossiveisJogadasVitoria.append("B2")
                else:
                    if(tabuleiroAtual[4] == tabuleiroAtual[8] == casaVazia):
                        escolha = ["B2", "C3"]
                        listaPossiveisJogadasSimples.extend(escolha)

            if(tabuleiroAtual[1] == pecaMaquina):
                if(tabuleiroAtual[0] == pecaMaquina):
                    if(tabuleiroAtual[2] == casaVazia):
                        # IF THIS HOUSE IS ALREADY ADDED TO THE LIST, IT WON'T BE ADDED
                        if("A3" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("A3")
                if(tabuleiroAtual[2] == pecaMaquina):
                    if(tabuleiroAtual[0] == casaVazia):
                        listaPossiveisJogadasVitoria.append("A1")
                else:
                    if(tabuleiroAtual[0] == tabuleiroAtual[2] == casaVazia):
                        escolha = ["A1", "A3"]
                        for casa in escolha:
                            # IF THIS HOUSE IS ALREADY ADDED TO THE LIST, IT WON'T BE ADDED
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)

                if(tabuleiroAtual[4] == pecaMaquina):
                    if(tabuleiroAtual[7] == casaVazia):
                        listaPossiveisJogadasVitoria.append("C2")
                if(tabuleiroAtual[7] == pecaMaquina):
                    if(tabuleiroAtual[4] == casaVazia):
                        if("B2" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("B2")
                else:
                    if(tabuleiroAtual[4] == tabuleiroAtual[7] == casaVazia):
                        escolha = ["B2", "C2"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)
                
            if(tabuleiroAtual[2] == pecaMaquina):
                if(tabuleiroAtual[0] == pecaMaquina):
                    if(tabuleiroAtual[1] == casaVazia):
                        if("A2" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("A2")
                if(tabuleiroAtual[1] == pecaMaquina):
                    if(tabuleiroAtual[0] == casaVazia):
                        if("A1" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("A1")
                else:
                    if(tabuleiroAtual[0] == tabuleiroAtual[1] == casaVazia):
                        escolha = ["A1", "A2"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)

                if(tabuleiroAtual[5] == pecaMaquina):
                    if(tabuleiroAtual[8] == casaVazia):
                        if("C3" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("C3")
                if(tabuleiroAtual[8] == pecaMaquina):
                    if(tabuleiroAtual[5] == casaVazia):
                        listaPossiveisJogadasVitoria.append("B3")
                else:
                    if(tabuleiroAtual[5] == tabuleiroAtual[8] == casaVazia):
                        escolha = ["B3", "C3"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)

                if(tabuleiroAtual[4] == pecaMaquina):
                    if(tabuleiroAtual[6] == casaVazia):
                        if("C1" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("C1")
                if(tabuleiroAtual[6] == pecaMaquina):
                    if(tabuleiroAtual[4] == casaVazia):
                        if("B2" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("B2")
                else:
                    if(tabuleiroAtual[4] == tabuleiroAtual[6] == casaVazia):
                        escolha = ["B2", "C1"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)

            if(tabuleiroAtual[3] == pecaMaquina):
                if(tabuleiroAtual[4] == pecaMaquina):
                    if(tabuleiroAtual[5] == casaVazia):
                        if("B3" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("B3")
                if(tabuleiroAtual[5] == pecaMaquina):
                    if(tabuleiroAtual[4] == casaVazia):
                        if("B2" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("B2")
                else:
                    if(tabuleiroAtual[4] == tabuleiroAtual[5] == casaVazia):
                        escolha = ["B2", "B3"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)

                if(tabuleiroAtual[0] == pecaMaquina):
                    if(tabuleiroAtual[6] == casaVazia):
                        if("C1" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("C1")
                if(tabuleiroAtual[6] == pecaMaquina):
                    if(tabuleiroAtual[0] == casaVazia):
                        if("A1" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("A1")
                else:
                    if(tabuleiroAtual[0] == tabuleiroAtual[6] == casaVazia):
                        escolha = ["A1", "C1"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)
                
            if(tabuleiroAtual[4] == pecaMaquina):
                if(tabuleiroAtual[0] == pecaMaquina):
                    if(tabuleiroAtual[8] == casaVazia):
                        if("C3" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("C3")
                if(tabuleiroAtual[8] == pecaMaquina):
                    if(tabuleiroAtual[0] == casaVazia):
                        if("A1" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("A1")
                else:
                    if(tabuleiroAtual[0] == tabuleiroAtual[8] == casaVazia):
                        escolha = ["A1", "C3"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)

                if(tabuleiroAtual[1] == pecaMaquina):
                    if(tabuleiroAtual[7] == casaVazia):
                        if("C2" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("C2")
                if(tabuleiroAtual[7] == pecaMaquina):
                    if(tabuleiroAtual[1] == casaVazia):
                        if("A2" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("A2")
                else:
                    if(tabuleiroAtual[1] == tabuleiroAtual[7] == casaVazia):
                        escolha = ["A2", "C2"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)

                if(tabuleiroAtual[2] == pecaMaquina):
                    if(tabuleiroAtual[6] == casaVazia):
                        if("C1" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("C1")
                if(tabuleiroAtual[6] == pecaMaquina):
                    if(tabuleiroAtual[2] == casaVazia):
                        if("A3" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("A3")
                else:
                    if(tabuleiroAtual[2] == tabuleiroAtual[6] == casaVazia):
                        escolha = ["A3", "C1"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)

                if(tabuleiroAtual[3] == pecaMaquina):
                    if(tabuleiroAtual[5] == casaVazia):
                        if("B3" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("B3")
                if(tabuleiroAtual[5] == pecaMaquina):
                    if(tabuleiroAtual[3] == casaVazia):
                        if("B1" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("B1")
                else:
                    if(tabuleiroAtual[3] == tabuleiroAtual[5] == casaVazia):
                        escolha = ["B1", "B3"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)

            if(tabuleiroAtual[5] == pecaMaquina):
                if(tabuleiroAtual[4] == pecaMaquina):
                    if(tabuleiroAtual[3] == casaVazia):
                        if("B1" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("B1")
                if(tabuleiroAtual[3] == pecaMaquina):
                    if(tabuleiroAtual[4] == casaVazia):
                        if("B2" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("B2")
                else:
                    if(tabuleiroAtual[3] == tabuleiroAtual[4] == casaVazia):
                        escolha = ["B1", "B2"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)

                if(tabuleiroAtual[2] == pecaMaquina):
                    if(tabuleiroAtual[8] == casaVazia):
                        if("C3" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("C3")
                if(tabuleiroAtual[8] == pecaMaquina):
                    if(tabuleiroAtual[2] == casaVazia):
                        if("A3" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("A3")
                else:
                    if(tabuleiroAtual[2] == tabuleiroAtual[8] == casaVazia):
                        escolha = ["A3", "C3"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)
                
            if(tabuleiroAtual[6] == pecaMaquina):
                if(tabuleiroAtual[3] == pecaMaquina):
                    if(tabuleiroAtual[0] == casaVazia):
                        if("A1" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("A1")
                if(tabuleiroAtual[0] == pecaMaquina):
                    if(tabuleiroAtual[3] == casaVazia):
                        if("B1" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("B1")
                else:
                    if(tabuleiroAtual[0] == tabuleiroAtual[3] == casaVazia):
                        escolha = ["A1", "B1"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)

                if(tabuleiroAtual[4] == pecaMaquina):
                    if(tabuleiroAtual[2] == casaVazia):
                        if("A3" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("A3")
                if(tabuleiroAtual[2] == pecaMaquina):
                    if(tabuleiroAtual[4] == casaVazia):
                        if("B2" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("B2")
                else:
                    if(tabuleiroAtual[2] == tabuleiroAtual[4] == casaVazia):
                        escolha = ["A3", "B2"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)

                if(tabuleiroAtual[7] == pecaMaquina):
                    if(tabuleiroAtual[8] == casaVazia):
                        if("C3" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("C3")
                if(tabuleiroAtual[8] == pecaMaquina):
                    if(tabuleiroAtual[7] == casaVazia):
                        if("C2" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("C2")
                else:
                    if(tabuleiroAtual[7] == tabuleiroAtual[8] == casaVazia):
                        escolha = ["C2", "C3"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)

            if(tabuleiroAtual[7] == pecaMaquina):
                if(tabuleiroAtual[6] == pecaMaquina):
                    if(tabuleiroAtual[8] == casaVazia):
                        if("C3" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("C3")
                if(tabuleiroAtual[8] == pecaMaquina):
                    if(tabuleiroAtual[6] == casaVazia):
                        if("C1" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("C1")
                else:
                    if(tabuleiroAtual[6] == tabuleiroAtual[8] == casaVazia):
                        escolha = ["C1", "C3"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)

                if(tabuleiroAtual[4] == pecaMaquina):
                    if(tabuleiroAtual[1] == casaVazia):
                        if("A2" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("A2")
                if(tabuleiroAtual[1] == pecaMaquina):
                    if(tabuleiroAtual[4] == casaVazia):
                        if("B2" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("B2")
                else:
                    if(tabuleiroAtual[1] == tabuleiroAtual[4] == casaVazia):
                        escolha = ["A2", "B2"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)
            
            if(tabuleiroAtual[8] == pecaMaquina):
                if(tabuleiroAtual[7] == pecaMaquina):
                    if(tabuleiroAtual[6] == casaVazia):
                        if("C1" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("C1")
                if(tabuleiroAtual[6] == pecaMaquina):
                    if(tabuleiroAtual[7] == casaVazia):
                        if("C2" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("C2")
                else:
                    if(tabuleiroAtual[6] == tabuleiroAtual[7] == casaVazia):
                        escolha = ["C1", "C2"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)

                if(tabuleiroAtual[5] == pecaMaquina):
                    if(tabuleiroAtual[2] == casaVazia):
                        if("A3" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("A3")
                if(tabuleiroAtual[2] == pecaMaquina):
                    if(tabuleiroAtual[5] == casaVazia):
                        if("B3" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("B3")
                else:
                    if(tabuleiroAtual[2] == tabuleiroAtual[5] == casaVazia):
                        escolha = ["A3", "B3"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)

                if(tabuleiroAtual[4] == pecaMaquina):
                    if(tabuleiroAtual[0] == casaVazia):
                        if("A1" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("A1")
                if(tabuleiroAtual[0] == pecaMaquina):
                    if(tabuleiroAtual[4] == casaVazia):
                        if("B2" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("B2")
                else:
                    if(tabuleiroAtual[0] == tabuleiroAtual[4] == casaVazia):
                        escolha = ["A1", "B2"]
                        for casa in escolha:
                            if(casa not in listaPossiveisJogadasSimples):
                                listaPossiveisJogadasSimples.append(casa)
            
            # THE COMPUTER WILL KEEP THE HOUSES IT HAS FOUND AND, IF THE LIST HAS AT LEAST
            # 1 ITEM, THE COMPUTRE WILL MARK IT
            if(len(listaPossiveisJogadasVitoria) > 0):
                vitoriaGarantida = True
            
            # THE COMPUTER WILL KEEP THE HOUSES IT HAS FOUND AND, IF THE LIST HAS AT LEAST
            # 1 ITEM, THE COMPUTRE WILL MARK IT
            if(len(listaPossiveisJogadasSimples) > 0):
                jogadaSimplesRealizada  = True

        # IF THE COMPUTER FOUND AT LEAST 1 HOUSE THAT WILL MAKE IT WIN,
        # IT WILL PRIORITIZE THIS.
        if(vitoriaGarantida == True):
            movimentoComputador = random.choice(listaPossiveisJogadasVitoria)
        # IN CASE THE COMPUTAR DIDN'T FOUND A HOUSE TO WIN THE GAME, BUT FOUND ONE
        # THAT WILL MAKE THE USER WIN, IT WILL PRIORITIZE THIS.
        elif(jogadaContraRealizada == True):
            movimentoComputador = random.choice(listaPossiveisJogadasContra)
        # IN CASE THE COMPUTER DIDN'T FOUND A HOUSE TO WIN THE GAME AND ALSO DIDN'T
        # FOUND ONE THAT WILL MAKE THE USER WIN, IT WILL SEE IF THERE'S HOUSES THAT
        # IT WILL HELP IT WIN.
        elif(jogadaSimplesRealizada == True):
            movimentoComputador = random.choice(listaPossiveisJogadasSimples)

        # IF THE COMPUTER DIFFICULTY LEVEL IS EASY, MEDIUM OR HARD, IT WILL SEE THE FOLLOWING CONDITION:
        # IF THERE'S NO HOUSE THAT WILL MAKE IT WIN; IF THE USER'S DON'T HAVE A WAY TO WIN; AND IF THERE
        # ARE NO OTHERS HOUSES THAT CAN HELP IT WIN.
        # IF THEESE CONDITIONS HAPPENS, THE COMPUTER WILL CHOOSE RANDOMLY ANY HOUSE THAT IS STILL
        # AVAILABLE ON THE BOARD.
        # IF THE DIFFICULTY LEVEL IS ONLY EASY, IT WILL ONLY CHOOSE RANDOMLY ANY HOUSE THAT IS STILL
        # AVAILABLE ON THE BOARD.
        if(nivelDificuldade >= facil):
            if((jogadaSimplesRealizada == False) and (jogadaContraRealizada == False) and (vitoriaGarantida == False)):
                movimentoComputador = random.choice(casasDisponiveis)
    
    casasUsadas.append(movimentoComputador)

    return movimentoComputador, casasUsadas

# ERROR MASSAGE IF THE PLAYER CHOOSE A INVALID OPTION
def erroOpcaoInvalida():
    print("Error! You didn't typed on of the available options!\nPlease, try again!")

# ERROR MESSAGE IF THE PLAYER CHOOSES A HOUSE THAT IS ALREADY USED ON THE BOARD
def erroCasaUsada():
    print("Error! This house was already used!\nYou can't use it anymore!\nPlease, try again!")

# ERROR MESSAGE IF THE PLAYER TYPED AN INVALID COORDINATE
def erroCoordenadaValida():
    print("Error! You didn't typed a valid coordinate!\nPlease, try again!")

# FUNCTION TO CHANGE WHO WILL PLAY NOW
def trocarJogador(jogAtual, jog1, jog2):
    jogAtual = jog2
    jog2 = jog1
    jog1 = jogAtual

    return jogAtual, jog1, jog2

# FUNCTION THAT IDENTIFY THE USER'S OPERATIONAL SYSTEM, AND CLEAR THE SCREAM
def limparTela():
    comando = None

    if(platform.system() == "Windows"):
        comando = "cls"
    else:
        comando = "clear"

    os.system(comando)

# CONVERT THE USER'S OPTIONS IN NUMBERS AND, IN CASE IT CAN'T, RETURNS A ERROR MESSAGEM FROM opcaoInvalida()
def converterOpcoes(opcaoDigitada):
    opcaoValida = None
    try:
        opcaoDigitada = int(opcaoDigitada)
        opcaoValida = True
    except:
        opcaoValida = False

    return opcaoValida, opcaoDigitada

# FUNCTION THAT PRINTS THE BOARD'S CURRENT STATUS, WITH IT'S HOUSES THAT ARE OCCUPIED AND EMPTY
def tabuleiro(coordenadas):
    print("    A   B   C  \n  ┌───┬───┬───┐")
    print(f"1 │ {coordenadas[0]} │ {coordenadas[3]} │ {coordenadas[6]} │\n  ├───┼───┼───┤")
    print(f"2 │ {coordenadas[1]} │ {coordenadas[4]} │ {coordenadas[7]} │\n  ├───┼───┼───┤")
    print(f"3 │ {coordenadas[2]} │ {coordenadas[5]} │ {coordenadas[8]} │\n  └───┴───┴───┘")

if __name__ == '__main__':
    print('-' * 30)
    print("Welcome user!")
    print("This program is a Tic Tac Toe game. You can choose to play against other person, " \
          "against the computer ou machina against machine.")

    while(True):
        while(True):
            listaCasasDisponiveis = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            listaJogadas = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            listaCasasUsadas = []
            jogadasAtuais = contagemDifMaq = 0
            jogador1 = jogadorAtual = 'X'
            jogador2 = 'O'
            jogadorMaquina = jogadorHumano = jogadorAdversario = difAtual = None
            jogarNovamente = opcoesContra = opcoesDificuldade = jogada = difMaq1 = difMaq2 = None

            print('-' * 30)
            print(f"Choose one of the following options:\n{contraAmigo} - Play against friend;")
            print(f"{contraComputador} - Play against machine;\n{maqContraMaq} - Machine against machine;")
            opcoesContra = input()
            limparTela()

            statusOpcao, opcoesContra = converterOpcoes(opcoesContra)

            if(statusOpcao == True):
                if(opcoesContra == contraComputador):
                    while(True):
                        print('-' * 30)
                        print("Now, which difficulty level you wish for the computer")
                        print(f"{difFacil} - Easy;\n{difMedio} - Medium;\n{difDificil} - Hard;")
                        opcoesDificuldade = input()
                        limparTela()

                        statusOpcao, opcoesDificuldade = converterOpcoes(opcoesDificuldade)

                        if(statusOpcao == True):
                                if((opcoesDificuldade < difFacil) or (opcoesDificuldade > difDificil)):
                                    print('-' * 30)
                                    erroOpcaoInvalida()
                                else:
                                    break
                        else:
                            print('-' * 30)
                            erroOpcaoInvalida()
                    break
                elif(opcoesContra == maqContraMaq):
                    while(contagemDifMaq < 2):
                        print('-' * 30)
                        print(f"Now, which difficulty level you wish for computer {jogadorAtual}?")
                        print(f"{difFacil} - Easy;\n{difMedio} - Medium;\n{difDificil} - Hard;")
                        difAtual = input()
                        limparTela()
                        
                        statusOpcao, difAtual = converterOpcoes(difAtual)
                        difMaq1 = difAtual
                        
                        if(statusOpcao == True):
                            if((difAtual < difFacil) or (difAtual > difDificil)):
                                print('-' * 30)
                                erroOpcaoInvalida()
                            else:
                                jogadorAtual, jogador1, jogador2 = trocarJogador(jogadorAtual, jogador1, jogador2)
                                difAtual, difMaq1, difMaq2 = trocarJogador(difAtual, difMaq1, difMaq2)
                                contagemDifMaq += 1
                        else:
                            print('-' * 30)
                            erroOpcaoInvalida()
                    break
                elif(opcoesContra == contraAmigo):
                    break
                else:
                    print('-' * 30)
                    erroOpcaoInvalida()
            else:
                print('-' * 30)
                erroOpcaoInvalida()

        limparTela()

        if(opcoesContra == contraAmigo):
            print('-' * 30)
            print("Here is the board!\nTo choose a house, type the coordinate!(Ex:A3)")

            # WHILE THE NUMBER OS MOVES IS LESS THAN THE NUMBER OF HOUSES OF THE BOARD, THE GAMES KEEP GOING
            while(jogadasAtuais < maxJogadas):
                print('-' * 30)
                tabuleiro(listaJogadas)
                print(f"What is your move, player {jogadorAtual}?(Ex:A3)")
                jogada = input()
                limparTela()
                jogada = jogada.upper()
                jogadasAtuais += 1

                jogadaValida = verificarCoordenada(jogada)

                if(jogadaValida == True):
                    casaAtual, listaCasasUsadas = verificarJogada(jogada, listaCasasUsadas)

                    if(casaAtual == False):
                        listaJogadas = posicionarJogada(jogada, listaJogadas, jogadorAtual)
                        statusJogo, ganhador = verificarVitoria(listaJogadas, jogador1, jogador2)
                        
                        if(statusJogo == False):
                            jogadorAtual, jogador1, jogador2 = trocarJogador(jogadorAtual, jogador1, jogador2)
                        else:
                            print('-' * 30)
                            print(f"GAME OVER!\nWINNER: {ganhador}")
                            print('-' * 30)
                            tabuleiro(listaJogadas)
                            break
                    else:
                        print('-' * 30)
                        erroCasaUsada()
                else:
                    print('-' * 30)
                    erroCoordenadaValida()
                
        elif(opcoesContra == contraComputador):
            print('-' * 30)
            print("Please wait. The game is deciding who will play frist!")
            time.sleep(2)
            # RAFFLE TO SE IF THE USER OR COMPUTER STARTS
            jogadorInicial = random.randint(1,2)
            print('-' * 30)

            if(jogadorInicial == 1):
                print("the computer starts!")
                time.sleep(1)
                jogadorMaquina = jogador1
                jogadorHumano = jogador2
            else:
                print("You start!")
                jogadorHumano = jogador1
                jogadorMaquina = jogador2
                print("Here is the board!\nTo choose a house, type the coordinate!(Ex:A3)")

            difComp = "Easy" if(opcoesDificuldade == difFacil) else "Medium" if(opcoesDificuldade == difMedio) else "Hard"

            # WHILE THE NUMBER OS MOVES IS LESS THAN THE NUMBER OF HOUSES OF THE BOARD, THE GAMES KEEP GOING
            while(jogadasAtuais < maxJogadas):
                if(jogadorAtual == jogadorMaquina):
                    jogadaMaquina, listaCasasUsadas = jogadaComputador(listaCasasUsadas, listaCasasDisponiveis, 
                                                                    jogadorMaquina, jogadorHumano, listaJogadas, 
                                                                    opcoesDificuldade)
                    listaJogadas = posicionarJogada(jogadaMaquina, listaJogadas, jogadorMaquina)
                else:
                    while(True):
                        print('-' * 30)
                        print(f"Computer difficulty: {difComp}")
                        print('-' * 30)
                        tabuleiro(listaJogadas)
                        print(f"What is your move, player {jogadorHumano}?(Ex:A3)")
                        jogada = input()
                        jogada = jogada.upper()
                        limparTela()

                        jogadaValida = verificarCoordenada(jogada)

                        if(jogadaValida == True):
                            casaAtual, listaCasasUsadas = verificarJogada(jogada, listaCasasUsadas)

                            if(casaAtual == False):
                                listaJogadas = posicionarJogada(jogada, listaJogadas, jogadorAtual)
                                break
                            else:
                                print('-' * 30)
                                erroCasaUsada()
                        else:
                            print('-' * 30)
                            erroCoordenadaValida()

                statusJogo, ganhador = verificarVitoria(listaJogadas, jogadorMaquina, jogadorHumano)

                if(statusJogo == False):
                    jogadorAtual, jogador1, jogador2 = trocarJogador(jogadorAtual, jogador1, jogador2)
                    jogadasAtuais += 1
                else:
                    print('-' * 30)

                    ganhador = "MACHINE" if(ganhador == jogadorMaquina) else "YOU"

                    print(f"GAME OVER!\nWINNER: {ganhador}")
                    print('-' * 30)
                    print(f"Computer difficulty: {difComp}")
                    print('-' * 30)
                    tabuleiro(listaJogadas)
                    print('-' * 30)
                    break
        # IF THE USER CHOOSES TO SEE MACHINE AGAINST MACHINE
        else:
            # WHILE THE NUMBER OS MOVES IS LESS THAN THE NUMBER OF HOUSES OF THE BOARD, THE GAMES KEEP GOING
            while(jogadasAtuais < maxJogadas):
                print('-' * 30)
                tabuleiro(listaJogadas)
                print(f"Player's turn: {jogadorAtual}")

                dificuldade = "Easy" if(difAtual == difFacil) else "Medium" if(difAtual == difMedio) else "Hard"

                print(f"Difficulty: {dificuldade}")
                # TIME FOR THE USER TO SEE EACH MOVE FROM THE MACHINES
                time.sleep(2)
                jogadorAdversario = jogador2
                jogadaMaquina, listaCasasUsadas = jogadaComputador(listaCasasUsadas, listaCasasDisponiveis, 
                                                                    jogadorAtual, jogadorAdversario, listaJogadas, 
                                                                    difAtual)
                limparTela()
                jogadasAtuais += 1
                listaJogadas = posicionarJogada(jogadaMaquina, listaJogadas, jogadorAtual)
                statusJogo, ganhador = verificarVitoria(listaJogadas, jogadorAtual, jogadorAdversario)

                if(statusJogo == False):
                    jogadorAtual, jogador1, jogador2 = trocarJogador(jogadorAtual, jogador1, jogador2)
                    # AS EACH MACHINE HAS IT'S OWN LEVEL OF DIFFICULTY, I USED THE FUNCTION
                    # trocarJogador() TO DO THE SAME WITH THE DIFFICULTY OF EACH MACHINE
                    difAtual, difMaq1, difMaq2 = trocarJogador(difAtual, difMaq1, difMaq2)
                else:
                    print('-' * 30)
                    print(f"GAME OVER!\nWINNER: {ganhador}")
                    print('-' * 30)
                    
                    dif1 = "Easy" if (difAtual == difFacil) else "Medium" if(difAtual == difMedio) else "Hard"
                    dif2 = "Easy" if (difMaq2 == difFacil) else "Medium" if(difMaq2 == difMedio) else "Hard"

                    print(f"Machine's {jogadorAtual} difficulty: {dif1}")
                    print(f"Machine's {jogadorAdversario} difficulty: {dif2}")
                    tabuleiro(listaJogadas)
                    print('-' * 30)
                    break

        if((jogadasAtuais == maxJogadas) and (statusJogo == False)):
            print('-' * 30)
            tabuleiro(listaJogadas)
            print('-' * 30)
            print("GAME OVER!\nDRAW!")
            print('-' * 30)

        print("To play again, please type any key and then 'ENTER':")
        print("To exit, just press 'ENTER':")
        jogarNovamente = input()
            
        if(jogarNovamente == ""):
            print('-' * 30)
            print("Program closing...")
            time.sleep(3)
            break
        else:
            limparTela()
            continue