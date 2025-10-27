
from scrapping.CrawlerReclameAqui import CrawlerReclameAqui
from utils.Utils import Utils
from utils.AnalisadorLexico import AnalisadorLexico
import os
from dotenv import load_dotenv

if __name__ == "__main__":

    load_dotenv()

    print("Iniciando programa...")

    al = AnalisadorLexico()
    utils = Utils()

    result = CrawlerReclameAqui().crawler()
    
    for item in result:
        filtered_list = al.filtrar_frase(item['RECLAMACAO'])
        tokens = al.tokenizer(filtered_list)
        emotion = al.definir_sentimento(tokens)
        item['SENTIMENTO_FRASE'] = emotion

    file_path = utils.from_dict_list_to_csv_file(result)
    utils.send_to_s3(file_path, os.getenv("BUCKET_NAME_RAW", None))

    print("Programa finalizado!")