# Trabalho 1 de Algoritmos Avancados
# Sabrina Faceroli - 9066452
# Joao Gabriel Fontana - 7979144 

# THE AMAZING AND MOST AWESOME PYTHON FUTOSHIKI EVER!
# -----------------------------------------------------

import time

# Estruturas necessarias
casosdeteste = int(input())
variaveisNaoAtribuidas = [] # Vetor de pontos, ou seja, v = {1, 2, 3, 4} seriam os pontos (1, 2) e (3, 4)
dominioInicial = []
verificacaoAdianteFlag = 1 # 1 - Verifica adiante; 0 - Nao verifica
MVRFlag = 1 # 1 - Nao usa MVR; 2 - Usa MVR

# -----------------------------------------------------
# FUNCAO PARA TESTE DE RESTRICOES
# Dado um ponto (x, y) ele checa se existem restricoes para esse ponto
def obedeceRestricoes(x, y):
    for z in range(0, qtsRestr):
        if (restricoes[z][0] == x and restricoes[z][1] == y) or (restricoes[z][2] == x and restricoes[z][3] == y):
            if (jogo[restricoes[z][0]][restricoes[z][1]] < jogo[restricoes[z][2]][restricoes[z][3]]) or (jogo[restricoes[z][0]][restricoes[z][1]] == 0 or jogo[restricoes[z][2]][restricoes[z][3]] == 0):
                return 1
            else: 
                return 0
    return 1

# FUNCAO BACKTRACKING
# variaveisNaoAtribuidas precisa ser reinstanciada para nao conflitar ao rodar os n casos de teste
def backtracking():
    global variaveisNaoAtribuidas
    variaveisNaoAtribuidas = []

    defineVariaveis(MVRFlag) # Sem poda pra testar
    variaveisNaoAtribuidas.reverse()
    x = variaveisNaoAtribuidas.pop()
    y = variaveisNaoAtribuidas.pop()
    ini = time.time()
    j = recursiveBacktracking(x, y)
    fim = time.time()
    for a in range(0, tamanhoJogo):
        for b in range(0, tamanhoJogo):
            print str(jogo[a][b]),
        print ""
    print "Tempo de execucao: " + str(fim-ini) + " segundos."
    
    if j == -1:
        print "***** NUMERO DE ATRIBUICOES EXCEDEU LIMITE MAXIMO *********"
    else:
        print "Numero de atribuicoes: " + str(atribuicao)  

# FUNCAO RECURSIVEBACKTRACKING
# Pode retornar 3 valores:
#       0 - Em caso de falha / atribuicao nao permitida
#       1 - Bem sucedido
#      -1 - Estourou limite de atribuicoes
# Para testar o fim do jogo, eu adiciono um ponto (x,y) que nao existe (tamanho + 1) e quando o programa atinge isso, sabe que o jogo terminou
# Empiricamente essa foi uma boa forma de terminar o jogo sem ter que checar a todo momento a matriz, o que eh custoso
def recursiveBacktracking(x, y):
    global atribuicao
    
    if x == (tamanhoJogo + 1):
        return 1
    
    if atribuicao > 1000000:
        return -1
   
    dominios = defineDominios(x, y)

    for d in dominios:
        jogo[x][y] = d
        atribuicao = atribuicao + 1
        if obedeceRestricoes(x, y) == 1:
            if verificacaoAdianteFlag == 1:
                v = verificacaoAdiante()
                if v == 0:
                    jogo[x][y] = 0
                    return 0

            a = variaveisNaoAtribuidas.pop()
            b = variaveisNaoAtribuidas.pop()
            
            j = recursiveBacktracking(a, b)
            if j == 1:
                return 1
            elif j == 0:
                variaveisNaoAtribuidas.append(b)
                variaveisNaoAtribuidas.append(a)
            elif j == -1:
                return -1
        
        jogo[x][y] = 0

    return 0

# FUNCAO DEFINEVARIAVEIS
# Essa funcao define a ordem de variaves a receberem dominios.
# Em caso sem poda, simplesmente adiciona os pontos na ordem original da matriz
# Em caso de MVR, a solucao que achei mais interessante foi a de adicionar os pontos que possuem restricoes primeiro, porem isso soh faz sentido
#   se eu adicionar a sua linha e sua coluna pra checagem tambem, pois a restricao de uma casinha eh em RELACAO a outra casinha de sua linha ou coluna,
#   portanto, ele adiciona o ponto de restricao na ordem da matriz de restricoes e adiciona logo em seguida sua linha e coluna, apos fazer isso com todas
#       as restricoes, adiciona o resto da matriz na ordem comum.
def defineVariaveis(heuristica):
    if heuristica == 1: # Sem poda
        for a in range(0, tamanhoJogo):
            for b in range(0, tamanhoJogo):
                if jogo[a][b] == 0:
                    variaveisNaoAtribuidas.append(a)
                    variaveisNaoAtribuidas.append(b)
       
    if heuristica == 2: # Com MVR - verifica qual variavel possui mais restricoes, a adiciona, e depois adiciona sua linha e coluna em seguida
        for a in range (0, qtsRestr):
            if jogo[restricoes[a][0]][restricoes[a][1]] == 0:
                variaveisNaoAtribuidas.append(restricoes[a][0])
                variaveisNaoAtribuidas.append(restricoes[a][1])
                jogo[restricoes[a][0]][restricoes[a][1]] = -1    # -1 pq ela ja foi adicionada, pq se ficar 0 ele vai adicionar de novo
                for b in range (0, tamanhoJogo):
                    if jogo[restricoes[a][0]][b] == 0:
                        variaveisNaoAtribuidas.append(restricoes[a][0])
                        variaveisNaoAtribuidas.append(b)
                        jogo[restricoes[a][0]][b] = -1

                    if jogo[b][restricoes[a][1]] == 0:
                        variaveisNaoAtribuidas.append(b)
                        variaveisNaoAtribuidas.append(restricoes[a][1])
                        jogo[b][restricoes[a][1]] = -1
        
        for a in range (0, tamanhoJogo):
            for b in range (0, tamanhoJogo):
                if jogo[a][b] == 0:
                    variaveisNaoAtribuidas.append(a)
                    variaveisNaoAtribuidas.append(b)
                elif jogo[a][b] == -1:  # Agora que ja foi adicionada, limpa o -1
                    jogo[a][b] = 0

    variaveisNaoAtribuidas.append(tamanhoJogo + 1)
    variaveisNaoAtribuidas.append(tamanhoJogo + 1)
        

# FUNCAO VERIFICACAOADIANTE
# A funcao verifica os dominios possiveis para todas as variaveis na ordem de sua atribuicao, assim que encontra uma falta de dominios
#   em determinada variavel, retorna o erro para entao o recursiveBacktracking voltar e reatribuir variaveis antigas
def verificacaoAdiante():
    for a in range (((len(variaveisNaoAtribuidas)/2) - 1), 0):
        for b in range ((len(variaveisNaoAtribuidas)/2), 1):
            if variaveisNaoAtribuidas[a] == (tamanhoJogo + 1):
                return 1

            dominios = defineDominios(variaveisNaoAtribuidas[a], variaveisNaoAtribuidas[b])
            if len(dominios) == 0:
                return 0
    return 1

# FUNCAO DEFINEDOMINIOS
# Usando um vetor dominioInicial que esta instanciado com os valores possiveis para o jogo (por exemplo, se eh uma matriz 4 -> {1, 2, 3, 4}) ele checa
#   quais dos valores possiveis para o jogo podem ser atribuidos a variavel.
# Retorna os dominios possiveis para a variavel (x, y)
def defineDominios(x, y):    
    dominiosValidos = []
    for d in dominioInicial:
        flag = 0
        for a in range(0, tamanhoJogo):    
            if jogo[x][a] == d or jogo[a][y] == d:
                flag = -1
                a += tamanhoJogo # Para sair do laco
                
        if flag == 0:
            dominiosValidos.append(d)
    
    return dominiosValidos


# ------------------------------------------------------------------
# Jogo rodando em si (MAIN)
for j in range (0, casosdeteste):
    if j != 0:
        lixo = raw_input() # Existe um espaco entre os boards do game

    tamanhoJogo, qtsRestr = raw_input().split(" ")
    tamanhoJogo = int(tamanhoJogo)
    qtsRestr = int(qtsRestr)

    dominioInicial = []
    for a in range (0, tamanhoJogo):
        dominioInicial.append(int(a+1))

    jogo = [[0 for a in range(tamanhoJogo)] for b in range(tamanhoJogo)]
    # Lendo as linhas do jogo
    for x in range(0, tamanhoJogo):
        i = 0 
        for a in raw_input().split(" "):
            jogo[x][i] = int(a)
            i += 1

    restricoes = [[0 for a in range(4)] for b in range(qtsRestr)]
    # Lendo as restricoes
    for x in range(0, qtsRestr):
        i = 0
        for a in raw_input().split(" "):
            restricoes[x][i] = (int(a)-1)
            i += 1

    atribuicao = 0
    print str((j+1))
    backtracking() 
