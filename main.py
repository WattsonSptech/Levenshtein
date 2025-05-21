from unidecode import unidecode
from palavras import *

multiplicador = 1.0

def run():
    frase = 'Novamente acabou a energia aqui no bairro. Nem mesmo estava chovendo. Simplesmente acaba do nada. Já teve uns 10 picos de retorno, mas pisca e acaba, colocando em risco os eletrodomésticos da casa. É um total descaso. A conta vem nas alturas. O serviço é péssimo. Já queimou transformador do poste da outra esquina, menos de um ano depois, outro transformador de outra esquina, quando cai qualquer chuva, já sabemos que vai faltar luz, e hj, mesmo sem chuva já estamos a 3 hs sem energia. E só lamento que esta péssima empresa seja enfiada goela abaixo de nós moradores. Torço para que seja multada diariamente, que vaá embora o quanto antes. Não precisam me responder. Pois sei que vcs não tem a menor condição de pre😡star esse serviço. Vcs são a pior empresa que eu tive o desprazer de ser obrigado a contratar.'
    print(filtrar_frase(frase))

def filtrar_frase(frase: str) -> list:

    palavras = frase.split(' ')
    lista_filtrada = []

    for palavra in palavras:

        palavra = remove_caracteres_especiais(palavra.lower())

        for letra in palavra:
                if letra in NUMEROS or letra in SIMBOLOS or letra in IMAGENS_EMOJIS:
                    palavra = palavra.replace(str(letra), '')

        if palavra not in PALAVRAS_NAO_UTILIZADAS:
                lista_filtrada.append(palavra)
    
    return lista_filtrada

def tokenizer(palavras: list) -> list:
    tokens = []

    
    


def remove_caracteres_especiais(palavra):
    return unidecode(palavra)

if __name__ == "__main__":
    run()