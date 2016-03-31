from abstract_page import AbstractPage
from locators.confirm_erase_loc import ConfirmEraseLocator
from selenium.webdriver.common.keys import Keys


class ConfirmErasePage(AbstractPage):
    def confirm_erase(self):
        element = self.driver.find_element(*ConfirmEraseLocator.CONFIRM_ERASE_BUTTON)
        element.click()
