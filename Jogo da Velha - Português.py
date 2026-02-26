import random
import time
import os
import platform

continuar = contraAmigo = difFacil = 1
contraComputador = difMedio = 2
maqContraMaq = difDificil = 3
maxJogadas = 9

# VERIFICA SE A COORDENADA INSERIDA PELO USUÁRIO É VÁLIDA OU NÃO.
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

# COM BASE NA COORDENADA, COLOCA A PEÇA DO JOGADOR NO TABULEIRO.
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

# VERIFICA SE A COORDENADA INSERIDA PELO USUÁRIO JÁ FOI USADA OU NÃO.
def verificarJogada(casaJogador, casasUsadas):
    casaUsada = None

    if(casaJogador in casasUsadas):
        casaUsada = True
    else:
        casaUsada = False
        casasUsadas.append(casaJogador)

    return casaUsada, casasUsadas

# COM BASE NAS CASAS DO TABULEIRO QUE ESTÃO OCUPADAS, VERIFICA SE ALGUM JOGADOR JÁ VENCEU OU NÃO.
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

# FUNÇÃO QUE IRÁ DETERMINAR O NÍVEL DE INTELIGÊNCIA DO COMPUTADOR.
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
    
    # CASO O COMPUTADOR COMECE A JOGAR, ELE IRÁ ESCOLHER UMA CASA ALEATÓRIA NO TABULEIRO.
    if(len(casasUsadas) == 0):
        movimentoComputador = random.choice(casasDisponiveis)
    else:
        # VERIFICA QUAIS CASAS ESTÃO DISPONÍVEIS PARA USAR NO TABULEIRO.
        for casa in casasUsadas:
            for casas in casasDisponiveis:
                if(casa == casas):
                    casasDisponiveis.remove(casa)

        # CASO O NÍVEL DE DIFICULDADE DO COMPUTADOR SEJA DIFÍCIL, ELE IRÁ IDENTIFICAR
        # SE O USUÁRIO NECESSITA DE PELO MENOS 1 CASA PARA VENCER.
        # SE OCORRER, O COMPUTADOR IRÁ GUARDAR AS CASAS QUE POSSAM FAZER O USUÁRIO
        # GANHAR EM UMA LISTA E IRÁ ESCOLHER ENTRE UMA DELAS PARA IMPEDIR A VITÓRIA DO USUÁRIO.
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
                        # SE ESTA CASA JÁ FOI ADICIONADA À LISTA, ELA NÃO É MAIS ADICIONADA
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

            # O COMPUTADOR GUARDA AS CASAS QUE ENCONTROU E, CASO A LISTA TENHA PELO MENOS
            # 1 ITEM, O COMPUTADOR MARCA ISSO
            if(len(listaPossiveisJogadasContra) > 0):
                jogadaContraRealizada = True

        # CASO O NÍVEL DE DIFICULDADE DO COMPUTADOR SEJA MÉDIO OU DIFÍCIL, ELE IRÁ
        # IDENTIFICAR SE HÁ ALGUMA CASA QUE ELE TENHA UMA PEÇA SUA E, QUAIS AS OUTRAS
        # CASAS ELE PODE USAR PARA PODER GANHAR.
        # SE HÁ PELO MENOS 1 CASA QUE IRÁ GARANTIR A VITÓRIA, ELE GUARDA EM UMA LISTA.
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
                        # SE ESTA CASA JÁ FOI ADICIONADA À LISTA, ELA NÃO É MAIS ADICIONADA
                        if("A3" not in listaPossiveisJogadasVitoria):
                            listaPossiveisJogadasVitoria.append("A3")
                if(tabuleiroAtual[2] == pecaMaquina):
                    if(tabuleiroAtual[0] == casaVazia):
                        listaPossiveisJogadasVitoria.append("A1")
                else:
                    if(tabuleiroAtual[0] == tabuleiroAtual[2] == casaVazia):
                        escolha = ["A1", "A3"]
                        for casa in escolha:
                            # SE ESTA CASA JÁ FOI ADICIONADA À LISTA, ELA NÃO É MAIS ADICIONADA
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
            
            # O COMPUTADOR GUARDA AS CASAS QUE ENCONTROU E, CASO A LISTA TENHA PELO MENOS
            # 1 ITEM, O COMPUTADOR MARCA ISSO
            if(len(listaPossiveisJogadasVitoria) > 0):
                vitoriaGarantida = True
            
            # O COMPUTADOR GUARDA AS CASAS QUE ENCONTROU E, CASO A LISTA TENHA PELO MENOS
            # 1 ITEM, O COMPUTADOR MARCA ISSO
            if(len(listaPossiveisJogadasSimples) > 0):
                jogadaSimplesRealizada  = True

        # SE O COMPUTADOR ENCONTROU PELO MENOS UMA CASA QUE IRÁ GARANTIR SUA VITÓRIA,
        # ELE IRÁ DAR PRIORIDADE À ISSO
        if(vitoriaGarantida == True):
            movimentoComputador = random.choice(listaPossiveisJogadasVitoria)
        # CASO O COMPUTADOR NÃO TENHA COMO GARANTIR A VITÓRIA, MAS HÁ COMO IMPEDIR A 
        # VITÓRIA DO JOGADOR, ELE IRÁ PRIORIZAR ISSO
        elif(jogadaContraRealizada == True):
            movimentoComputador = random.choice(listaPossiveisJogadasContra)
        # CASO O COMPUTADOR NÃO CONSIGA GARANTIR A VITÓRIA, MAS TAMBÉM NÃO IDENTIFICOU QUE O
        # USUÁRIO POSSA GANHAR, ELE VERÁ SE HÁ CASAS QUE POSSAM AJUDÁ-LO A VENCER
        elif(jogadaSimplesRealizada == True):
            movimentoComputador = random.choice(listaPossiveisJogadasSimples)

        # SE A DIFICULDADE DO COMPUTADOR FOR FÁCIL, MÉDIO OU DIFÍCIL, ELE TERÁ QUE VERIFICAR A SEGUINTE CONDIÇÃO:
        # SE NÃO HÁ COMO GARANTIR A VITÓRIA; SE O USUÁRIO NÃO TEM UMA CASA QUE POSSA GARANTIR SUA VITÓRIA; E
        # SE NÃO HÁ MAIS CASAS QUE POSSAM AJUDÁ-LO A GANHAR.
        # CASO TODAS ESSAS CONDIÇÕES OCORREREM, O COMPUTADOR IRÁ ESCOLHER ALEATÓRIAMENTE ALGUMA CASA QUE
        # AINDA ESTEJA DISPONÍVEL NO TABULEIRO.
        # CASO O DIFICULDADE SEJA SOMENTE FÁCIL, ELE SÓ IRA ESCOLHER UMA CASA DISPONÍVEL ALEATORIAMENTE
        # NO TABULEIRO.
        if(nivelDificuldade >= facil):
            if((jogadaSimplesRealizada == False) and (jogadaContraRealizada == False) and (vitoriaGarantida == False)):
                movimentoComputador = random.choice(casasDisponiveis)
    
    casasUsadas.append(movimentoComputador)

    return movimentoComputador, casasUsadas

# MENSAGEM DE ERRO CASO O JOGADOR ESCOLHA UMA OPÇÃO INVÁLIDA
def erroOpcaoInvalida():
    print("Erro! Você não digitou uma das opções disponíveis!\nPor favor, tente novamente!")

# MENSAGEM DE ERRO CASO O JOGADOR ESCOLHA UMA CASA QUE JÁ FOI USADA NO TABULEIRO
def erroCasaUsada():
    print("Erro! Está casa já foi usada!\nVocê não pode mais usa-lá!\nPor favor, tente novamente!")

# MENSAGEM DE ERRO CASO O JOGADOR INSIRA UMA COORDENADA INVÁLIDA
def erroCoordenadaValida():
    print("Erro! Você não digitou uma coordenada válida!\nPor favor, tente novamente!")

# FUNÇÃO PARA TROCAR A VEZ DE QUEM IRÁ JOGAR
def trocarJogador(jogAtual, jog1, jog2):
    jogAtual = jog2
    jog2 = jog1
    jog1 = jogAtual

    return jogAtual, jog1, jog2

# FUNÇÃO QUE IDENTIFICA O SISTEMA OPERACIONAL DO USUÁRIO, E LIMPA A TELA EM DETERMINADOS PONTOS DO SCRIPT
def limparTela():
    comando = None

    if(platform.system() == "Windows"):
        comando = "cls"
    else:
        comando = "clear"

    os.system(comando)

# CONVERTE AS OPÇÕES DO USUÁRIO EM NÚMEROS E, CASO NÃO CONSIGA, RETORNA UMA MENSAGEM DE opcaoInvalida()
def converterOpcoes(opcaoDigitada):
    opcaoValida = None
    try:
        opcaoDigitada = int(opcaoDigitada)
        opcaoValida = True
    except:
        opcaoValida = False

    return opcaoValida, opcaoDigitada

# FUNÇÃO QUE IMPRIME O ESTADO ATUAL DO TABULEIRO, COM SUAS CASAS QUE ESTÃO OCUPADAS E VAZIAS
def tabuleiro(coordenadas):
    print("    A   B   C  \n  ┌───┬───┬───┐")
    print(f"1 │ {coordenadas[0]} │ {coordenadas[3]} │ {coordenadas[6]} │\n  ├───┼───┼───┤")
    print(f"2 │ {coordenadas[1]} │ {coordenadas[4]} │ {coordenadas[7]} │\n  ├───┼───┼───┤")
    print(f"3 │ {coordenadas[2]} │ {coordenadas[5]} │ {coordenadas[8]} │\n  └───┴───┴───┘")

if __name__ == '__main__':
    print('-' * 30)
    print("Bem-vindo usuário!")
    print("Este programa é um jogo da velha, que você pode jogar contra outra pessoa, " \
    "contra o computador ou máquina contra máquina.")

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
            print(f"Escolha uma das opções a seguir:\n{contraAmigo} - Jogar contra um amigo;")
            print(f"{contraComputador} - Jogar contra a máquina;\n{maqContraMaq} - Máquina contra máquina;")
            opcoesContra = input()
            limparTela()

            statusOpcao, opcoesContra = converterOpcoes(opcoesContra)

            if(statusOpcao == True):
                if(opcoesContra == contraComputador):
                    while(True):
                        print('-' * 30)
                        print("Agora, qual a dificuldade você deseja que o computador tenha?")
                        print(f"{difFacil} - Fácil;\n{difMedio} - Médio;\n{difDificil} - Difícil;")
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
                        print(f"Agora, qual a dificuldade você deseja que o computador {jogadorAtual} tenha?")
                        print(f"{difFacil} - Fácil;\n{difMedio} - Médio;\n{difDificil} - Difícil;")
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
            print("Aqui está o tabuleiro!\nPara escolher uma casa, digite sua coordenada!(Ex:A3)")

            # ENQUANTO O NÚMERO DE JOGADAS FOR MENOS QUE O NÚMERO DE CASAS DO TABULEIRO, O JOGO CONTINUA
            while(jogadasAtuais < maxJogadas):
                print('-' * 30)
                tabuleiro(listaJogadas)
                print(f"Qual a sua jogada, jogador {jogadorAtual}?(Ex:A3)")
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
                            print(f"FIM de JOGO!\nVENCEDOR: {ganhador}")
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
            print("Por favor aguarde. O jogo está decidindo quem irá jogar primeiro!")
            time.sleep(2)
            # SORTEIO PARA VER SE O USUÁRIO OU A MÁQUINA COMEÇA
            jogadorInicial = random.randint(1,2)
            print('-' * 30)

            if(jogadorInicial == 1):
                print("O computador inicia o jogo!")
                time.sleep(1)
                jogadorMaquina = jogador1
                jogadorHumano = jogador2
            else:
                print("Você inicia o jogo!")
                jogadorHumano = jogador1
                jogadorMaquina = jogador2
                print("Aqui está o tabuleiro!\nPara escolher uma casa, digite sua coordenada!(Ex:A3)")

            difComp = "Fácil" if(opcoesDificuldade == difFacil) else "Médio" if(opcoesDificuldade == difMedio) else "Difícil"

            # ENQUANTO O NÚMERO DE JOGADAS FOR MENOS QUE O NÚMERO DE CASAS DO TABULEIRO, O JOGO CONTINUA
            while(jogadasAtuais < maxJogadas):
                if(jogadorAtual == jogadorMaquina):
                    jogadaMaquina, listaCasasUsadas = jogadaComputador(listaCasasUsadas, listaCasasDisponiveis, 
                                                                    jogadorMaquina, jogadorHumano, listaJogadas, 
                                                                    opcoesDificuldade)
                    listaJogadas = posicionarJogada(jogadaMaquina, listaJogadas, jogadorMaquina)
                else:
                    while(True):
                        print('-' * 30)
                        print(f"Dificuldade do computador: {difComp}")
                        print('-' * 30)
                        tabuleiro(listaJogadas)
                        print(f"Qual a sua jogada, jogador {jogadorHumano}?(Ex:A3)")
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

                    ganhador = "MÁQUINA" if(ganhador == jogadorMaquina) else "VOCÊ"

                    print(f"FIM de JOGO!\nVENCEDOR: {ganhador}")
                    print('-' * 30)
                    print(f"Dificuldade do computador: {difComp}")
                    print('-' * 30)
                    tabuleiro(listaJogadas)
                    print('-' * 30)
                    break
        # CASO O USUÁRIO ESCOLHA VER MÁQUINA CONTRA MÁQUINA
        else:
            # ENQUANTO O NÚMERO DE JOGADAS FOR MENOS QUE O NÚMERO DE CASAS DO TABULEIRO, O JOGO CONTINUA
            while(jogadasAtuais < maxJogadas):
                print('-' * 30)
                tabuleiro(listaJogadas)
                print(f"Vez do jogador: {jogadorAtual}")

                dificuldade = "Fácil" if(difAtual == difFacil) else "Médio" if(difAtual == difMedio) else "Difícil"

                print(f"Dificuldade: {dificuldade}")
                # TIMER PARA O USUÁRIO ACOMPANHAR CADA JOGADA DAS MÁQUINAS
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
                    # COMO CADA MÁQUINA TEM SEU PRÓPRIO NÍVEL DE DIFICULDADE, USEI A FUNÇÃO
                    # trocarJogador() PARA PODER FAZER O MESMO COM AS DIFICULDADE DE CADA MÁQUINA
                    difAtual, difMaq1, difMaq2 = trocarJogador(difAtual, difMaq1, difMaq2)
                else:
                    print('-' * 30)
                    print(f"FIM de JOGO!\nVENCEDOR: {ganhador}")
                    print('-' * 30)
                    
                    dif1 = "Fácil" if (difAtual == difFacil) else "Médio" if(difAtual == difMedio) else "Difícil"
                    dif2 = "Fácil" if (difMaq2 == difFacil) else "Médio" if(difMaq2 == difMedio) else "Difícil"

                    print(f"Dificuldade da máquina {jogadorAtual}: {dif1}")
                    print(f"Dificuldade da máquina {jogadorAdversario}: {dif2}")
                    tabuleiro(listaJogadas)
                    print('-' * 30)
                    break

        if((jogadasAtuais == maxJogadas) and (statusJogo == False)):
            print('-' * 30)
            tabuleiro(listaJogadas)
            print('-' * 30)
            print("FIM DE JOGO!\nEMPATE!")
            print('-' * 30)

        print("Para jogar novamente, por favor digite qualquer tecla e em seguida 'ENTER':")
        print("Para sair, basta apertar 'ENTER':")
        jogarNovamente = input()
            
        if(jogarNovamente == ""):
            print('-' * 30)
            print("Programa finalizado...")
            time.sleep(3)
            break
        else:
            limparTela()
            continue