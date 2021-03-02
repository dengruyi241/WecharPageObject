from time import sleep


class RegisterPage:
    def __init__(self,driver):
        self.driver = driver

    def RegisterAccount(self):
        self.driver.find_element_by_xpath('//*[@id="corp_name"]').send_keys("深圳市如意测试有限公司")
        self.driver.find_element_by_xpath('//*[@id="manager_name"]').send_keys("Terry")
        self.driver.find_element_by_xpath('//*[@id="register_tel"]').send_keys("15013687199")
        self.driver.find_element_by_xpath('//*[@id="iagree"]').click()
        self.driver.find_element_by_xpath('//*[@id="submit_btn"]').click()
        sleep(6)
