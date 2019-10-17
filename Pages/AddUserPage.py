from BasicMethod.GadgetTree import Base
import Pages


class Add_user_page(Base):
    def __init__(self, driver):
        super.__init__(driver)

    def click_add_btn(self):
        self.click_add_btn(Pages.add_user)

    def click_save_local(self):
        self.click_element(Pages.save_local)

    def get_user_list(self):
        user_data = self.find_elements_o(Pages.user_text)
        return [x.text for x in user_data]

    def input_user_info(self, name, phone):
        self.input_text(Pages.send_name, name)
        self.input_text(Pages.send_phone, phone)
        self.click_element(Pages.click_save_back)
        if not self.is_element_disappear(Pages.usr_edit_btn):
            self.driver.keyevent(4)
