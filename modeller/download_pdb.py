import os 
import pandas as pd
from selenium import webdriver
# contador
n = 0
# site pbd
site = 'https://www.rcsb.org/structure/'
# deterermina o caminho real do arquivo chomedriver.exe
path =  os.path.dirname(os.path.realpath(__file__)) + '/chromedriver.exe'

#import pyautogui 
#pyautogui.hotkey('ctrl', 'shift', 'esc')

# csv tratado com os pds desejados
df = pd.read_csv('C:/Users/Acer/Documents/Progamacao/bot_pyautogui/identidade402.csv')

for i in range (len(df['id'])):

    # pega o df, seleciona coluna id, na linha n, toda a str menos o ultimo caracter
    proteina = df['id'][n][:-1]

    driver = webdriver.Chrome(executable_path = path)

    # inicia o driver com o site
    driver.get(site + proteina)

    # acessa Download
    driver.find_element_by_xpath('//*[@id="dropdownMenuDownloadFiles"]').click()
    # seleciona pbd
    driver.find_element_by_xpath('//*[@id="DownloadFilesButton"]/ul/li[3]/a').click()
    n=n+1
