from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import os
import dotenv

class CrawlerReclameAqui:

    def __init__(self):
        dotenv.load_dotenv()       
        self.driver = self.config()

    def config(self):
        edge_options = Options()
        edge_options.add_argument("headless")
        edge_service = edge_options.add_extension(os.environ["DRIVER_PATH"])
        edge_driver = webdriver.Edge(edge_service)
        return edge_driver
    
    def spider(self):

        data = []

        self.driver.get("https://www.reclameaqui.com.br/empresa/aes-eletropaulo/lista-reclamacoes")
        links= self.driver.find_elements(By.ID, "site_bp_lista_ler_reclamacao")

        path = "/html/body/div[@id='__next']/div[2]/div/div/main/div/div[2]/div[1]/div[1]/div[3]"

        self.driver.quit()
        
        for link in links:
            self.driver = self.config()
            self.driver.get(str(link.get_attribute('href')))
            titulo = self.driver.find_element(By.XPATH, f"{path}/h1").text
            cidade_uf = self.driver.find_element(By.XPATH, f"{path}/div[1]/section/div[1]/span").text
            data_hora = self.driver.find_element(By.XPATH, f"{path}/div[1]/section/div[2]/span").text
            reclamacao = self.driver.find_element(By.XPATH, f"{path}/p").text
            
            cidade = cidade_uf[len(cidade_uf) - 5]
            estado = cidade_uf[-1:-2:-1]
            data = data_hora[0:10]
            hora = data_hora[14:]

            print("Titulo: ", titulo)
            print("Cidade: ", cidade)
            print("Estado: ", estado)
            print("Data: ", data)
            print("Hora: ", hora)
            print("Reclamação: ", reclamacao)
            print()

            self.driver.quit()