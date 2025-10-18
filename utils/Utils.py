from unidecode import unidecode
import pandas as pd

class Utils:

    def __init__(self):
        pass

    def to_ascii_string(self, palavra: str) -> str:
        return unidecode(palavra)
    
    def from_dict_list_to_csv_file(self, data: dict) -> None:
        try: 
            df = pd.DataFrame(data)
            df.to_csv("temp/ReclameAqui_Raw.csv", ";")
        except Exception as e:
            print(f"Erro: {e}")
