#Importação de Bibliotecas
import os
import time
import random

#Função que inicia o tabuleiro
def inicia_tabuleiro(n_linhas, n_colunas):
    tabuleiro=[]
    for l in range(n_linhas):
        linha=[]
        for c in range(n_colunas):
            linha.append(0)
        tabuleiro.append(linha)
    return tabuleiro

#Função que inicia as peças
def inicia_pecas():
    pecas=[
        #Peça I
        ['1', '1', '1', '1'],
        #Peça O
        [['1', '1'], ['1', '1']],
        #Peça T
        [['1', '1', '1'], ['0', '1', '0']],
        #Peça S
        [['0', '1', '1'], ['1', '1', '0']],
        #Peça Z
        [['1', '1', '0'], ['0', '1', '1']],
        #Peça J
        [['1', '0', '0'], ['1', '1', '1']],
        #Peça L
        [['0', '0', '1'], ['1', '1', '1']]
    ]
    return pecas

#Função que seleciona a peça a ser adicionada no tabuleiro
def escolhe_peca(pecas):
    return random.choice(pecas)

#Função que adiciona a peça selecionada no tabuleiro 
def adiciona_peca(tabuleiro, pecas, peca_selecionada):
    posicao_x=random.randint(0, 9)
    posicao_y=0
    for l in range(len(peca_selecionada)):
        for c in range(len(peca_selecionada[l])):
            if peca_selecionada[l][c]=='1':
                tabuleiro[posicao_y+l][posicao_x+c]='1'

#Função que mostra o tabuleiro
def mostra_tabuleiro(n_linhas, n_colunas, tabuleiro):
    for l in range(n_linhas):
        for c in range(n_colunas):
            print(tabuleiro[l][c], end=' ')
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
    tabuleiro=inicia_tabuleiro(20, 10)
    pecas=inicia_pecas()
    while True:
        peca_selecionada=escolhe_peca(pecas)
        adiciona_peca(tabuleiro, pecas, peca_selecionada)
        mostra_tabuleiro(20, 10, tabuleiro)
        #limpa_terminal()
        break

#Chamada da função principal do programa
main()
