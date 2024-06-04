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
    estado_meta = tuple(map(tuple, estado_meta))
    return estado_meta == tabuleiro

def printarTabuleiro(tabuleiro):
    for i in tabuleiro:
        print(i)

def solucionavel(lista):
    inversoes = 0
    for i,e in enumerate(lista):
        if e == 0:
            continue
        for j in range(i+1,len(lista)):
            if lista[j]==0:
                continue
            if e > lista[j]:
                inversoes+=1
        if inversoes%2 == 1:
            return False
        else:
            return True


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
        for i in range(1000):
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
        self.estado_meta = estado_meta
        return estado_meta


class No:
    def __init__(self):
        self.tabuleiro = None
        self.estado_meta = None
        self.pai = None
        self.pontos = 0
 
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
            vNo = No()
            vNo.pai = self
            vNo.estado_meta = self.estado_meta
            vNo.tabuleiro = self.clonarTabuleiro()
            aux = vNo.tabuleiro[linha - 1][coluna]
            vNo.tabuleiro[linha - 1][coluna] = 0
            vNo.tabuleiro[linha][coluna] = aux
            movimentos.append(vNo)

        # Movimento para baixo
        if linha < (tamanho_tabuleiro - 1):
            vNo = No()
            vNo.estado_meta = self.estado_meta
            vNo.pai = self
            vNo.tabuleiro = self.clonarTabuleiro()
            aux = vNo.tabuleiro[linha + 1][coluna]
            vNo.tabuleiro[linha + 1][coluna] = 0
            vNo.tabuleiro[linha][coluna] = aux
            movimentos.append(vNo)
            if vNo.tabuleiro == vNo.estado_meta: print(" -------------- ACHOU --------------")

        # Movimento para esquerda
        if coluna > 0:
            vNo = No()
            vNo.pai = self
            vNo.estado_meta = self.estado_meta
            vNo.tabuleiro = self.clonarTabuleiro()
            aux = vNo.tabuleiro[linha][coluna - 1]
            vNo.tabuleiro[linha][coluna - 1] = 0
            vNo.tabuleiro[linha][coluna] = aux
            movimentos.append(vNo)

        # Movimento para direita
        if coluna < (tamanho_tabuleiro - 1):
            vNo = No()
            vNo.pai = self
            vNo.estado_meta = self.estado_meta
            vNo.tabuleiro = self.clonarTabuleiro()
            aux = vNo.tabuleiro[linha][coluna + 1]
            vNo.tabuleiro[linha][coluna + 1] = 0
            vNo.tabuleiro[linha][coluna] = aux
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
        fila = deque() 
        visitados = set()
        fila.append(estado_inicial)

        while fila:
            estado_atual = fila.popleft()
            
            # Supondo que `estado_atual.tabuleiro` seja uma lista, vamos convertê-lo para uma tupla
            tabu_atual = tuple(map(tuple, estado_atual.tabuleiro))

            if ehObjetivo(tabu_atual):
                print('fim da busca')
                return estado_atual.passos()
            
            # print("estado atual:", tabu_atual)
            
            visitados.add(tabu_atual)
            movimentos = estado_atual.movimentosPossiveis()
            
            # Adiciona os tabuleiros de possíveis movimentos para verificação e debug
            # for movimento in movimentos:
            #     mov_tabu = tuple(map(tuple, movimento.tabuleiro))
                # print(mov_tabu)
            
            # print(visitados)
            
            for movimento in movimentos:
                mov_tabu = tuple(map(tuple, movimento.tabuleiro))
                if mov_tabu not in visitados:
                    fila.append(movimento)

# Exemplo de uso:
# Define a função `ehObjetivo` que verifica se um tabuleiro é o estado objetivo
# Define a classe `No` com atributos `tabuleiro`, método `passos()` e `movimentosPossiveis()`


        
        return None  # Nenhum estado objetivo encontrado

class BuscaEmProfundidade:
    def buscar(self, inicio, objetivo):
        obj = objetivo
        profundidade = 0
        
        while True:
            resultado = self.busca_limitada_por_profundidade(BuscaEmProfundidade, inicio, obj, profundidade)
            if resultado:
                return resultado

            profundidade += 1
    
    def busca_em_profundidade(self, inicio, objetivo, limite):
        pilha = [(inicio, limite)]
        
        while len(pilha) > 0:
            atual, profundidade_restante = pilha.pop()
            
            if atual == objetivo:
                return atual.passos()
            
            if profundidade_restante > 0:
                print(atual.passos())
                caminho_atual = atual.passos()
                
                if atual in caminho_atual[:-1]:
                    continue
                
                for vizinho in atual.movimentosPossiveis():
                    pilha.append((vizinho, profundidade_restante - 1))
        
        return False


class AEstrela_h1:
    
    def busca(estado_inicial: No):
        def pecas_fora_do_lugar(no: No, estado_meta: list):
            counter = 0
            for i in range(len(no.tabuleiro)):
                for j in range(len(no.tabuleiro)):
                    if no.tabuleiro[i][j] == 0: continue
                    if no.tabuleiro[i][j] != estado_meta[i][j]:
                        counter += 1

            return counter
        fila_prioridade = deque()
        fila_prioridade.append((0, estado_inicial))

        pontos_g = { estado_inicial: 0 }

        while fila_prioridade:
            estado_atual:No = fila_prioridade.popleft()[1]
            
            if ehObjetivo(estado_atual.tabuleiro):
                print('Fim A*')
            # print(pontos_g[estado_atual])
            tentiva_ponto_g = pontos_g[estado_atual] + 1
            # print('tetatiav ', tentiva_ponto_g)

            movimentos = estado_atual.movimentosPossiveis()

            for movimento in movimentos:
                if movimento not in pontos_g or tentiva_ponto_g < pontos_g[movimento]:
                    fila_prioridade.appendleft((tentiva_ponto_g + pecas_fora_do_lugar(movimento, movimento.estado_meta), movimento))
                    pontos_g[movimento] = tentiva_ponto_g
        return None

# Exemplo de uso
# estado_inicial = ...
# estado_objetivo = busca_em_largura(estado_inicial)

tabuleiro = Tabuleiro()
tabuleiro.criar_tabuleiro(3)

print(tabuleiro.tabuleiro)
print(tabuleiro.estado_meta)

puzzel = No()
puzzel.tabuleiro = tabuleiro.tabuleiro
puzzel.estado_meta = [[1,2,3],[4,5,6],[7,8,0]]

# if ehObjetivo(((1,2,3),(4,5,6),(7,8,0))):
#     print('fim da busca')

final = BuscaEmLargura.busca_em_largura(puzzel)
# final = BuscaEmProfundidade.buscar(BuscaEmProfundidade, puzzel, puzzel.estado_meta)
# a_estrela = AEstrela_h1.busca(puzzel)
# print(a_estrela)
# print(final)
for i, state in enumerate(final):
        print('-' * 10 + f' Passo {i} ' + '-' * 10)
        printarTabuleiro(state.tabuleiro)