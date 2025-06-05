from unidecode import unidecode
from palavras import *
from levenshtein import levenshtein
from crawlerReddit import *
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt 
from Utils import *
from datetime import datetime
import os

def filtrar_frase(frase: str) -> list:
    palavras = frase.split(' ') 
    lista_filtrada = []
    
    for palavra in palavras:

        palavra_encontrada = False

        palavra = remove_caracteres_especiais(palavra.lower())

        for letra in palavra:
                if letra in NUMEROS or letra in SIMBOLOS or letra in IMAGENS_EMOJIS:
                    palavra = palavra.replace(str(letra), '')

        for item in PALAVRAS_BOAS + PALAVRAS_RUINS + INTENSIFICADORES_NEGATIVOS + INTENSIFICADORES_POSITIVOS + PALAVRAS_BAIXO_CALAO:
            nota_levenshtein = levenshtein(palavra, item)
            if (nota_levenshtein != 0 and nota_levenshtein < len(palavra) // 2):
                print(f'Troca realizada: {palavra} -> {item}')
                palavra = item
                palavra_encontrada = True
            
        if not palavra_encontrada:
            print("Lexema não reconhecido: ", palavra)
            
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

def analisar_sentimento_comentarios(posts:dict) -> dict:
    sentimentos_por_frase = {
        'frase': [],
        'sentimento': [],
        'wordcloud': []
    }

    for post_id, post_data in posts.items():
        link = post_data['link']
        comentarios = get_post_comments(link, post_id)
        frases = filter_comments(comentarios)
        for frase in frases:
            frase_filtrada = filtrar_frase(frase)
            sentimentos_por_frase['wordcloud'] += frase_filtrada
            tokens = tokenizer(frase_filtrada)
            sentimento = definir_sentimento(tokens)

            if frase not in sentimentos_por_frase["frase"]:
                sentimentos_por_frase['frase'].append(frase)
                sentimentos_por_frase['sentimento'].append(sentimento)

    return sentimentos_por_frase

if __name__ == "__main__":
    s3 = Utils()
    df = pd.DataFrame()
    posts = get_posts_links('saopaulo', 'enel',1)
    lista = analisar_sentimento_comentarios(posts)
    df  = pd.DataFrame({'id': range(1,1+len(lista['frase'])),'frase': lista["frase"], 'sentimento': lista["sentimento"]})
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    txt_file = f'arquivos/txt/resultCrawler{timestamp}.txt'
    with open(txt_file,'x',encoding='utf-8') as f:
        for i in range(len(lista['wordcloud'])):
            f.write(f'{lista["wordcloud"][i]}\n')

    csv_path = 'arquivos/csv/'
    csv_files = [os.path.join(csv_path, f) for f in os.listdir(csv_path) if os.path.isfile(os.path.join(csv_path, f))]
    recent_csv = ''
    if csv_files:
        recent_csv = max(csv_files, key=os.path.getctime)
        df.to_csv(f'arquivos/csv/dataframe{timestamp}.csv', index=False, sep=';')
        s3.upload_object(recent_csv,'comentarios.csv')

    txt_path = 'arquivos/txt/'
    txt_files = [os.path.join(txt_path, f) for f in os.listdir(txt_path) if os.path.isfile(os.path.join(txt_path, f))]
    recent_file = ''
    if txt_files:
        recent_file = max(txt_files, key=os.path.getctime)
        with open(recent_file,'r',encoding='utf-8') as f:
          text = f.read()
          wordcloud = WordCloud(width=800, height=600, background_color='white', colormap='Set2', collocations=False).generate(text)
          plt.imshow(wordcloud, interpolation='bilinear')
          plt.axis("off")
          image_name = os.path.join(f'arquivos/image/palavras{timestamp}.png')
          plt.savefig(image_name)
          s3.upload_object(image_name,'wordcloud.png')
          plt.show()


    
    
    


