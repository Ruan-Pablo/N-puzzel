import random
from collections import deque
from queue import Queue


def getPosicaoPecaVazia(tabuleiro):
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro)):
            if tabuleiro[linha][coluna] == 0:
                return linha, coluna

def ehObjetivo(tabuleiro):
    tamanho = len(tabuleiro)
    estado_meta = []
    for linha in range(tamanho):
        linha_meta = []
        for coluna in range(tamanho):
            valor = linha * tamanho + coluna + 1
            if valor == tamanho * tamanho:
                valor = 0
            linha_meta.append(valor)
        estado_meta.append(linha_meta)
    return estado_meta == tabuleiro

def printarTabuleiro(tabuleiro):
    for i in tabuleiro:
        print(i)

class Tabuleiro:
    def __init__(self) -> None:
        self.tabuleiro = None
        self.estado_meta = None

    def setTabuleiro(self, tabuleiro):
        self.tabuleiro = tabuleiro
    def getTabuleiro(self):
        return self.tabuleiro

    def printarTabuleiro(self):
        for i in self.tabuleiro:
            print(i)
    
    def clonarTabuleiro(self):
        nova_matriz = []
        for row in self.tabuleiro:
            nova_matriz.append(row[:])
        return nova_matriz

    def subir(self):
        pos_zero = getPosicaoPecaVazia(self.tabuleiro)
        tabuleiro = self.clonarTabuleiro()
        if pos_zero[0] > 0:
            aux = tabuleiro[pos_zero[0] - 1][pos_zero[1]] 
            tabuleiro[pos_zero[0]][pos_zero[1]] = aux
            tabuleiro[pos_zero[0] - 1][pos_zero[1]] = 0
            self.tabuleiro = tabuleiro

            return tabuleiro
        
    def descer(self):
        pos_zero = getPosicaoPecaVazia(self.tabuleiro)
        tabuleiro = self.clonarTabuleiro()
        if pos_zero[0] < (len(self.tabuleiro) - 1):
            aux = tabuleiro[pos_zero[0] + 1][pos_zero[1]] 
            tabuleiro[pos_zero[0]][pos_zero[1]] = aux
            tabuleiro[pos_zero[0] + 1][pos_zero[1]] = 0
            self.tabuleiro = tabuleiro

            return tabuleiro
            
    def direitar(self):
        pos_zero = getPosicaoPecaVazia(self.tabuleiro)
        tabuleiro = self.clonarTabuleiro()
        if pos_zero[1] < (len(self.tabuleiro) - 1):
            aux = tabuleiro[pos_zero[0]][pos_zero[1] + 1] 
            tabuleiro[pos_zero[0]][pos_zero[1]] = aux
            tabuleiro[pos_zero[0]][pos_zero[1] + 1] = 0
            self.tabuleiro = tabuleiro

            return tabuleiro
            # print(getPosicaoPecaVazia(self.tabuleiro))

    def esquerdar(self):
        pos_zero = getPosicaoPecaVazia(self.tabuleiro)
        tabuleiro = self.clonarTabuleiro()
        if pos_zero[1] > 0:
            aux = tabuleiro[pos_zero[0]][pos_zero[1] - 1] 
            tabuleiro[pos_zero[0]][pos_zero[1]] = aux
            tabuleiro[pos_zero[0]][pos_zero[1] - 1] = 0
            self.tabuleiro = tabuleiro

            return tabuleiro

    def movimentoAleatorio(self):
        tabuleiro = []
        pos_zero = getPosicaoPecaVazia(self.tabuleiro)
        if pos_zero[0] > 0:
            tabuleiro.append(self.subir())
            # print('subi')
        if pos_zero[0] < (len(self.tabuleiro) - 1):
            tabuleiro.append(self.descer())
            # print('desci')

        if pos_zero[1] > 0:
            tabuleiro.append(self.esquerdar())
            # print('esq')

        if pos_zero[1] < (len(self.tabuleiro) - 1):
            tabuleiro.append(self.direitar())
            # print('dir')

        return tabuleiro

    def criar_tabuleiro(self, tamanho_matriz: int):
        self.estado_meta = self.criarEstadoMeta(tamanho_matriz)
        self.tabuleiro = self.estado_meta
        for i in range(100):
            ale = random.randint(1, 4)
            pos_zero = getPosicaoPecaVazia(self.tabuleiro)
            if ale == 1 and pos_zero[0] > 0:
                self.subir()
            if ale == 2 and (pos_zero[0] < (tamanho_matriz - 1)):
                self.descer()
            if ale == 3 and (pos_zero[1] < (tamanho_matriz - 1)):
                self.direitar()
            if ale == 4 and pos_zero[1] > 0:
                self.esquerdar()
        self.printarTabuleiro()
    
    def ehObjetivo(self, tabuleiro):
        return self.estado_meta == tabuleiro
    
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


class No:
    def __init__(self):
        self.tabuleiro = None
        self.pai = None

    def setTabuleiro(self, tabuleiro: Tabuleiro):
        self.tabuleiro = tabuleiro
    def getTabuleiro(self):
        return self.tabuleiro
    
    def clonarTabuleiro(self):
        nova_matriz = []
        for row in self.tabuleiro:
            nova_matriz.append(row[:])
        return nova_matriz

    def setPai(self, pai):
        self.pai = pai

    def getPai(self):
        return self.pai

    def movimentosPossiveis(self):
        movimentos = []
        linha, coluna = getPosicaoPecaVazia(self.tabuleiro)
        tamanho_tabuleiro = len(self.tabuleiro)
        # Movimento para cima
        if linha > 0:
            vNo = No()
            vNo.setPai(self)
            vNo.setTabuleiro(self.clonarTabuleiro())
            aux = vNo.getTabuleiro()[linha - 1][coluna]
            vNo.getTabuleiro()[linha - 1][coluna] = 0
            vNo.getTabuleiro()[linha][coluna] = aux
            movimentos.append(vNo)

        # Movimento para baixo
        if linha < (tamanho_tabuleiro - 1):
            vNo = No()
            vNo.setPai(self)
            vNo.setTabuleiro(self.clonarTabuleiro())
            aux = vNo.getTabuleiro()[linha + 1][coluna]
            vNo.getTabuleiro()[linha + 1][coluna] = 0
            vNo.getTabuleiro()[linha][coluna] = aux
            movimentos.append(vNo)

        # Movimento para esquerda
        if coluna > 0:
            vNo = No()
            vNo.setPai(self)
            vNo.setTabuleiro(self.clonarTabuleiro())
            aux = vNo.getTabuleiro()[linha][coluna - 1]
            vNo.getTabuleiro()[linha][coluna - 1] = 0
            vNo.getTabuleiro()[linha][coluna] = aux
            movimentos.append(vNo)

        # Movimento para direita
        if coluna < (tamanho_tabuleiro - 1):
            vNo = No()
            vNo.setPai(self)
            vNo.setTabuleiro(self.clonarTabuleiro())
            aux = vNo.getTabuleiro()[linha][coluna + 1]
            vNo.getTabuleiro()[linha][coluna + 1] = 0
            vNo.getTabuleiro()[linha][coluna] = aux
            movimentos.append(vNo)
        # print(movimentos)
        return movimentos

    def getPosicaoPecaVazia(self):
        for linha in range(len(self.tabuleiro)):
            for coluna in range(len(self.tabuleiro)):
                if self.tabuleiro[linha][coluna] == 0:
                    return linha, coluna

    def exibirMovimentos(self, movimentos:list):
        for obj in movimentos:
            print(obj.tabuleiro)
    
    def passos(self):
        current = self
        passos = [current]
        
        while current.pai is not None:
            # print(current.pai.tabuleiro)
            current = current.pai
            passos.append(current)
        
        passos.reverse()
        return passos


    # def caminhoDasPecas(self, no):
    #     pass  # Implemente conforme necessário

class BuscaEmLargura:
    def busca_em_largura(estado_inicial):
        fila: Queue[No] = deque()
        visitados = set()

        # Adiciona o estado inicial à fila
        fila.append(estado_inicial)
        while fila:
            estado_atual = fila.popleft()

            if ehObjetivo(estado_atual.getTabuleiro()):
                print('fim da busca')
                
                return estado_atual.passos()

            visitados.add(estado_atual)
            movimentos = estado_atual.movimentosPossiveis()

            # Para cada movimento possível, verifica se já foi visitado e, caso contrário, adiciona à fila
            for movimento in movimentos:
                if movimento not in visitados:
                    # print(movimento.pai.tabuleiro)
                    fila.append(movimento)

        
        return None  # Nenhum estado objetivo encontrado

# Exemplo de uso
# estado_inicial = ...
# estado_objetivo = busca_em_largura(estado_inicial)

tabuleiro = Tabuleiro()
tabuleiro.criar_tabuleiro(3)

puzzel = No()
puzzel.setTabuleiro(tabuleiro.getTabuleiro())

final = BuscaEmLargura.busca_em_largura(puzzel)
for i, state in enumerate(final):
        print('-' * 10 + f' Passo {i} ' + '-' * 10)
        printarTabuleiro(state.tabuleiro)