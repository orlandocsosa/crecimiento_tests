from abstract_page import AbstractPage
from locators.add_memebership_loc import AddMembershipLocator


class AddMembershipPage(AbstractPage):
    def click_dripped_memb(self):
        elements = self.driver.find_elements(*AddMembershipLocator.DRIPPED_CONTENT_RADIO)
        element = elements[1]
        element.click()

    def add_membership_name(self,name):
        element = self.driver.find_element(*AddMembershipLocator.MEMBERSHIP_NAME)
        element.send_keys(name)


