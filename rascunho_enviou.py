import random
from collections import deque
import time
import sys


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
    estado_meta = tuple(map(tuple, estado_meta))
    return estado_meta == tabuleiro

def printarTabuleiro(tabuleiro):
    for i in tabuleiro:
        print(i)


class Metricas:
    def __init__(self) -> None:
        self.passos = 0
        self.inicio_tempo = 0
        self.tempo_execucao = None
        self.memoria = 0
        self.nos_expandidos = 0
        self.ciclos = 0
    
    def zerar_metricas(self):
        self.passos = 0
        self.inicio_tempo = 0
        self.tempo_execucao = None
        self.memoria = 0
        self.nos_expandidos = 0
        self.ciclos = 0

    def comecar_cronometro(self):
        self.inicio_tempo = time.time()
    def finalizar_cronometro(self):
        self.tempo_execucao = time.time() - self.inicio_tempo
    
    def atualiza_memoria(self, fila=0):
        self.memoria = max(self.memoria, sys.getsizeof(fila))

class Tabuleiro:
    def __init__(self) -> None:
        self.tabuleiro = None
        self.estado_meta = None

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
        for i in range(10000):
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
        self.estado_meta = estado_meta
        return estado_meta


class No:
    def __init__(self):
        self.tabuleiro = None
        self.estado_meta = None
        self.pai = None
 
    def clonarTabuleiro(self):
        nova_matriz = []
        for row in self.tabuleiro:
            nova_matriz.append(row[:])
        return nova_matriz


    def movimentosPossiveis(self):
        movimentos = []
        linha, coluna = getPosicaoPecaVazia(self.tabuleiro)
        tamanho_tabuleiro = len(self.tabuleiro)
        # Movimento para cima
        if linha > 0:
            nNo = No()
            nNo.pai = self
            nNo.estado_meta = self.estado_meta
            nNo.tabuleiro = self.clonarTabuleiro()
            aux = nNo.tabuleiro[linha - 1][coluna]
            nNo.tabuleiro[linha - 1][coluna] = 0
            nNo.tabuleiro[linha][coluna] = aux
            movimentos.append(nNo)

        # Movimento para baixo
        if linha < (tamanho_tabuleiro - 1):
            nNo = No()
            nNo.estado_meta = self.estado_meta
            nNo.pai = self
            nNo.tabuleiro = self.clonarTabuleiro()
            aux = nNo.tabuleiro[linha + 1][coluna]
            nNo.tabuleiro[linha + 1][coluna] = 0
            nNo.tabuleiro[linha][coluna] = aux
            movimentos.append(nNo)

        # Movimento para esquerda
        if coluna > 0:
            nNo = No()
            nNo.pai = self
            nNo.estado_meta = self.estado_meta
            nNo.tabuleiro = self.clonarTabuleiro()
            aux = nNo.tabuleiro[linha][coluna - 1]
            nNo.tabuleiro[linha][coluna - 1] = 0
            nNo.tabuleiro[linha][coluna] = aux
            movimentos.append(nNo)

        # Movimento para direita
        if coluna < (tamanho_tabuleiro - 1):
            nNo = No()
            nNo.pai = self
            nNo.estado_meta = self.estado_meta
            nNo.tabuleiro = self.clonarTabuleiro()
            aux = nNo.tabuleiro[linha][coluna + 1]
            nNo.tabuleiro[linha][coluna + 1] = 0
            nNo.tabuleiro[linha][coluna] = aux
            movimentos.append(nNo)
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
        metricas_BFS = Metricas()
        metricas_BFS.comecar_cronometro() # metrica
        fila = deque() 
        visitados = set()
        fila.append(estado_inicial)

        while fila:
            metricas_BFS.atualiza_memoria(fila) # metrica
            estado_atual = fila.popleft()
            tabu_atual = tuple(map(tuple, estado_atual.tabuleiro))

            if ehObjetivo(tabu_atual):
                passos = estado_atual.passos()
                metricas_BFS.passos = len(passos)
                metricas_BFS.finalizar_cronometro() # metrica
                return (metricas_BFS, passos)
            
            visitados.add(tabu_atual)
            movimentos = estado_atual.movimentosPossiveis()
            metricas_BFS.ciclos += 1

            for movimento in movimentos:
                mov_tabu = tuple(map(tuple, movimento.tabuleiro))
                if mov_tabu not in visitados:
                    metricas_BFS.nos_expandidos += 1
                    fila.append(movimento)        

        return None

def mostrar_resultado(tupla_busca):
    metricas, passos = tupla_busca
    for i, estado in enumerate(passos):
        print(f"""
           {estado.tabuleiro[0]}
Passo {i:02d}:  {estado.tabuleiro[1]}
           {estado.tabuleiro[2]}""")
        
    print(f"""
--------- Metricas calculadas ---------
Quantidade de passos:  {metricas.passos - 1}
Tempo:                 {metricas.tempo_execucao:.3f} segundos
Maximo de memoria:     {metricas.memoria} bytes
Nos expandidos:        {metricas.nos_expandidos}
Fator de ramificacao:  {metricas.nos_expandidos / metricas.ciclos if metricas.ciclos > 0 else 0:.2f}
""")


tabuleiro = Tabuleiro()
tabuleiro.criar_tabuleiro(3)


puzzel = No()
puzzel.tabuleiro = tabuleiro.tabuleiro
puzzel.estado_meta = tabuleiro.estado_meta

print("Estado Atual | Estado Meta")
for index, valor in enumerate(puzzel.tabuleiro):
    print(' ', valor, ' | ', puzzel.estado_meta[index])

busca = BuscaEmLargura.busca_em_largura(puzzel)

mostrar_resultado(busca)
