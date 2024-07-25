import numpy as np

class tab_move:
    def __init__(self, matriz):
        self.atualizar_dimensoes(matriz)
        self.matriz = matriz
        
    def atualizar_dimensoes(self, matriz):
        self.linhas, self.colunas = matriz.shape
        
    def encontrar_vazio(self, matriz):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if matriz[i, j] == '_':
                    return i, j
   
    def mover_para_cima(self, matriz):
        i, j = self.encontrar_vazio(matriz)
        if i > 0:
            matriz_copy = matriz.copy() 
            matriz_copy[i, j], matriz_copy[i - 1, j] = matriz_copy[i - 1, j], matriz_copy[i, j]
            return matriz_copy  
        else:
            return matriz  
    
    def mover_para_baixo(self, matriz):
        i, j = self.encontrar_vazio(matriz)
        if i < self.linhas - 1:
            matriz_copy = matriz.copy()  
            matriz_copy[i, j], matriz_copy[i + 1, j] = matriz_copy[i + 1, j], matriz_copy[i, j]
            return matriz_copy  
        else:
            return matriz  
    
    def mover_para_esquerda(self, matriz):
        i, j = self.encontrar_vazio(matriz)
        if j > 0:
            matriz_copy = matriz.copy()  
            matriz_copy[i, j], matriz_copy[i, j - 1] = matriz_copy[i, j - 1], matriz_copy[i, j]
            return matriz_copy  
        else:
            return matriz  
    
    def mover_para_direita(self, matriz):
        i, j = self.encontrar_vazio(matriz)
        if j < self.colunas - 1:
            matriz_copy = matriz.copy()  
            matriz_copy[i, j], matriz_copy[i, j + 1] = matriz_copy[i, j + 1], matriz_copy[i, j]
            return matriz_copy  
        else:
            return matriz  
    
    def caminhos_possiveis(self, estado):
        possibilidades = []
    
        possibilidade = estado.copy()
        if not np.array_equal(self.mover_para_cima(possibilidade), estado):
            possibilidades.append(("cima", self.mover_para_cima(possibilidade)))

        possibilidade = estado.copy()
        if not np.array_equal(self.mover_para_baixo(possibilidade), estado):
            possibilidades.append(("baixo", self.mover_para_baixo(possibilidade)))
        
        possibilidade = estado.copy()
        if not np.array_equal(self.mover_para_esquerda(possibilidade), estado):
            possibilidades.append(("esquerda", self.mover_para_esquerda(possibilidade)))
    
        possibilidade = estado.copy()
        if not np.array_equal(self.mover_para_direita(possibilidade), estado):
            possibilidades.append(("direita", self.mover_para_direita(possibilidade)))
    
        return possibilidades