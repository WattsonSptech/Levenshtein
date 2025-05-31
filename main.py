from unidecode import unidecode
from palavras import *
from levenshtein import levenshtein
from crawlerReddit import *

sentimentos_por_frase = []

def filtrar_frase(frase: str) -> list:
    palavras = frase.split(' ')
    lista_filtrada = []
    
    for palavra in palavras:

        palavra = remove_caracteres_especiais(palavra.lower())

        for letra in palavra:
                if letra in NUMEROS or letra in SIMBOLOS or letra in IMAGENS_EMOJIS:
                    palavra = palavra.replace(str(letra), '')

        for item in PALAVRAS_BOAS + PALAVRAS_RUINS + INTENSIFICADORES_NEGATIVOS + INTENSIFICADORES_POSITIVOS + PALAVRAS_BAIXO_CALAO:
            nota_levenshtein = levenshtein(palavra, item)
            if (nota_levenshtein != 0 and nota_levenshtein < len(palavra) // 2):
                # print(f'Troca realizada: {palavra} -> {item}')
                palavra = item
            else:
                pass
            
        if palavra not in PALAVRAS_NAO_UTILIZADAS:
            lista_filtrada.append(palavra)
    
    # print(lista_filtrada)
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

def analisar_setimento_comentarios(posts:dict):
    for post_id, post_data in posts.items():
        link = post_data['link']
        comentarios = get_post_comments(link, post_id)
        frases = filter_comments(comentarios)
        for frase in frases:
            frase_filtrada = filtrar_frase(frase)
            tokens = tokenizer(frase_filtrada)
            sentimento = definir_sentimento(tokens)
            sentimentos_por_frase.append({"frase": frase, "sentimento": sentimento})

if __name__ == "__main__":
    
    posts = get_posts_links('saopaulo', 'enel',1)
    analisar_setimento_comentarios(posts)


