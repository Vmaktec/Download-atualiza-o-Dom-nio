from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from datetime import datetime
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

# Configuração do WebDriver (ajuste o caminho para o driver do seu navegador)


download_folder = ''  # Substitua pelo caminho da pasta onde deseja salvar os downloads


chrome_options = Options()

chrome_options.add_argument("--no-sandbox")  # Desativa o modo sandbox
chrome_options.add_argument("--disable-dev-shm-usage")  # Resolve problemas de limitação de recursos em containers
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_folder,
    "download.prompt_for_download": False,  # Não pede confirmação para download
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True  # Desativa a Navegação segura do Chrome
})



servico = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico, options=chrome_options)

try:
    # Acessa o URL
    url = 'https://download.dominiosistemas.com.br/atualizacao/contabil/'
    browser.get(url)

    browser.find_element(By.XPATH, '/html/body/pre/a[12]').click()
    browser.find_element(By.XPATH, '/html/body/pre/a[8]').click()

    url = 'https://download.dominiosistemas.com.br/atualizacao/contabil/'
    browser.get(url)
    browser.find_element(By.XPATH, '/html/body/pre/a[12]').click()
    browser.find_element(By.XPATH, '/html/body/pre/a[6]').click()
    elements = browser.find_elements(By.XPATH, '/html/body/pre/a')
    # Clique no último elemento da lista
    if elements:
            elements[-1].click()
    else:
        print("Nenhum elemento encontrado")


finally:
    # Fecha o navegador após uma pausa ou imediatamente
    # input("Pressione Enter para sair...")  # Descomente para adicionar uma pausa
    time.sleep(9999999)
    browser.quit()

