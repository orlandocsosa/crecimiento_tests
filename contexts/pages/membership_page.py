from abstract_page import AbstractPage
from locators.membership_page_loc import MembershipPageLocator


class MembershipPage(AbstractPage):
    def create_membership(self):
        element = self.driver.find_element(*MembershipPageLocator.CREATE_MEMB_BUTTON)
        element.click()

    def click_pop_up_finish(self):
        elements = self.driver.find_elements(*MembershipPageLocator.POP_UP_MEMBERSHIP)
        element = elements[0]
        element.click()

    def get_new_membership_name(self):
        elements = self.driver.find_elements(*MembershipPageLocator.MEMBERSHIP_NAME)
        element = elements[len(elements) - 1]
        return element

