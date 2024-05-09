def criar_matriz_objetivo(tamanho):
    matriz_objetivo = []

    for linha in range(tamanho):
        linha_objetivo = []
        for coluna in range(tamanho):
            valor = linha * tamanho + coluna + 1
            if valor == tamanho * tamanho:
                valor = 0
            linha_objetivo.append(valor)
        matriz_objetivo.append(linha_objetivo)

    return matriz_objetivo

# Exemplo de uso
tamanho = 5
matriz_objetivo = criar_matriz_objetivo(tamanho)
print(matriz_objetivo)
