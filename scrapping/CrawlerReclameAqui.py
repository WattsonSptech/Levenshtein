from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException, NoSuchDriverException, StaleElementReferenceException
import undetected_chromedriver as uc
import dotenv
import logging as log
class CrawlerReclameAqui:

    def __init__(self):
        dotenv.load_dotenv()       
        self.driver = self.config()

    def config(self):
        try:
            chrome_driver = uc.Chrome()
            chrome_driver.options.add_argument('--headless')
        except NoSuchDriverException as e:
            log.exception(f'Driver não encontrado: {e}')
        except Exception as e:
            log.exception(f'Erro ao definir driver: {e}')
        return chrome_driver
    
    def get_complaints_urls(self):
        links = self.driver.find_elements(By.ID, "site_bp_lista_ler_reclamacao")
        return list(str(link.get_attribute('href')) for link in links)

    def get_elements(self, url_list):

        base_path = "/html/body/div[@id='__next']/div[2]/div/div/main/div/div[2]/div[1]/div[1]"
        resultado = []

        try:
            for url in url_list:
                try: 
                    print(f"Visitando url: {url}")
                    self.driver.get(url)
                    self.driver.implicitly_wait(5)

                    tags = ""
                    categoria = tipo_produto = tipo_problema = "NAO INFORMADO"

                    try: 
                        titulo = self.driver.find_element(By.XPATH, f"{base_path}/div[3]/h1").text
                        cidade_uf = (self.driver.find_element(By.XPATH, f"{base_path}/div[3]/div[1]/section/div[1]/span").text).split('-')
                        data_hora = self.driver.find_element(By.XPATH, f"{base_path}/div[3]/div[1]/section/div[2]/span").text
                        reclamacao = self.driver.find_element(By.XPATH, f"{base_path}/div[3]/p").text
                        status = self.driver.find_element(By.XPATH, f"{base_path}/div[2]/div/span").text
                        
                        try:
                            tags = self.driver.find_elements(By.XPATH, f"{base_path}/div[3]/div[1]/div/ul/li")
                        except NoSuchElementException as e:
                            log.exception(f'Elemento HTML não encontrado: {e}')

                    except StaleElementReferenceException as e:
                        titulo = self.driver.find_element(By.XPATH, f"{base_path}/div[3]/h1").text
                        cidade_uf = (self.driver.find_element(By.XPATH, f"{base_path}/div[3]/div[1]/section/div[1]/span").text).split('-')
                        data_hora = self.driver.find_element(By.XPATH, f"{base_path}/div[3]/div[1]/section/div[2]/span").text
                        reclamacao = self.driver.find_element(By.XPATH, f"{base_path}/div[3]/p").text
                        status = self.driver.find_element(By.XPATH, f"{base_path}/div[2]/div/span").text

                        try:
                            tags = self.driver.find_elements(By.XPATH, f"{base_path}/div[3]/div[1]/div/ul/li")
                        except NoSuchElementException as e:
                            log.exception(f'Elemento HTML não encontrado: {e}') 
                    
                    if tags != "":
                        for li in tags:
                            a = li.find_element(By.XPATH, f"{base_path}/div[3]/div[1]/div/ul/li/div/a")
                            print("aqui >>>> ", str(a.get_property('href')))
                            if "?categoria=" in str(a.get_property('href')):
                                categoria = a.text
                            elif "?produto=" in str(a.get_property('href')):
                                tipo_produto = a.text
                            elif "?problema=" in str(a.get_property('href')):
                                tipo_problema = a.text

                    cidade = cidade_uf[0].strip()
                    uf = cidade_uf[1].strip()
                    data = data_hora[0:10]
                    hora = data_hora[14:]

                    resultado.append({
                        "url": url,
                        "cidade": cidade,
                        "uf": uf,
                        "data": data,
                        "hora": hora,
                        "titulo": titulo,
                        "reclamacao": reclamacao,
                        "status": status,
                        "categoria": categoria,
                        "tipo_produto": tipo_produto,
                        "tipo_problema": tipo_problema
                    })  

                except TimeoutException as e:
                   log.exception(f'Erro ao visitar url {url}: {e}')
                except WebDriverException as e:
                    log.exception(f'Erro no Webdriver: {e}')
                
        except Exception as e:
            log.exception('Exception: ', e)

        self.driver.close()
        self.driver.quit()
        return resultado

    def crawler(self):
        self.driver.get("https://www.reclameaqui.com.br/empresa/aes-eletropaulo/lista-reclamacoes")
        urls = self.get_complaints_urls()
        print("Finalizado!")
        return self.get_elements(urls)