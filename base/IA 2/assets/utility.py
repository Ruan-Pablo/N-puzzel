import math
import random
import numpy as np 
from .tab import *
from .node import *
from .tab_move import tab_move as tab

class utility:
    def __init__(self):
        pass
    
    def imprimir_matriz(self, matriz):
        print("Matriz:")
        for linha in matriz:
            print(" ".join(str(node) for node in linha))

    def verifica_zeros_apos_virgula(self, numero):
        partes = str(numero).split('.')
        if len(partes) == 2:  
            parte_decimal = partes[1]
            if all(digito == '0' for digito in parte_decimal):
                return True
        return False
        
    def gerar_matriz(self):
        print("Envie o tamanho das peças")
        N = input()
        verificacao = math.sqrt(int(N)+1)
    
        if self.verifica_zeros_apos_virgula(verificacao):
            tabuleiro = board(int(N))
            matriz = tabuleiro.criar_matriz()
            matriz = np.array(matriz, dtype=str)  
            self.imprimir_matriz(matriz)
            return matriz  
    
        return "O número não atende a restrição"
    
    def embaralhar_matriz(self, matriz):
        vezes = random.randint(1, 50)
        embaralhar = tab(matriz)
        estado_atual = matriz.copy()
        
        for i in range(vezes):
            possibilidades = embaralhar.caminhos_possiveis(estado_atual)
            direcao, novo_estado = random.choice(possibilidades)
            estado_atual = novo_estado
            
        self.imprimir_matriz(estado_atual)
        
        return estado_atual
    
    def pecas_erradas(self, estado_atual, estado_final):
        return sum(1 for i, j in zip(estado_atual.flatten(), estado_final.flatten()) if i != j and i != '0')
    
    def distancia_manhatan(self, estado_atual, estado_final):
        distancia = 0
        tamanho = len(estado_atual)
        
        for i in range(tamanho):
            for j in range(tamanho):
                valor = estado_atual[i, j]
                if valor != '_':
                    posicao_desejada = np.argwhere(estado_final == valor)[0]
                    linha_desejada, coluna_desejada = posicao_desejada
                    distancia += abs(i - linha_desejada) + abs(j - coluna_desejada)
                    
        return distancia