from pprint import pprint
def levenshtein(palavra1, palavra2):
    n = len(palavra1)
    m = len(palavra2)
    matriz = [[0 for i in range(m + 1)] for j in range(n + 1)]
    
    for i in range(n + 1):
        matriz[i][0] = i
        
    for j in range(m + 1):
        matriz[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if palavra1[i - 1] == palavra2[j - 1]:
                custo = 0
            else:
                custo = 1
    
            matriz[i][j] = min(matriz[i - 1][j] + 1, matriz[i][j - 1] + 1, matriz[i - 1][j - 1] + custo)

    return matriz[n][m]