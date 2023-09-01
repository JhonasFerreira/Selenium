from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
web_drive_local=MY_PATH
user=USUARIO
senha=SENHA
class InstagramBot:
    def __init__(self,path):
        self.driver=webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get('https://www.instagram.com/')
        sleep(1)
        username=self.driver.find_element_by_name('username')
        username.send_keys(user)
        password=self.driver.find_element_by_name('password')
        password.send_keys(senha,Keys.ENTER)
        sleep(4)
        agora_nao=self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        agora_nao.click()
        sleep(2)
        agora_nao_2=self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        agora_nao_2.click()

    def procurar_seguidores(self):
        self.driver.get('https://www.instagram.com/capiadiy/followers/')
        sleep(4)

        pop_up = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up)
        # print(lista_seguidores[0].find_element_by_tag_name('button').click())

    def follow():
       pass
    # array_seguidores[i].click()


bot=InstagramBot(path=web_drive_local)
bot.login()
sleep(2)
bot.procurar_seguidores()
