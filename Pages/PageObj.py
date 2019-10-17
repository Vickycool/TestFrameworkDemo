from Pages.AddUserPage import Add_user_page


class PageObj:
    def __init__(self, driver):
        self.driver = driver

    def return_AddUserPage(self):
        return Add_user_page(self.driver)