from abstract_page import AbstractPage
from locators.new_user_loc import NewUserLocator
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class NewUserPage(AbstractPage):
    def fill_user_name(self, text):
        element = self.driver.find_element(*NewUserLocator.USER)
        element.send_keys(text)

    def fill_email(self, text):
        element = self.driver.find_element(*NewUserLocator.EMAIL)
        element.send_keys(text)

    def fill_name(self, text):
        element = self.driver.find_element(*NewUserLocator.NAME)
        element.send_keys(text)

    def fill_last_name(self, text):
        element = self.driver.find_element(*NewUserLocator.LAST_NAME)
        element.send_keys(text)

    def password(self, text):
        elements = self.driver.find_elements(*NewUserLocator.SHOW_PASS)
        element = elements[0]
        element1 = self.driver.find_element(*NewUserLocator.ADMIN_BAR)
        self.adjustedClick(element, element1)
        element_two = self.driver.find_element(*NewUserLocator.PASS)
        self.wait(1)
        element_two.click()
        element_two.send_keys(Keys.CONTROL + 'a')
        element_two.send_keys(Keys.BACKSPACE)
        element_two.send_keys(text)
        weak_pass = self.driver.find_element(*NewUserLocator.CONFIRM_PASS)
        weak_pass.click()

    def click_user_notif(self):
        element = self.driver.find_element(*NewUserLocator.USER_NOTIF)
        element.click()

    def click_confirm_user(self):
        element = self.driver.find_element(*NewUserLocator.CREATE)
        element.click()

    def fill_form(self):
        self.wait(5)
        self.fill_user_name('orlando85')
        self.fill_email('orlandocsosa@gmail.com')
        self.fill_name('Orlando')
        self.fill_last_name('Sosa')
        self.password('Orlando123')
        self.click_user_notif()
        self.click_confirm_user()
