import sys 
import time
class No:
    def __init__(self, tabuleiro=None, pai=None) -> None:
        self.tabuleiro = tabuleiro
        self.pai = pai

def pecas_fora_do_lugar(no, estado_meta: list):
    counter = 0
    for i in range(len(no)):
        for j in range(len(no)):
            if no[i][j] != estado_meta[i][j]:
                counter += 1
    return counter

tabuleiro = [[1,2,3],[4,6,5],[7,8,0]]
lista_no = [No([123]), No([123]), No([456])]
n=0
m=([123])
visitados = 0
# print(sys.getsizeof(visitados) if visitados > 0 else 0)

class Metrica:
    def __init__(self) -> None:
        self.inicio_tempo = 0
        self.tempo_execucao = 0

    def comecar_cronometro(self):
        self.inicio_tempo = time.time()
    def finalizar_cronometro(self):
        self.tempo_execucao = time.time() - self.inicio_tempo



from heapq import heappop, heappush

def heuristic(state, goal):
    """Calcula a heurística de Manhattan para o estado dado."""
    return sum(abs(s % 3 - g % 3) + abs(s // 3 - g // 3)
               for s, g in ((state.index(i), goal.index(i)) for i in range(1, 9)))

def a_star_search(start, goal):
    """Realiza a busca A* no problema do 8 puzzle."""
    def get_neighbors(state):
        """Retorna os estados vizinhos possíveis a partir do estado atual."""
        neighbors = []
        index = state.index(0)  # Posição do espaço vazio (0)
        x, y = index % 3, index // 3
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Esquerda, direita, cima, baixo

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_index = ny * 3 + nx
                new_state = list(state)
                new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
                neighbors.append(tuple(new_state))

        return neighbors

    open_list = []
    heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_list:
        _, current = heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(open_list, (f_score[neighbor], neighbor))

    return None

def printarTabuleiro(tabuleiro):
    for i in tabuleiro:
        print(i)

# Exemplo de uso
start = ((1, 2, 3),
         (4, 0, 5),
         (6, 7, 8))
goal = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))

path = a_star_search(start, goal)
print("Caminho encontrado:")
for step in path:
    printarTabuleiro(step)


# print(pecas_fora_do_lugar(tabuleiro, [[1,2,3],[4,5,6],[7,8,0]]))
# print(No([123]) in lista_no)
