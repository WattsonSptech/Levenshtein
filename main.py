
from scrapping.CrawlerReclameAqui import CrawlerReclameAqui
from utils.Utils import Utils
from utils.AnalisadorLexico import AnalisadorLexico

if __name__ == "__main__":

    print("Iniciando programa...")

    al = AnalisadorLexico()
    utils = Utils()

    result = CrawlerReclameAqui().crawler()
    
    for item in result:
        filtered_list = al.filtrar_frase(item['RECLAMACAO'])
        tokens = al.tokenizer(filtered_list)
        emotion = al.definir_sentimento(tokens)
        item['SENTIMENTO_FRASE'] = emotion

    utils.from_dict_list_to_csv_file(result)

    print("Programa finalizado!")