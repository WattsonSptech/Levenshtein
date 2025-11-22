import os
import nltk
from scrapping.CrawlerReclameAqui import CrawlerReclameAqui
from utils.ProcessadorLN import ProcessadorLN
from utils.Utils import Utils
from utils.AnalisadorLexico import AnalisadorLexico
from dotenv import load_dotenv

if __name__ == "__main__":

    load_dotenv()
    nltk.download('stopwords')

    print("Iniciando programa...")

    utils = Utils()

    result = CrawlerReclameAqui().crawler()
    
    processador = ProcessadorLN()
    for item in result:
        processador.limpar_conectivos(item["RECLAMACAO"])

    file_path = utils.from_dict_list_to_csv_file(result)
    # utils.send_to_s3(file_path, os.getenv("BUCKET_NAME_RAW", None))

    print("Programa finalizado!")