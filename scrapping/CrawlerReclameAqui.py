from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException, NoSuchDriverException, StaleElementReferenceException
import undetected_chromedriver as uc
import dotenv
from pprint import pprint

class CrawlerReclameAqui:

    def __init__(self):
        dotenv.load_dotenv()       
        self.driver = self.config()

    def config(self):
        try:
            chrome_options = uc.ChromeOptions()
            chrome_arguments = chrome_options.add_argument('--headless')
            chrome_driver = uc.Chrome(chrome_arguments)
        except NoSuchDriverException as e:
            print(f'Driver não encontrado: {e}')
        except Exception as e:
            print(f'Erro ao definir driver: {e}')
        return chrome_driver
    
    def spider(self):
            
        self.driver.get("https://www.reclameaqui.com.br/empresa/aes-eletropaulo/lista-reclamacoes")
        links = self.driver.find_elements(By.ID, "site_bp_lista_ler_reclamacao")
        path = "/html/body/div[@id='__next']/div[2]/div/div/main/div/div[2]/div[1]/div[1]/div[3]"

        urls = list(str(link.get_attribute('href')) for link in links)

        resultado = []

        try:
            for url in urls:
                try: 
                    print(f"Visitando url: {url}")
                    self.driver.get(url)
                    self.driver.implicitly_wait(5)

                    try: 
                        titulo = self.driver.find_element(By.XPATH, f"{path}/h1").text
                        cidade_uf = (self.driver.find_element(By.XPATH, f"{path}/div[1]/section/div[1]/span").text).split('-')
                        data_hora = self.driver.find_element(By.XPATH, f"{path}/div[1]/section/div[2]/span").text
                        reclamacao = self.driver.find_element(By.XPATH, f"{path}/p").text

                    except StaleElementReferenceException as e:
                        titulo = self.driver.find_element(By.XPATH, f"{path}/h1").text
                        cidade_uf = (self.driver.find_element(By.XPATH, f"{path}/div[1]/section/div[1]/span").text).split('-')
                        data_hora = self.driver.find_element(By.XPATH, f"{path}/div[1]/section/div[2]/span").text
                        reclamacao = self.driver.find_element(By.XPATH, f"{path}/p").text

                    

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
                        "reclamacao": reclamacao
                    })  

                except TimeoutException as e:
                   print(f'Erro ao visitar url {url}: {e}')
                except NoSuchElementException as e:
                    print(f'Elemento HTML não encontrado: {e}') 
                except WebDriverException as e:
                    print(f'Erro no Webdriver: {e}')
                
        except Exception as e:
            print('Exception: ', e)
        finally:
            pprint(resultado)
            self.driver.quit()
            return resultado