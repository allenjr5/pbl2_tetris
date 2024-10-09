#Importação de bibliotecas que serão utilizadas no código
import os
import time
import random

#Declaração de variáveis que serão utilizadas com frequência no código
n_linhas=20
n_colunas=10

#Inicialização da matriz do tabuleiro
tabuleiro=[]
for l in range(n_linhas):
    linha=[]
    for c in range(n_colunas):
        linha.append('⬛')
    tabuleiro.append(linha)

#Inicialização das matrizes das peças em forma de dicionário
pecas={
    'I': ['1', '1', '1', '1'],
    'O': [['1', '1'], ['1', '1']],
    'T': [['1', '1', '1'], ['0', '1', '0']],
    'S': [['0', '1', '1'], ['1', '1', '0']],
    'Z': [['1', '1', '0'], ['0', '1', '1']],
    'J': [['1', '0', '0'], ['1', '1', '1']],
    'L': [['0', '0', '1'], ['1', '1', '1']]
}

#Função que mostra o tabuleiro no terminal
def mostra_tabuleiro():
    for l in range(n_linhas):
        for c in range(n_colunas):
            print(tabuleiro[l][c], end=' ')
        print()
    time.sleep(1)

#Função que adiciona uma peça no tabuleiro e move automaticamente para baixo
def adiciona_peca(peca, py, px):
    for l in range(len(peca)):
        for c in range(len(peca[l])):
            if peca[l][c]=='1':
                tabuleiro[l+py][c+px]='🟦'

#Função que limpa a posição anterior da peça no tabuleiro
def limpa_peca(peca, py, px):
    for l in range(len(peca)):
        for c in range(len(peca[l])):
            if peca[l][c]=='1':
                tabuleiro[l+py][c+px]='⬛'

#Função que limpa o terminal
def limpa_terminal():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

#Função principal do programa
def main():
    while True:
        peca=random.choice(list(pecas.values()))
        posicao_y=0
        posicao_x=random.randint(0, 9 - len(peca[0]))
        while True:
            adiciona_peca(peca, posicao_y, posicao_x)
            mostra_tabuleiro()
            limpa_peca(peca, posicao_y, posicao_x)
            posicao_y+=1
            limpa_terminal()

#Chamada da função principal do programa
main()
