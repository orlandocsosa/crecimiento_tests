from abstract_page import AbstractPage
from locators.admin_login_loc import AdminLoginLocator


class AdminLoginPage(AbstractPage):
    def enter_username_text(self, text):
        element = self.driver.find_element(*AdminLoginLocator.USERNAME)
        element.send_keys(text)

    def enter_password_text(self, text):
        element = self.driver.find_element(*AdminLoginLocator.PASSWORD)
        element.send_keys(text)

    def click_submit(self):
        element = self.driver.find_element(*AdminLoginLocator.LOG_IN)
        elements = self.driver.find_elements(*AdminLoginLocator.NAV_BAR)
        element1 = elements[0]
        self.adjustedClick(element,element1)

    def go(self):
        self.driver.get("http://crecimientototal.com/beta/account-2/")

    def login(self):
        self.enter_username_text('admin')
        self.enter_password_text('****') #update with password
        self.click_submit()
