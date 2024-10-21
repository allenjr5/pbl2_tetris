#Importação de bibliotecas
import os, time, random, keyboard

#Declaração de variáveis que serão utilizadas com frequência ao longo do código
n_linhas = 20
n_colunas = 10
pontuacao = 0

#Inicialização da matriz do tabuleiro
tabuleiro = [['⬛' for _ in range(n_colunas)] for _ in range(n_linhas)]

#Inicialização das matrizes das peças
pecas = [
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
    [['0', '0', '1'], ['1', '1', '1']],
    #Bomba
    ['2']
]

#Função que mostra o tabuleiro no terminal
def mostra_tabuleiro():
    for l in range(n_linhas):
        for c in range(n_colunas):
            print(tabuleiro[l][c], end=' ')
        print()
    print(f'Pontos: {pontuacao}')
    time.sleep(0.3)

#Função que adiciona a peça
def adiciona_peca(peca, py, px):
    for l in range(len(peca)):
        for c in range(len(peca[0])):
            if peca[l][c] == '1':
                tabuleiro[py + l][px + c] = '🟦'
            elif peca[l][c] == '2':
                tabuleiro[py + l][px + c] = '🟥'

#Função que limpa a posição anterior da peça
def limpa_peca(peca, py, px):
    for l in range(len(peca)):
        for c in range(len(peca[0])):
            if peca[l][c] == '1' or peca[l][c] == '2':
                tabuleiro[py + l][px + c] = '⬛'

#Função que verifica a colisão da peça
def verifica_colisao(peca, py, px):
    for l in range(len(peca)):
        for c in range(len(peca[0])):
            if peca[l][c] == '1' or peca[l][c] == '2':
                if py + l >= n_linhas or px + c < 0 or px + c >= n_colunas or tabuleiro[py + l][px + c] == '🟦':
                    return True
    return False

#Função que gira a peça
def girar_peca(peca):
    return [list(linha) for linha in zip(*peca[::-1])]

#Função que verifica se existem linhas completas e as limpa
def verifica_linhas():
    global pontuacao
    n_linhas = 0
    
    #Verifica se existem linhas completas
    linhas_completas = [i for i in range(len(tabuleiro)) if all(c == '🟦' for c in tabuleiro[i])]
    
    #Remove as linhas completas e adiciona linhas vazias no topo do tabuleiro
    for linha in linhas_completas:
        tabuleiro.pop(linha)
        tabuleiro.insert(0, ['⬛' for _ in range(n_colunas)])
        n_linhas += 1
    
    #Soma a pontuação de acordo com o número de linhas completas
    if n_linhas > 0:
        pontuacao += 100 * n_linhas

#Função que limpa a área da bomba ao colidir com outras peças
def limpa_area(px, py):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= py + i < n_linhas and 0 <= px + j < n_colunas:
                tabuleiro[py + i][px + j] = '⬛'

#Função que limpa o terminal
def limpa_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Função principal
def main():
    #Looping do jogo
    while True:

        #Escolhe uma peça aleatória
        peca = random.choice(pecas)
        
        #Define a posição y inicial da peça
        posicao_y = 0
        
        #Define a posição x inicial da peça de forma aleatória
        posicao_x = random.randint(0, n_colunas - len(peca[0]))
        adiciona_peca(peca, posicao_y, posicao_x)

        #looping das peças
        while True:
            mostra_tabuleiro()
            limpa_peca(peca, posicao_y, posicao_x)
            
            #Desce as peças automaticamente para baixo e verifica a colisão
            if not verifica_colisao(peca, posicao_y + 1, posicao_x):
                posicao_y += 1
            else:
                limpa_terminal()
                adiciona_peca(peca, posicao_y, posicao_x)
                
                #Se a peça for a bomba, chama a função que limpa a área que ela colide
                if peca == ['2']:
                    limpa_area(posicao_x, posicao_y)

                #Chamada da função que verifica se existem linhas completas no tabuleiro
                verifica_linhas()

                break
            
            #Move a peça para a esquerda ao apertar o botão 'esquerda'
            if keyboard.is_pressed('left'):
                if not verifica_colisao(peca, posicao_y, posicao_x - 1):
                    posicao_x -= 1
            
            #Move a peça para a direita ao apertar o botão 'direita'
            elif keyboard.is_pressed('right'):
                if not verifica_colisao(peca, posicao_y, posicao_x + 1):
                    posicao_x += 1
            
            #Faz com que a peça caia mais rápido ao apertar o botão 'baixo'
            elif keyboard.is_pressed('down'):
                if not verifica_colisao(peca, posicao_y + 1, posicao_x):
                    posicao_y += 1
            
            #Faz com que a peça gire ao apertar o botão 'cima'
            elif keyboard.is_pressed('up'):
                peca_girada = girar_peca(peca)
                if not verifica_colisao(peca_girada, posicao_y, posicao_x):
                    peca = peca_girada
            
            #Limpa o terminal depois que a peça colide
            limpa_terminal()
            adiciona_peca(peca, posicao_y, posicao_x)

        #Termina o jogo caso as peças cheguem ao topo do tabuleiro
        if verifica_colisao(peca, 0, posicao_x):
            print(f'Fim de Jogo! Pontuação Final: {pontuacao}')
            break

#Chama a Função Principal
main()
