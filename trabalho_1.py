import random
from collections import deque


class Tabuleiro:
    def __init__(self, tamanho_matriz) -> list:    
        numeros = list(range(1, tamanho_matriz**2)) # Gera uma lista com os números de 1 a n^2 - 1
        numeros.append(0) # Adiciona o espaço vazio representado por 0
        random.shuffle(numeros) # Embaralha os números
        tabuleiro = []
        for i in range(0, tamanho_matriz**2, tamanho_matriz): # Divide a lista em sublistas para representar as linhas do tabuleiro
            linha = numeros[i:i+tamanho_matriz]
            tabuleiro.append(linha)
        return tabuleiro  # Implemente a classe Tabuleiro conforme necessário
    
    def ehObjetivo(self, tabuleiro:list):
        tamanho = len(tabuleiro)
        matriz_meta = []
        for linha in range(tamanho):
            linha_meta = []
            for coluna in range(tamanho):
                valor = linha * tamanho + coluna + 1
                if valor == tamanho * tamanho:
                    valor = 0
                linha_meta.append(valor)
            matriz_meta.append(linha_meta)

        return matriz_meta
    
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
    
    def clonarTabuleiro(self, tabuleiro):
        return tabuleiro[:]

    def setPai(self, pai):
        self.pai = pai

    def getPai(self):
        return self.pai

    def movimentosPossiveis(self):
        movimentos = []
        linha, coluna = self.getPosicaoPecaVazia()

        # Movimento para cima
        if linha > 0:
            vNo = No()
            vNo.setPai(self)
            vNo.setTabuleiro([row[:] for row in self.tabuleiro])
            aux = vNo.getTabuleiro()[linha - 1][coluna]
            vNo.getTabuleiro()[linha - 1][coluna] = 0
            vNo.getTabuleiro()[linha][coluna] = aux
            movimentos.append(vNo)

        # Movimento para baixo
        if linha < 2:
            vNo = No()
            vNo.setPai(self)
            vNo.setTabuleiro([row[:] for row in self.tabuleiro])
            aux = vNo.getTabuleiro()[linha + 1][coluna]
            vNo.getTabuleiro()[linha + 1][coluna] = 0
            vNo.getTabuleiro()[linha][coluna] = aux
            movimentos.append(vNo)

        # Movimento para esquerda
        if coluna > 0:
            vNo = No()
            vNo.setPai(self)
            vNo.setTabuleiro([row[:] for row in self.tabuleiro])
            aux = vNo.getTabuleiro()[linha][coluna - 1]
            vNo.getTabuleiro()[linha][coluna - 1] = 0
            vNo.getTabuleiro()[linha][coluna] = aux
            movimentos.append(vNo)

        # Movimento para direita
        if coluna < 2:
            vNo = No()
            vNo.setPai(self)
            vNo.setTabuleiro([row[:] for row in self.tabuleiro])
            aux = vNo.getTabuleiro()[linha][coluna + 1]
            vNo.getTabuleiro()[linha][coluna + 1] = 0
            vNo.getTabuleiro()[linha][coluna] = aux
            movimentos.append(vNo)
        return movimentos

    def getPosicaoPecaVazia(self):
        for linha in range(3):
            for coluna in range(3):
                if self.tabuleiro.m[linha][coluna] == 0:
                    return linha, coluna

    # def representacaoDoTabuleiro(self):
    #     pass  # Implemente conforme necessário

    # def exibirMovimentos(self):
    #     pass  # Implemente conforme necessário

    # def caminhoDasPecas(self, no):
    #     pass  # Implemente conforme necessário

class BuscaEmLargura:
    def busca_em_largura(estado_inicial):
        fila = deque()
        visitados = set()

        # Adiciona o estado inicial à fila
        fila.append(estado_inicial)

        while fila:
            # Remove o próximo estado da fila
            estado_atual = fila.popleft()

            # Verifica se o estado atual é o objetivo
            if Tabuleiro.ehObjetivo(estado_atual):
                return estado_atual

            # Adiciona o estado atual aos visitados
            visitados.add(estado_atual)

            # Obtém os movimentos possíveis a partir do estado atual
            movimentos = estado_atual.movimentosPossiveis()

            # Para cada movimento possível, verifica se já foi visitado e, caso contrário, adiciona à fila
            for movimento in movimentos:
                if movimento not in visitados and movimento not in fila:
                    fila.append(movimento)

        return None  # Nenhum estado objetivo encontrado

    # Exemplo de uso
    # estado_inicial = ...
    # estado_objetivo = busca_em_largura(estado_inicial)
