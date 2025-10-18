from utils.palavras import *
from utils.Utils import Utils

class AnalisadorLexico:
    
    def __init__(self):
        self.sentimentos_por_frase = list()
        self.utils = Utils()

    def filtrar_frase(self, frase: str) -> list:

        palavras = frase.split(' ')
        lista_filtrada = []

        for palavra in palavras:

            palavra = self.utils.to_ascii_string(palavra.lower())

            for letra in palavra:
                if letra in NUMEROS or letra in SIMBOLOS or letra in IMAGENS_EMOJIS:
                    palavra = palavra.replace(str(letra), '')

            for item in PALAVRAS_BOAS + PALAVRAS_RUINS + INTENSIFICADORES_NEGATIVOS + INTENSIFICADORES_POSITIVOS + PALAVRAS_BAIXO_CALAO:
                nota_levenshtein = self.levenshtein(palavra, item)
                if (nota_levenshtein != 0 and nota_levenshtein < len(palavra) // 2):
                    palavra = item
                else:
                    pass
                
            if palavra not in PALAVRAS_NAO_UTILIZADAS:
                lista_filtrada.append(palavra)
        
        return lista_filtrada

    def tokenizer(self, palavras: list) -> list:
        tokens = []

        for palavra in palavras:
            if palavra in PALAVRAS_BOAS:
                tokens.append((palavra, "PSTV"))
            elif palavra in PALAVRAS_RUINS:
                tokens.append((palavra, "NGTV"))
            elif palavra in INTENSIFICADORES_NEGATIVOS + INTENSIFICADORES_POSITIVOS:
                tokens.append((palavra, "MULT"))
            else:
                tokens.append((palavra, "NULL"))

        return tokens

    def definir_sentimento(self, tokens: list) -> str:
        multiplicador = 1.0
        pontos = 0

        for token in tokens:
            if token[1] == "PSTV":
                pontos = pontos + 1 * multiplicador
                multiplicador = 1.0
            elif token[1] == "NGTV":
                pontos = pontos + (-1 * multiplicador)
                multiplicador = 1.0
            elif token[1] == "MULT":
                multiplicador += 1

        if (pontos == 0):
            return "Neutro"
        elif (pontos > 0): 
            return "Positivo"
        else:
            return "Negativo"

    def levenshtein(self, palavra1, palavra2):
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