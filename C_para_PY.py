import random

class No:
    def __init__(self):
        self.tabuleiro = None
        self.pai = None

    def setTabuleiro(self, tabuleiro):
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
            vNo.setTabuleiro([row[:] for row in self.tabuleiro.m])
            aux = vNo.getTabuleiro()[linha - 1][coluna]
            vNo.getTabuleiro()[linha - 1][coluna] = 0
            vNo.getTabuleiro()[linha][coluna] = aux
            movimentos.append(vNo)

        # Movimento para baixo
        if linha < 2:
            vNo = No()
            vNo.setPai(self)
            vNo.setTabuleiro([row[:] for row in self.tabuleiro.m])
            aux = vNo.getTabuleiro()[linha + 1][coluna]
            vNo.getTabuleiro()[linha + 1][coluna] = 0
            vNo.getTabuleiro()[linha][coluna] = aux
            movimentos.append(vNo)

        # Movimento para esquerda
        if coluna > 0:
            vNo = No()
            vNo.setPai(self)
            vNo.setTabuleiro([row[:] for row in self.tabuleiro.m])
            aux = vNo.getTabuleiro()[linha][coluna - 1]
            vNo.getTabuleiro()[linha][coluna - 1] = 0
            vNo.getTabuleiro()[linha][coluna] = aux
            movimentos.append(vNo)

        # Movimento para direita
        if coluna < 2:
            vNo = No()
            vNo.setPai(self)
            vNo.setTabuleiro([row[:] for row in self.tabuleiro.m])
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

    def isSolucao(self, tabuleiro:list):
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

    def representacaoDoTabuleiro(self):
        pass  # Implemente conforme necessário

    def exibirMovimentos(self):
        pass  # Implemente conforme necessário

    def caminhoDasPecas(self, no):
        pass  # Implemente conforme necessário

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

class BuscaEmLargura:
    pass