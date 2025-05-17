from unidecode import unidecode

def run():
    print(remove_acentos('café é muito bom'))

def remove_acentos(palavra):
    return unidecode(palavra)

if __name__ == "__main__":
    run()