#Importação de bibliotecas que serão utilizadas no código
import os, time, random

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

#Inicialização das matrizes das peças
pecas=[
    ['1', '1', '1', '1'],
    [['1', '1'], ['1', '1']],
    [['1', '1', '1'], ['0', '1', '0']],
    [['0', '1', '1'], ['1', '1', '0']],
    [['1', '1', '0'], ['0', '1', '1']],
    [['1', '0', '0'], ['1', '1', '1']],
    [['0', '0', '1'], ['1', '1', '1']]
]

#Função que mostra o tabuleiro no terminal
def mostra_tabuleiro():
    for l in range(n_linhas):
        for c in range(n_colunas):
            print(tabuleiro[l][c], end=' ')
        print()
    time.sleep(0.3)

#Função que adiciona uma peça no tabuleiro e move automaticamente para baixo
def adiciona_peca(peca, py, px):
    for l in range(len(peca)):
        for c in range(len(peca[0])):
            if peca[l][c]=='1':
                tabuleiro[l+py][c+px]='🟦'

#Função que limpa a posição anterior da peça no tabuleiro
def limpa_peca(peca, py, px):
    for l in range(len(peca)):
        for c in range(len(peca[0])):
            if peca[l][c]=='1':
                tabuleiro[l+py][c+px]='⬛'

#Função que define a posição y máxima para cada tipo de peça
def py_max(peca):
    return 15 if len(peca)==4 else 16 if len(peca)==3 else 17

#Função que define a posição x máxima para cada tipo de peça
def px_max(peca):
    return 7 if len(peca[0])==3 else 8 if len(peca[0])==2 else 9

#Função que chaca a colisão da peça no final do tabuleiro
def checa_colisao(peca, py, py_max, px):
    return True if py<=py_max else False

#Função que limpa o terminal
def limpa_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Função principal do programa
def main():
    while True:
        peca=random.choice(pecas)
        py=0
        px=random.randint(0, px_max(peca))
        adiciona_peca(peca, py, px)
        while checa_colisao(peca, py, py_max(peca), px):
            mostra_tabuleiro()
            limpa_peca(peca, py, px)
            py+=1
            limpa_terminal()
            adiciona_peca(peca, py, px)

#Chamada da função principal do programa
main()
