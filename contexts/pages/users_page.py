from abstract_page import AbstractPage
from locators.users_locator import UsersPageLocator
from selenium.webdriver.common.keys import Keys


class UsersPage(AbstractPage):
    def get_new_user_name(self):
        elements = self.driver.find_elements(*UsersPageLocator.NEW_USER)
        element = elements[len(elements) - 1]
        return element

    def check_new_user_box(self):
        elements = self.driver.find_elements(*UsersPageLocator.NEW_USER_CHECKBOX)
        element = elements[len(elements) - 1]
        element.click()

    def erase_action_selected_users(self):
        element = self.driver.find_element(*UsersPageLocator.GROUP_SELECTOR)
        element.click()
        element.send_keys(Keys.ARROW_DOWN)
        element.click()

    def apply_button(self):
        element = self.driver.find_element(*UsersPageLocator.APPLY_BUTTON)
        element.click()

    def get_users(self):
        elements = self.driver.find_elements(*UsersPageLocator.USERS)
        return len(elements)

    def erase_created_user(self):
        self.check_new_user_box()
        self.erase_action_selected_users()
        self.apply_button()
