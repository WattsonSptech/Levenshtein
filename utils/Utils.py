from unidecode import unidecode
import pandas as pd
from datetime import date
import boto3
import os

class Utils:

    def __init__(self):
        pass

    def to_ascii_string(self, palavra: str) -> str:
        return unidecode(palavra)
    
    def from_dict_list_to_csv_file(self, data: dict) -> None:
        
        ano = date.today().year
        mes = date.today().month
        dia = date.today().day

        try: 
            df = pd.DataFrame(data)
            if not os.path.exists("./temp"):
                os.mkdir("./temp")
            path = f"./temp/ReclameAqui_Raw_{ano}{mes}{dia}.csv"
            df.to_csv(path, ";")
            return path
        except Exception as e:
            print(f"Erro: {e}")
    
    def send_to_s3(self, file_path, bucket_name):
        print(f'Enviando arquivo para o bucket {bucket_name}')
        try:
            s3 = boto3.client('s3')
            file_name = file_path.split("/")[-1]
            s3.upload_file(file_path, bucket_name, file_name)
            print('Arquivo enviado para a S3!')
        except Exception as e:
            print(f'Erro ao enviar arquivo para a S3: {e}') 
        
