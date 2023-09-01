from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Variavel Selenium


#Header
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Accept-Language':'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'X-Deviceid':'94b810f1-4b9d-4168-91e7-e7318dfdfc5c',
    'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTU5NDE4MzUsInVzZXJfbmFtZSI6Impob25hc2ZlcnJlaXJhMzRAZ21haWwuY29tIiwiYXV0aG9yaXRpZXMiOlsiU0lURSJdLCJqdGkiOiIxYTljMTMwMC00ZjQ4LTQxMjUtYWZiOS0wNTkwZWU5YWE3NTUiLCJjbGllbnRfaWQiOiJ6YXAtc2l0ZSIsInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdfQ.jgZW_UjlyvM9C_XG3DM1NYIwmbx5UeFfQVhvTtqU6lA'
}
#URLS para o Web Scrapping
url_zapimoveis='https://www.zapimoveis.com.br/aluguel/imoveis/pr+londrina/1-quarto/?transacao=aluguel&onde=,Paran%C3%A1,Londrina,,,,,city,BR%3EParana%3ENULL%3ELondrina,-23.319731,-51.166201,&pagina=1&banheiros=1&quartos=1&tipoAluguel=Mensal'
data_aluguel=requests.get(url_zapimoveis,headers=header)
data_aluguel.raise_for_status()
sopa=BeautifulSoup(data_aluguel.text,'lxml')

lista_alugueis=sopa.select(selector='.listing-wrapper__content div .result-card')


lista_enderecos=[(endereco.find(name='h2').text,endereco.find('p').text) for endereco in lista_alugueis[::2]]
print(lista_enderecos)
lista_valores=[val.select_one(selector='.listing-price p').text.replace('Total ','') for val in lista_alugueis[::2]]
print(lista_valores)
lista_links=[aluguel.get('href') for aluguel in lista_alugueis[1::2]]
print(lista_links)

url_form='https://docs.google.com/forms/d/e/1FAIpQLSeEamtiX69ybXeNCtc2O-Ul6ebbpzEbfiEOm0VbeCULpcgfLQ/viewform?usp=sf_link'
chrome_drive_path='C:\DesenvolvimentoPy\chromedriver.exe'

driver=webdriver.Chrome(executable_path=chrome_drive_path)
driver.get(url=url_form)
sleep(1)

for i in range(len(lista_enderecos)):
    inputs=driver.find_elements_by_css_selector('.zHQkBf')
    endereco=inputs[0]
    preco=inputs[1]
    link=inputs[2]
    if len(lista_enderecos[i][1])==0:
        endereco.send_keys(f'{lista_enderecos[i][0]}')
        print(len(lista_enderecos[i][1]))
    else:
        endereco.send_keys(f'{lista_enderecos[i][1]},{lista_enderecos[i][0]}')
    preco.send_keys(lista_valores[i])
    link.send_keys(lista_links[i])
    sleep(1)
    btn=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    btn.click()
    sleep(1)
    voltar=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    voltar.click()

