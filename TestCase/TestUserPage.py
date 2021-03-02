from UserMainPageObject.UserMainPage import UserMainPage


class TestUserMainPage:
    def test_add_member(self):
        user_main_page = UserMainPage()
        contact_page = user_main_page.goto_contact()
        contact_page.AddMember()
