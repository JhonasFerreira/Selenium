from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_drive_path='C:\DesenvolvimentoPy\chromedriver.exe'
DOWNLOAD=300
UPLOAD=100

class VelocidadeInternet:
    def __init__(self,driver_path):
        # self.down=DOWNLOAD
        # self.up=UPLOAD
        self.driver=webdriver.Chrome(executable_path=driver_path)
        self.download_atual=0
        self.upload_atual=0
    # def get_vel_internet(self):
    #     self.driver.get('https://www.speedtest.net')
    #     sleep(3)
    #     element = self.driver.find_element(By.ID, value='onetrust-accept-btn-handler')
    #     element.click()
    #     sleep(1.5)
    #     start = self.driver.find_element_by_css_selector('.test-mode-multi')
    #     start.click()
    #     sleep(50)
    #     close_window=self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a')
    #     close_window.click()
    #     download_speed=self.driver.find_element(By.CLASS_NAME,'download-speed').text
    #     self.download_atual = float(download_speed)
    #     up_speed=self.driver.find_element(By.CLASS_NAME,'upload-speed').text
    #     self.upload_atual=float(up_speed)
    #     self.driver.quit()

    def login_twitter(self):
        EMAIL = 'jhonasferreira1@hotmail.com'
        SENHA = '23jh23jh'
        self.driver.get(url='https://twitter.com')
        sleep(2)
        btn_login = self.driver.find_element_by_css_selector('.r-2o02ov a')
        btn_login.click()
        sleep(2)
        email_input = self.driver.find_element_by_css_selector('.r-ttdzmv input')
        email_input.send_keys(EMAIL, Keys.ENTER)
        sleep(2)
        span = self.driver.find_element_by_css_selector('.r-qvutc0 span')
        print(span.text)
        senha_input = self.driver.find_element_by_css_selector('.r-qvutc0 input')
        senha_input.send_keys('juquinha50')
        senha_input.send_keys(Keys.ENTER)
        sleep(2)
        senha_input2 = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        sleep(1)
        senha_input2.send_keys(SENHA)
        senha_input2.send_keys(Keys.ENTER)
        sleep(5)
        postar=self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        postar.send_keys('ASaasdsadsa')


    def twittar_ao_provedor(self):
        pass
internetSpeed=VelocidadeInternet(driver_path=chrome_drive_path)
sleep(1)
# internetSpeed.get_vel_internet()
# print(internetSpeed.download_atual,internetSpeed.upload_atual)
internetSpeed.login_twitter()
