import time

class Metrics:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.max_memoria = 0
        self.nos_expandidos = 0
        self.total_filhos = 0
        self.passos = 0

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.end_time = time.time()

    def elapsed_time(self):
        return self.end_time - self.start_time if self.start_time and self.end_time else 0

    def update_max_memoria(self, fronteira_len, explorado_len):
        self.max_memoria = max(self.max_memoria, fronteira_len + explorado_len)

    def increment_nos_expandidos(self):
        self.nos_expandidos += 1

    def add_filhos(self, num_filhos):
        self.total_filhos += num_filhos

    def increment_passos(self): 
        self.passos += 1

    def print_metrics(self):
        print(f"Nós expandidos: {self.nos_expandidos}")
        print(f"Memória máxima usada: {self.max_memoria}")
        fator_ramificacao_media = self.total_filhos / self.nos_expandidos if self.nos_expandidos > 0 else 0
        print(f"Fator de ramificação média: {fator_ramificacao_media}")
        print(f"Tempo gasto: {self.elapsed_time():.4f} segundos")
