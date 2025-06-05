import boto3
import os
import boto3.session
from dotenv import load_dotenv
from datetime import datetime

load_dotenv('.env')
class Utils():

    def __init__(self):
        self.session = boto3.session.Session(
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
            region_name=os.getenv('AWS_REGION')
        )
        self.s3 = self.session.client('s3')
        self.bucket = os.getenv('BUCKET_NAME')

    def upload_object(self,file:str,key:str):
        print(f'Fazendo upload do arquivo {file}')
        if file.endswith('.csv'):
            pasta = 'csv'
        elif file.endswith('.png'):
            pasta = 'png'
        else:
            pasta = 'outros'

        key_path = os.path.join(pasta, key)
        timestamp = datetime.now().strftime('%d%m%Y%h%M%S')
        file_base, extension = os.path.splitext(key)
        file_name = f"{file_base}-{timestamp}{extension}"
        key_path = os.path.join(pasta, file_name)
        try:
            self.s3.upload_file(file,self.bucket,key_path)
            print(f'Arquivo {file} enviado com sucesso')
        except Exception as e:
            print(f'Erro ao enviar o arquivo: {e}')