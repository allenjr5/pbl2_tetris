#Importação de Bibliotecas
import os
import time
import random

#Função que inicia o tabuleiro
def inicia_tabuleiro():
    tabuleiro=[]
    for i in range(20):
        linha=[]
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)
    return tabuleiro

#Função que inicia as peças
def inicia_pecas():
    pecas=[
        peca_i:=['1', '1', '1', '1'],
        peca_o:=[['1', '1'], ['1', '1']],
        peca_t:=[['1', '1', '1'], ['0', '1', '0']],
        peca_s:=[['0', '1', '1'], ['1', '1', '0']],
        peca_z:=[['1', '1', '0'], ['0', '1', '1']],
        peca_j:=[['1', '0', '0'], ['1', '1', '1']],
        peca_l:=[['0', '0', '1'], ['1', '1', '1']]
    ]
    return pecas

#Função que escolhe a peça a ser colocada no tabuleiro
def escolhe_peca(pecas):
    peca_escolhida=random.choice(pecas)
    return peca_escolhida

#Função que mostra o tabuleiro
def mostra_tabuleiro(tabuleiro):
    for i in range(20):
        for j in range(10):
            print(tabuleiro[i][j], end=' ')
        print()

#Função que limpa o terminal
def limpa_terminal():
    time.sleep(1)
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

#Função principal do programa
def main():
    tabuleiro=inicia_tabuleiro()
    pecas=inicia_pecas()
    while True:
        peca_escolhida=escolhe_peca(pecas)
        mostra_tabuleiro(tabuleiro)
        limpa_terminal()

#Chamada da função principal do programa
main()
