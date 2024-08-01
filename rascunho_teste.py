
import random

class Tabuleiro:
    def __init__(self) -> None:
        self.tabuleiro = None
        self.estado_meta = None

    def printarTabuleiro(self, tabuleiro):
        for i in tabuleiro:
            print(i)
    
    def clonarTabuleiro(self):
        nova_matriz = []
        for row in self.tabuleiro:
            nova_matriz.append(row[:])
        return nova_matriz
        
    def getPosicaoPecaVazia(self):
        for linha in range(len(self.tabuleiro)):
            for coluna in range(len(self.tabuleiro)):
                if self.tabuleiro[linha][coluna] == 0:
                    return linha, coluna
                
    def subir(self):
        pos_zero = self.getPosicaoPecaVazia()
        if pos_zero[0] > 0:
            tabuleiro = self.clonarTabuleiro()
            aux = tabuleiro[pos_zero[0] - 1][pos_zero[1]] 
            tabuleiro[pos_zero[0]][pos_zero[1]] = aux
            tabuleiro[pos_zero[0] - 1][pos_zero[1]] = 0

            return tabuleiro
        
    def descer(self):
        pos_zero = self.getPosicaoPecaVazia()
        if pos_zero[0] < (len(self.tabuleiro) - 1):
            tabuleiro = self.clonarTabuleiro()
            aux = tabuleiro[pos_zero[0] + 1][pos_zero[1]] 
            tabuleiro[pos_zero[0]][pos_zero[1]] = aux
            tabuleiro[pos_zero[0] + 1][pos_zero[1]] = 0

            return tabuleiro
            
    def direitar(self):
        pos_zero = self.getPosicaoPecaVazia()
        if pos_zero[1] < (len(self.tabuleiro) - 1):
            tabuleiro = self.clonarTabuleiro()
            aux = tabuleiro[pos_zero[0]][pos_zero[1] + 1] 
            tabuleiro[pos_zero[0]][pos_zero[1]] = aux
            tabuleiro[pos_zero[0]][pos_zero[1] + 1] = 0

            return tabuleiro


    def esquerdar(self):
        pos_zero = self.getPosicaoPecaVazia()
        if pos_zero[1] > 0:
            tabuleiro = self.clonarTabuleiro()
            aux = tabuleiro[pos_zero[0]][pos_zero[1] - 1] 
            tabuleiro[pos_zero[0]][pos_zero[1]] = aux
            tabuleiro[pos_zero[0]][pos_zero[1] - 1] = 0

            return tabuleiro

    def criarTabuleiro(self, tamanho_matriz: int):
        self.criarEstadoMeta(tamanho_matriz)
        self.tabuleiro = self.estado_meta
        for i in range(10000):
            ale = random.randint(1, 4)
            pos_zero = self.getPosicaoPecaVazia()
            if ale == 1 and pos_zero[0] > 0:
                self.tabuleiro = self.subir()
            if ale == 2 and (pos_zero[0] < (tamanho_matriz - 1)):
                self.tabuleiro = self.descer()
            if ale == 3 and (pos_zero[1] < (tamanho_matriz - 1)):
                self.tabuleiro = self.direitar()
            if ale == 4 and pos_zero[1] > 0:
                self.tabuleiro = self.esquerdar()
    
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
        self.estado_meta = estado_meta


class No(Tabuleiro):
    def __init__(self):
        self.pai = None

    def movimentosPossiveis(self):
        movimentos = []
        linha, coluna = self.getPosicaoPecaVazia()
        tamanho_tabuleiro = len(self.tabuleiro)
        # Movimento para cima
        if linha > 0:
            nNo = No()
            nNo.pai = self
            nNo.estado_meta = self.estado_meta
            nNo.tabuleiro = self.subir()
            movimentos.append(nNo)

        # Movimento para baixo
        if linha < (tamanho_tabuleiro - 1):
            nNo = No()
            nNo.estado_meta = self.estado_meta
            nNo.pai = self
            nNo.tabuleiro = self.descer()
            movimentos.append(nNo)

        # Movimento para esquerda
        if coluna > 0:
            nNo = No()
            nNo.pai = self
            nNo.estado_meta = self.estado_meta
            nNo.tabuleiro = self.esquerdar()
            movimentos.append(nNo)

        # Movimento para direita
        if coluna < (tamanho_tabuleiro - 1):
            nNo = No()
            nNo.pai = self
            nNo.estado_meta = self.estado_meta
            nNo.tabuleiro = self.direitar()
            movimentos.append(nNo)
        return movimentos
    
    def passos(self):
        atual = self
        passos = [atual]
        
        while atual.pai is not None:
            atual = atual.pai
            passos.append(atual)
        
        passos.reverse()
        return passos



puzzel = No()
puzzel.criarTabuleiro(3)

p = tuple(map(tuple, puzzel.tabuleiro))
tabu_tupla = tuple(map(tuple, [[1,2,3],[4,5,6],[7,8,0]]))

meta = [[1,2,3],[4,5,6],[7,8,0]]
control = [[1,2,3],[4,5,0],[7,8,6]]

dic = {}
nome = 'bfs'
valor = ('met','passo')
dic[nome] = valor
print(dic)


def getPosicaoMeta(estado_meta, valor):
    for linha in range(len(estado_meta)):
        for coluna in range(len(estado_meta)):
            if estado_meta[linha][coluna] == valor:
                return linha, coluna

def marahtan(estado, meta):
    distancia = 0
    
    for x1 in range(len(estado)):
        for y1 in range(len(estado)):
            valor = estado[x1][y1]
            if valor == 0:
                continue
            
            x2, y2 = getPosicaoMeta(meta, valor)
            
            distancia += abs(x1 - x2) + abs(y1 - y2)
    return distancia     

# print(marahtan(puzzel.tabuleiro, t))