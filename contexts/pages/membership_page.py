from abstract_page import AbstractPage
from locators.membership_page_loc import MembershipPageLocator


class MembershipPage(AbstractPage):
    def create_membership(self):
        element = self.driver.find_element(*MembershipPageLocator.CREATE_MEMB_BUTTON)
        element.click()
