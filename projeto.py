# Trabalho 1 de Algoritmos Avancados
# Sabrina Faceroli - 9066452
# Joao Gabriel Fontana - 

# THE AMAZING AND MOST AWESOME PYTHON FUTOSHIKI EVER!
# -----------------------------------------------------

# Leitura dos dados
casosdeteste = int(input())
#casosdeteste = int(casosdeteste)

tamanhoJogo, qtsRestr = raw_input().split(" ")
tamanhoJogo = int(tamanhoJogo) #passando pra int
qtsRestr = int(qtsRestr)

# Definindo a matriz do jogo
jogo = [[0 for a in range(tamanhoJogo)] for b in range(tamanhoJogo)]

# Definindo a matriz de restricoes
restricoes =  [[0 for a in range(4)] for b in range(qtsRestr)]

# Lendo as linhas do jogo
for x in range(0, tamanhoJogo):
    i = 0 
    for a in raw_input().split(" "):
        jogo[x][i] = a
        i += 1

# Lendo as restricoes
for x in range(0, qtsRestr):
    i = 0
    for a in raw_input().split(" "):
        restricoes[x][i] = a
        i += 1


# FUNCAO PARA TESTE DE RESTRICOES
# Dado um ponto (x, y) ele checa se existem restricoes para esse ponto
def obedeceRestricoes(x, y):
    for z in range(0, qtsRestr):
        print "entrei aqui" + str(z)
        print restricoes[z][0] + str(x)
        print restricoes[z][1] + str(y)
        if (restricoes[z][0] == x and restricoes[z][1] == y) or (restricoes[z][2] == x and restricoes[z][3] == y):
            if (jogo[restricoes[z][0]][restricoes[z][1]] < jogo[restricoes[z][2]][restricoes[z][3]]):
                return 1
            else: 
                return 0
        else:
            print "ENTRA NESSA MERDA PELO AMOR DE JESUS!"
        

print restricoes[0]
print jogo[0]
print jogo[1]
print jogo[2]
print obedeceRestricoes(0, 0)
