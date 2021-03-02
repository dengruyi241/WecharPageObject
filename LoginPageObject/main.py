from selenium import webdriver

from LoginPageObject.Login import LoginPage
from LoginPageObject.Registrer import RegisterPage


class MainPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def goto_login(self):
        self.driver.find_element_by_xpath('//*[@class = "index_top_operation_loginBtn"]').click()
        return LoginPage(self.driver)

    def goto_register(self):
        self.driver.find_element_by_xpath('//*[@class="index_head_info_pCDownloadBtn"]').click()
        return RegisterPage(self.driver)