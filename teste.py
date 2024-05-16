import random
from collections import deque

# Função para encontrar a posição do espaço vazio no tabuleiro
def encontrar_vazio(tabuleiro):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == 0:
                return i, j

# Função para gerar uma solução válida para o N-puzzle
def gerar_solucao(n):
    numeros = list(range(1, n**2))
    numeros.append(0)
    solucao = [numeros[i:i+n] for i in range(0, n**2, n)]
    return solucao

# Função para embaralhar o tabuleiro fazendo movimentos aleatórios
def embaralhar_tabuleiro(tabuleiro, movimentos):
    for _ in range(movimentos):
        vazio_i, vazio_j = encontrar_vazio(tabuleiro)
        direcao = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        novo_i, novo_j = vazio_i + direcao[0], vazio_j + direcao[1]
        if 0 <= novo_i < len(tabuleiro) and 0 <= novo_j < len(tabuleiro[0]):
            tabuleiro[vazio_i][vazio_j] = tabuleiro[novo_i][novo_j]
            tabuleiro[novo_i][novo_j] = 0

# Algoritmo de busca em largura para resolver o N-puzzle
def busca_em_largura(tabuleiro):
    fila = deque([(tabuleiro, [])])
    visitados = set()

    while fila:
        estado, caminho = fila.popleft()
        visitados.add(tuple(map(tuple, estado)))  # Convertendo o tabuleiro em tupla para torná-lo imutável

        if esta_resolvido(estado):
            return caminho

        movimentos = gerar_movimentos(estado)
        for movimento in movimentos:
            if tuple(map(tuple, movimento)) not in visitados:
                fila.append((movimento, caminho + [movimento]))

    return None  # Se não encontrou solução

# Função para verificar se o tabuleiro está resolvido
def esta_resolvido(tabuleiro):
    tamanho = len(tabuleiro) * len(tabuleiro[0])
    return all(tabuleiro[i // len(tabuleiro)][i % len(tabuleiro[0])] == i + 1 for i in range(tamanho - 1)) and tabuleiro[-1][-1] == 0

# Função para gerar os movimentos válidos a partir de um estado do tabuleiro
def gerar_movimentos(tabuleiro):
    movimentos = []
    vazio_i, vazio_j = encontrar_vazio(tabuleiro)
    direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Movimentos: direita, esquerda, baixo, cima

    for di, dj in direcoes:
        novo_i, novo_j = vazio_i + di, vazio_j + dj
        if 0 <= novo_i < len(tabuleiro) and 0 <= novo_j < len(tabuleiro[0]):
            novo_tabuleiro = [linha[:] for linha in tabuleiro]  # Copia o tabuleiro
            novo_tabuleiro[vazio_i][vazio_j] = novo_tabuleiro[novo_i][novo_j]
            novo_tabuleiro[novo_i][novo_j] = 0
            movimentos.append(novo_tabuleiro)

    return movimentos

# Teste do algoritmo
n = 4
solucao = gerar_solucao(n)
tabuleiro = [linha[:] for linha in solucao]
embaralhar_tabuleiro(tabuleiro, n**3 * 2)  # Embaralha o tabuleiro fazendo 2*N^3 movimentos aleatórios
print("Tabuleiro inicial:")
for linha in tabuleiro:
    print(linha)

passos = busca_em_largura(tabuleiro)
if passos:
    print("\nPassos para a solução:")
    for i, estado in enumerate(passos):
        print(f"Passo {i + 1}:")
        for linha in estado:
            print(linha)
        print()
else:
    print("\nNão foi possível encontrar uma solução.")
