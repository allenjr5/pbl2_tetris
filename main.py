#Importação de Bibliotecas
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

#Função principal do programa
def main():
    tabuleiro=inicia_tabuleiro()
    pecas=inicia_pecas()
    while True:
        peca_escolhida=escolhe_peca(pecas)

#Chamada da funnção principal do programa
main()
