import random
def criar_matriz_objetivo(tamanho):
    matriz_objetivo = []

    for linha in range(tamanho):
        linha_objetivo = []
        for coluna in range(tamanho):
            valor = linha * tamanho + coluna + 1
            if valor == tamanho * tamanho:
                valor = 0
            linha_objetivo.append(valor)
        matriz_objetivo.append(linha_objetivo)

    return matriz_objetivo

def getPosicaoPecaVazia(tabuleiro):
    for linha in range(len(tabuleiro)):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == 0:
                return linha, coluna

class Tabuleiro:
    def __init__(self) -> None:
        self.tabuleiro = None

    def setTabuleiro(self, tabuleiro):
        self.tabuleiro = tabuleiro
    def getTabuleiro(self):
        return self.tabuleiro

    def printarTabuleiro(self):
        for i in self.tabuleiro:
            print(i)
    
    def subir(self):
        pos_zero = getPosicaoPecaVazia(self.tabuleiro)
        # print(pos_zero)
        if pos_zero[0] > 0:
            aux = self.tabuleiro[pos_zero[0] - 1][pos_zero[1]] 
            self.tabuleiro[pos_zero[0]][pos_zero[1]] = aux
            self.tabuleiro[pos_zero[0] - 1][pos_zero[1]] = 0
        
    def descer(self):
        pos_zero = getPosicaoPecaVazia(self.tabuleiro)
        # print(pos_zero)
        if pos_zero[0] < (len(self.tabuleiro) - 1):
            aux = self.tabuleiro[pos_zero[0] + 1][pos_zero[1]] 
            self.tabuleiro[pos_zero[0]][pos_zero[1]] = aux
            self.tabuleiro[pos_zero[0] + 1][pos_zero[1]] = 0
            
    def direitar(self):
        pos_zero = getPosicaoPecaVazia(self.tabuleiro)
        # print(pos_zero)
        if pos_zero[1] < (len(self.tabuleiro) - 1):
            aux = self.tabuleiro[pos_zero[0]][pos_zero[1] + 1] 
            self.tabuleiro[pos_zero[0]][pos_zero[1]] = aux
            self.tabuleiro[pos_zero[0]][pos_zero[1] + 1] = 0
            # print(getPosicaoPecaVazia(self.tabuleiro))

    def esquerdar(self):
        pos_zero = getPosicaoPecaVazia(self.tabuleiro)
        # print(pos_zero)
        if pos_zero[1] > 0:
            aux = self.tabuleiro[pos_zero[0]][pos_zero[1] - 1] 
            self.tabuleiro[pos_zero[0]][pos_zero[1]] = aux
            self.tabuleiro[pos_zero[0]][pos_zero[1] - 1] = 0


    def criar_tabuleiro(self, tamanho_matriz: int):    
        estado_meta = self.criarEstadoMeta(tamanho_matriz)
        self.tabuleiro = estado_meta
        # self.printarTabuleiro()
        # print("--------- depois ----------")
        # self.esquerda()
        # self.printarTabuleiro()
        for i in range(100):
            ale = random.randint(0, 4)
            if ale == 1:
                self.subir()
                # self.printarTabuleiro()
            if ale == 2:
                self.descer()
                # self.printarTabuleiro()
            if ale == 3:
                self.direitar()
                # self.printarTabuleiro()
            if ale == 4:
                self.esquerdar()
                # self.printarTabuleiro()
            # print('-----------')
        self.printarTabuleiro()
        # self.tabuleiro = tabuleiro[:]
    
    def ehObjetivo(self, tabuleiro:list): # ajeitar pq tem codigo repetido
        tamanho = len(tabuleiro)
        matriz_meta = []
        for linha in range(tamanho):
            linha_meta = []
            for coluna in range(tamanho):
                valor = linha * tamanho + coluna + 1
                if ale == valor == tamanho * tamanho:
                    valor = 0
                linha_meta.append(valor)
            matriz_meta.append(linha_meta)

        return matriz_meta == tabuleiro
    
    def criarEstadoMeta(self, tamanho):
        estado_meta = []

        for linha in range(tamanho):
            linha_meta = []
            for coluna in range(tamanho):
                valor = linha * tamanho + coluna + 1
                if valor == tamanho * tamanho:
                    valor = 0
                linha_meta.append(valor)
            estado_meta.append(linha_meta)

        return estado_meta


# Exemplo de uso
tabuleiro = Tabuleiro()
matriz_objetivo = tabuleiro.criar_tabuleiro(3)

