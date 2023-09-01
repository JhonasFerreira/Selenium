from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='C:\DesenvolvimentoPy\chromedriver.exe')
def logar():
    try:
        email=''
        senha=''
        site_linkedin='https://www.linkedin.com'
        driver.get(url=site_linkedin)
        sleep(3)
        email_input=driver.find_element_by_id('session_key')
        email_input.send_keys(email)
        senha_input=driver.find_element_by_id('session_password')
        senha_input.send_keys(senha)
        senha_input.send_keys(Keys.ENTER)
    except:
        driver.refresh()
        logar()
logar()

def buscador_vaga():
    driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3691496305&f_AL=true&f_E=1%2C2%2C3&f_WT=3%2C2&geoId=106057199&keywords=Python&location=Brasil&refresh=true&sortBy=R')
    sleep(4)
    li_vagas=driver.find_elements_by_css_selector('.ember-view a')
    li_vagas[0].click()
    try:
        btn_candidatura=driver.find_element_by_css_selector('.jobs-apply-button--top-card button')
    except NoSuchElementException:
        pass
    else:
        btn_candidatura.click()
    print(li_vagas[0].text)
