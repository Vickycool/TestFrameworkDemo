from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def find_element_o(self, loc, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll) \
            .until(lambda x: x.find_element(*loc))

    def find_elements_o(self, loc, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll)\
            .until(lambda x: x.find_elements(*loc))

    def is_element_disappear(self, loc, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll)\
            .until_not(lambda x: x.find_element(*loc).is_displayed())

    def click_element(self, loc):
        self.find_elements_o(loc).click()

    def input_text(self, loc, text):
        elem = self.find_element_o(loc)
        elem.clear()
        elem.send_keys(text)

