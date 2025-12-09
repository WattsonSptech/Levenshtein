from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv
from scrapping.CrawlerReclameAqui import CrawlerReclameAqui
from utils import Utils, ProcessadorLN

def analisar_reclamacoes():
    load_dotenv()
    print("Iniciando programa...")

    print("\nIniciando scrapping...")    
    dados_extracts = CrawlerReclameAqui().crawler()

    print("\nPreparando processamento de LN...")
    process_ln = ProcessadorLN()

    print("\nAvaliando as reclamações extraídas...")
    reclams_avaliadas = []
    for dado in dados_extracts:
        datahora = datetime.strptime(f"{dado['DATA']} {dado['HORA']}", "%d/%m/%Y %H:%M")
        datahora = datahora.replace(tzinfo=ZoneInfo("America/Sao_Paulo")).isoformat()

        reclam = dado["RECLAMACAO"]
        reclam_limpa = " ".join(process_ln.tokenizar(reclam))
        avaliacao = process_ln.avaliar_sentenca(reclam_limpa)

        reclams_avaliadas.append({"Data-hora": datahora, "Avaliação": avaliacao, "Reclamação": reclam})

    print("\nPersistindo resultados...")
    utils = Utils()
    file_path = utils.save_to_file(reclams_avaliadas)
    utils.send_to_s3(file_path)
    print("Programa finalizado!")

if __name__ == "__main__":
    analisar_reclamacoes()
