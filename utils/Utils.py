from unidecode import unidecode
import pandas as pd
from datetime import date

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
            df.to_csv(f"temp/ReclameAqui_Raw_{ano}{mes}{dia}.csv", ";")
        except Exception as e:
            print(f"Erro: {e}")
