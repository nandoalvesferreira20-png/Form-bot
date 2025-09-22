from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Opções para reduzir logs
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--log-level=3")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Ler csv com os dados
df = pd.read_csv("data.csv")  # colunas: nome, cpf, email, telefone

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSesEXn-lCLzeai01oSUfBxMHHmvNUTGv8hkBZqVG1l4qeF2Dw/viewform?usp=dialog"

for index, row in df.iterrows():
    driver.get(form_url)
    time.sleep(2)  # esperar carregar

    # Pegar todos os inputs de texto do form
    campos = driver.find_elements(By.CSS_SELECTOR, "input.whsOnd")

    # Preencher os campos na ordem correta
    campos[0].send_keys(row["nome"])
    campos[1].send_keys(str(row["cpf"]))
    campos[2].send_keys(row["email"])
    campos[3].send_keys(str(row["telefone"]))

    # Enviar formulário
    submit_button = driver.find_element(By.XPATH, "//span[text()='Enviar']")
    submit_button.click()

    time.sleep(2)  # esperar o envio

driver.quit()
