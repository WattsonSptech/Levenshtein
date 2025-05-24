from unidecode import unidecode
from palavras import *
from levenshtein import levenshtein

sentimentos_por_frase = []

def filtrar_frase(frase: str) -> list:

    palavras = frase.split(' ')
    lista_filtrada = []

    for palavra in palavras:

        palavra = remove_caracteres_especiais(palavra.lower())

        for letra in palavra:
                if letra in NUMEROS or letra in SIMBOLOS or letra in IMAGENS_EMOJIS:
                    palavra = palavra.replace(str(letra), '')

        for palavra_proibida in PALAVRAS_NAO_UTILIZADAS:
            if (levenshtein(palavra, palavra_proibida) <= (len(palavra_proibida) // 2)):
                palavra = palavra_proibida

        if palavra not in PALAVRAS_NAO_UTILIZADAS:
                lista_filtrada.append(palavra)
    
    return lista_filtrada

def tokenizer(palavras: list) -> list:
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

def definir_sentimento(tokens: list) -> str:
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

def remove_caracteres_especiais(palavra: str) -> str:
    return unidecode(palavra)

if __name__ == "__main__":
    frase = 'Novamente acabou a energia aqui no bairro. Nem mesmo estava chovendo. Simplesmente acaba do nada. Já teve uns 10 picos de retorno, mas pisca e acaba, colocando em risco os eletrodomésticos da casa. É um total descaso. A conta vem nas alturas. O serviço é péssimo. Já queimou transformador do poste da outra esquina, menos de um ano depois, outro transformador de outra esquina, quando cai qualquer chuva, já sabemos que vai faltar luz, e hj, mesmo sem chuva já estamos a 3 hs sem energia. E só lamento que esta péssima empresa seja enfiada goela abaixo de nós moradores. Torço para que seja multada diariamente, que vaá embora o quanto antes. Não precisam me responder. Pois sei que vcs não tem a menor condição de pre😡star esse serviço. Vcs são a pior empresa que eu tive o desprazer de ser obrigado a contratar.'
    
    frase_filtrada = filtrar_frase(frase)
    
    tokens = tokenizer(frase_filtrada)
    
    sentimento = definir_sentimento(tokens)
    
    sentimentos_por_frase.append({"frase": frase, "sentimento": sentimento})

    print(sentimentos_por_frase)