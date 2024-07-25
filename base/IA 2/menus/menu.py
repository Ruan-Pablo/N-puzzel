from menus.metodos import metodos as metodos_module
from assets.utility import utility

class menu:
    def __init__(self):
        self.cases = {
            1: self.caseBL,
            2: self.caseBPI,
            3: self.caseBAW,
            4: self.caseBAM
        }
    
    def switch(self, case):
        if case in self.cases:           
            self.cases[case]()
        else:
            print("Caso inválido")
    
    def caseBL(self):
        metodos = metodos_module()      
        util = utility() 
        matriz_gerada = util.gerar_matriz()
        matriz_embaralhada = util.embaralhar_matriz(matriz_gerada)
        metodos.busca_em_largura(matriz_embaralhada, matriz_gerada)

    def caseBPI(self):
        metodos = metodos_module()      
        util = utility() 
        matriz_gerada = util.gerar_matriz()
        matriz_embaralhada = util.embaralhar_matriz(matriz_gerada)
        metodos.busca_em_profundidade(matriz_embaralhada, matriz_gerada)
    
    def caseBAW(self):
        metodos = metodos_module()
        util = utility()
        matriz_gerada = util.gerar_matriz()
        matriz_embaralhada = util.embaralhar_matriz(matriz_gerada)
        metodos.a_estrela_pecas_erradas(matriz_embaralhada, matriz_gerada)
    
    def caseBAM(self):
        metodos = metodos_module()
        util = utility()
        matriz_gerada = util.gerar_matriz()
        matriz_embaralhada = util.embaralhar_matriz(matriz_gerada)
        metodos.a_estrela_manhatan(matriz_embaralhada, matriz_gerada)
