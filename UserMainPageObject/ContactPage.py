from time import sleep


class ContactPage:
    def __init__(self,driver):
        self.driver = driver

    def AddMember(self):
        elements = self.driver.find_elements_by_xpath('//*[@class="qui_btn ww_btn js_add_member"]')
        print(len(elements))
        elements[1].click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("特瑞")
        self.driver.find_element_by_xpath('//*[@id="memberAdd_english_name"]').send_keys("Terry")
        self.driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys("terry1234456")
        self.driver.find_element_by_xpath('//*[@class="ww_radio" and @value="1"]').click()
        self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys("13412345788")
        self.driver.find_element_by_xpath('//*[@id="memberAdd_title"]').send_keys("测试工程师")
        self.driver.find_elements_by_xpath('//*[@class="qui_btn ww_btn ww_btn_Blue js_btn_continue"]')[1].click()