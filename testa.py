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

metrica = Metrica()
metrica.comecar_cronometro()
cont = 0
print(len(cont))
for i in range(100000000):
    cont += i
metrica.finalizar_cronometro()
print(metrica.tempo_execucao)
# print(pecas_fora_do_lugar(tabuleiro, [[1,2,3],[4,5,6],[7,8,0]]))
# print(No([123]) in lista_no)
