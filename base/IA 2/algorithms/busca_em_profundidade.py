import numpy as np
from collections import deque
from assets.node import node as dfs_node
from assets.tab_move import tab_move as tab
from assets.metrics import Metrics

class busca_em_profundidade:
    def __init__(self, limite_profundidade=30):
        self.limite_profundidade = limite_profundidade

    def solve(self, estado_inicial, estado_final):
        metrics = Metrics()
        metrics.start_timer()
        
        estado_final = np.array(estado_final, dtype=str)
        fronteira = deque([dfs_node(np.array(estado_inicial, dtype=str))])
        explorado = set()

        while fronteira:
            metrics.update_max_memoria(len(fronteira), len(explorado))
            node = fronteira.pop()
            valor = node.valor
            profundidade = node.profundidade

            print("Estado atual (valor):")
            print(np.array(valor))
            print("Estado final:")
            print(np.array(estado_final))
            print("Profundidade atual:", profundidade)

            if np.array_equal(valor, estado_final):
                metrics.stop_timer()
                print("Solução encontrada")
                metrics.print_metrics()
                caminho = self.construir_caminho(node)
                print(f"Quantidade de passos: {len(caminho)}")
                return caminho

            if profundidade < self.limite_profundidade:
                explorado.add(tuple(map(tuple, valor)))
                metrics.increment_nos_expandidos()

                filhos = list(self.caminhos_possiveis(valor))
                metrics.add_filhos(len(filhos))

                for acao, estado_filho in filhos:
                    metrics.increment_passos()
                    estado_filho_tupla = tuple(map(tuple, estado_filho))

                    if estado_filho_tupla not in explorado:
                        no_filho = dfs_node(estado_filho, node, acao, profundidade + 1)
                        fronteira.append(no_filho)

        metrics.stop_timer()
        metrics.print_metrics()
        return ("Não foi possível encontrar a solução dentro do limite de profundidade.", len(explorado))

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
