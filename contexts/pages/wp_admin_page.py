from abstract_page import AbstractPage
from locators.wp_admin_loc import WpAdminLocator
from selenium.webdriver.common.action_chains import ActionChains


class WpAdminPage(AbstractPage):
    def hover_user(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        elements = self.driver.find_elements(*WpAdminLocator.USERS)
        element = elements[17]
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def click_membership(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        elements = self.driver.find_elements(*WpAdminLocator.USERS)
        element = elements[21]
        element.click()

    def click_new_user(self):
        element = self.driver.find_element(*WpAdminLocator.NEW)
        element.click()

    def click_all_users(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        elements = self.driver.find_elements(*WpAdminLocator.USERS)
        element = elements[17]
        element.click()

    def click_users(self):
        self.hover_user()
        self.wait(5)
        self.click_new_user()
