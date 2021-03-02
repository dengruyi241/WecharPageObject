from time import sleep

from selenium import webdriver

from UserMainPageObject.ContactPage import ContactPage


class UserMainPage:
    def __init__(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address= "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options= chrome_args)
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")


    def goto_contact(self):
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()
        sleep(1)

        return ContactPage(self.driver)

    def goto_App_Manage(self):
        pass

    def goto_customer(self):
        pass

    def goto_manage_tools(self):
        pass

    def goto_profile(self):
        pass