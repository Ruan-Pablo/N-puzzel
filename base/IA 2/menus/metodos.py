from assets.utility import utility
from algorithms.busca_em_largura import busca_em_largura as BFS
from algorithms.busca_em_profundidade import busca_em_profundidade as DFS
from algorithms.a_star import a_star as BA
import time

class metodos:
    def __init__(self):
        pass
    
    def busca_em_largura(self, estado_inicial, estado_final):
        caminho = []
        solver = BFS()
        caminho = solver.solve(estado_inicial, estado_final)
        
        if caminho is not None:
            caminho_str = " -> ".join([acao for acao, estado in caminho])
            print("Caminho da resolução: " + caminho_str)
        else:
            print("Não foi encontrada solução")
    
    def busca_em_profundidade(self, estado_inicial, estado_final):
        caminho = []
        solver = DFS()
        caminho = solver.solve(estado_inicial, estado_final)
        
        if caminho is not None:
            caminho_str = " -> ".join([acao for acao, estado in caminho])
            print("Caminho da resolução: " + caminho_str)
        else:
            print("Não foi encontrada solução")
 
    def a_estrela_pecas_erradas(self, estado_inicial, estado_final):
        caminho = []
        util = utility()
        heuristica = util.pecas_erradas(estado_inicial, estado_final)
        solver = BA(heuristica)
        
        caminho = solver.solve(estado_inicial, estado_final)
        
        if caminho is not None:
            caminho_str = " -> ".join([acao for acao, estado in caminho])
            print("Caminho da resolução: " + caminho_str)
        else:
            print("Não foi encontrada solução")
        
    def a_estrela_manhatan(self, estado_inicial, estado_final):
        caminho = []
        util = utility()
        heuristica = util.distancia_manhatan(estado_inicial, estado_final)
        solver = BA(heuristica)   
        caminho = solver.solve(estado_inicial, estado_final)
        
        end_time = time.time()
        
        if caminho is not None:
            caminho_str = " -> ".join([acao for acao, estado in caminho])
            print("Caminho da resolução: " + caminho_str)
        else:
            print("Não foi encontrada solução")
