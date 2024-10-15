#Importação de Bibliotecas
import os, time, random

#Declaração de Variáveis Globais
n_linhas = 20
n_colunas = 10

#Inicialização do Tabuleiro
tabuleiro = [['⬛' for _ in range(n_colunas)] for _ in range(n_linhas)]

#Inicialização das Peças
pecas = [
    ['1', '1', '1', '1'],
    [['1', '1'], ['1', '1']],
    [['1', '1', '1'], ['0', '1', '0']],
    [['0', '1', '1'], ['1', '1', '0']],
    [['1', '1', '0'], ['0', '1', '1']],
    [['1', '0', '0'], ['1', '1', '1']],
    [['0', '0', '1'], ['1', '1', '1']]
]

#Função que Mostra o Tabuleiro no Terminal
def mostra_tabuleiro():
    for l in range(n_linhas):
        for c in range(n_colunas):
            print(tabuleiro[l][c], end=' ')
        print()
    time.sleep(0.1)

#Função que Adiciona uma Peça
def adiciona_peca(peca, py, px):
    for l in range(len(peca)):
        for c in range(len(peca[0])):
            if peca[l][c] == '1':
                tabuleiro[py + l][px + c] = '🟦'

#Função que Limpa a Posição Anterior da Peça
def limpa_peca(peca, py, px):
    for l in range(len(peca)):
        for c in range(len(peca[0])):
            if peca[l][c] == '1':
                tabuleiro[py + l][px + c] = '⬛'

#Função que Verifica a Colisão da Peça
def verifica_colisao(peca, py, px):
    for l in range(len(peca)):
        for c in range(len(peca[0])):
            if peca[l][c] == '1':
                if py + l >= n_linhas or tabuleiro[py + l][px + c] == '🟦':
                    return True
    return False

#Função que Limpa o Terminal
def limpa_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Função Principal
def main():
    while True:
        peca = random.choice(pecas)
        posicao_y = 0
        posicao_x = random.randint(0, n_colunas - len(peca[0]))
        adiciona_peca(peca, posicao_y, posicao_x)
        while True:
            mostra_tabuleiro()
            limpa_peca(peca, posicao_y, posicao_x)
            if not verifica_colisao(peca, posicao_y + 1, posicao_x):
                posicao_y += 1
            else:
                adiciona_peca(peca, posicao_y, posicao_x)
                break
            limpa_terminal()
            adiciona_peca(peca, posicao_y, posicao_x)

#Chamada da Função Principal
main()
