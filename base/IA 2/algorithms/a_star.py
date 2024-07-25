import numpy as np
import heapq
from assets.node import node as bfs_node
from assets.utility import utility as heuristicas
from assets.tab_move import tab_move as tab
from assets.metrics import Metrics

class a_star:
    def __init__(self, heuristica):
        self.heuristica = heuristica
    
    def solve(self, estado_inicial, estado_final):
        metrics = Metrics()
        metrics.start_timer()
        
        estado_inicial_node = bfs_node(valor=np.array(estado_inicial, dtype=str))
        estado_inicial_node.f = self.heuristica
        fronteira = []
        heapq.heappush(fronteira, estado_inicial_node)
        explorado = set()
        
        estado_inicial_str = self.estado_to_str(estado_inicial)
        g_score = {estado_inicial_str: 0}
        f_score = {estado_inicial_str: self.heuristica}
        
        while fronteira:
            metrics.update_max_memoria(len(fronteira), len(explorado))
            atual_node = heapq.heappop(fronteira)
            valor = atual_node.valor
            
            print("Atual")
            print(valor)
            
            if np.array_equal(valor, estado_final):
                metrics.stop_timer()
                print("Solução encontrada")
                metrics.print_metrics()
                caminho = self.construir_caminho(atual_node)
                print(f"Quantidade de passos: {len(caminho)}")
                return caminho
            
            explorado.add(tuple(map(tuple, valor)))
            metrics.increment_nos_expandidos()
            
            filhos = list(self.caminhos_possiveis(valor))
            metrics.add_filhos(len(filhos))
            
            for acao, estado_filho in filhos:
                metrics.increment_passos()
                estado_filho_tupla = tuple(map(tuple, estado_filho))
                tentativa_g_score = g_score[str(valor.tolist())] + 1

                if estado_filho_tupla not in explorado or tentativa_g_score < g_score.get(str(estado_filho.tolist()), float('inf')):
                    g_score[str(estado_filho.tolist())] = tentativa_g_score
                    f_score[str(estado_filho.tolist())] = tentativa_g_score + self.heuristica
                    no_filho = bfs_node(valor=estado_filho, pai=atual_node, acao=acao, g=tentativa_g_score, f=f_score[str(estado_filho.tolist())])
                    heapq.heappush(fronteira, no_filho)
                    explorado.add(estado_filho_tupla)
        
        metrics.stop_timer()
        print("Solução não encontrada")
        metrics.print_metrics()
        return None
        
    def estado_to_str(self, estado):
        return str(estado.tolist())
    
    def caminhos_possiveis(self, estado):
        tab_move = tab(estado)
        return tab_move.caminhos_possiveis(estado)
        
    def construir_caminho(self, node):
        caminho = []
        
        while node.pai:
            caminho.append((node.acao, node.valor))
            node = node.pai
            
        caminho.reverse()
        return caminho
