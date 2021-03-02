from LoginPageObject.main import MainPage


class TestMainPage:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()

    def test_login(self):
        login_page = self.main.goto_login()
        login_page.login()
        login_page.goto_register()

    def test_register(self):
        self.main.goto_register().RegisterAccount()