from unidecode import unidecode
from palavras import *

multiplicador = 1.0

def run():

    frase = 'Vai tomar no cu Enel, krl! que ódio'
    palavras = frase.split(' ')

    lista_filtrada = []

    for palavra in palavras:

        palavra = remove_acentos(palavra.lower())
        palavra_invalida = False

        if palavra not in PALAVRAS_NAO_UTILIZADAS:

            for letra in palavra:
                if letra in [NUMEROS, SIMBOLOS, (EMOJIS[i]['emoji'] for i in range(len(EMOJIS)))]:
                    palavra_invalida = True
                    break
        
        else:
            palavra_invalida = True
        
        if not palavra_invalida:
                lista_filtrada.append(palavra)
        
    print(lista_filtrada)

def remove_acentos(palavra):
    return unidecode(palavra)

if __name__ == "__main__":
    run()