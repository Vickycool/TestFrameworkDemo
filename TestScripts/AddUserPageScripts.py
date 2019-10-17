from TestBase.InitializeTest import init_driver
from Pages.PageObj import PageObj
import pytest


class Test_Add_User:

    def setup_class(self):
        self.driver = init_driver()
        self.add_user_page_obj = PageObj(self.driver).return_AddUserPage()

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture()
    def add_user_button(self):
        self.add_user_page_obj.click_add_btn()

    @pytest.mark.usefixtures("add_user_button")
    @pytest.mark.parametrize("test_num, name, phone, expect", [()])
    def test_input_user_info(self, test_num, name, phone, expect):
        self.add_user_page_obj.input_user_info(name,phone)
        if test_num == "test_001":
            assert expect not in self.add_user_page_obj.get_user_list()
        else:
            assert expect in self.add_user_page_obj.get_user_list()