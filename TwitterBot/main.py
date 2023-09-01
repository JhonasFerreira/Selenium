from time import sleep,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_drive_path='C:\DesenvolvimentoPy\chromedriver.exe'

driver=webdriver.Chrome(executable_path=chrome_drive_path)
def login_twitter():
    EMAIL='jhonasferreira1@hotmail.com'
    SENHA='23jh23jh'
    driver.get(url='https://twitter.com')
    sleep(2)
    btn_login=driver.find_element_by_css_selector('.r-2o02ov a')
    btn_login.click()
    sleep(2)
    email_input=driver.find_element_by_css_selector('.r-ttdzmv input')
    email_input.send_keys(EMAIL,Keys.ENTER)
    sleep(2)
    span=driver.find_element_by_css_selector('.r-qvutc0 span')
    print(span.text)
    senha_input=driver.find_element_by_css_selector('.r-qvutc0 input')
    senha_input.send_keys('juquinha50')
    senha_input.send_keys(Keys.ENTER)
    sleep(2)
    senha_input2=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    sleep(1)
    senha_input2.send_keys(SENHA)
    senha_input2.send_keys(Keys.ENTER)

login_twitter()