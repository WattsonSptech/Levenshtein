from datetime import datetime
from abc import ABC
import pandas as pd
import boto3
import os

class Utils(ABC):
    
    @staticmethod
    def save_to_file(analises: list[dict]) -> str:
        if not os.path.exists("./temp"):
            os.mkdir("./temp")

        path = "./temp/ReclameAqui_Raw_{}.csv".format(datetime.now().strftime("%Y-%m-%d"))
        pd.DataFrame.from_records(analises).to_csv(path, sep=";", index=False)
        return path
    
    @staticmethod
    def send_to_s3(file_path):
        bucket_name = os.getenv("BUCKET_NAME_RAW", None)
        if bucket_name is None:
            print("Não foi definido um nome de bucket para onde enviar o arquivo gerado! Pulando...")
            return

        print(f'Enviando arquivo para o bucket {bucket_name}')
    
        s3 = boto3.client('s3')
        file_name = file_path.split("/")[-1]
        s3.upload_file(file_path, bucket_name, file_name)
        print('Arquivo enviado para a S3!')
