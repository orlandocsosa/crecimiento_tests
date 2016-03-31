from abstract_page import AbstractPage
from locators.membership_page_loc import MembershipPageLocator
from selenium.webdriver.common.action_chains import ActionChains


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

    def hover_test_membership(self):
        elements = self.driver.find_elements(*MembershipPageLocator.MEMBERSHIP_NAME)
        element = elements[len(elements) - 1]
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def click_delete_test_membership(self):
        element = self.driver.find_element(*MembershipPageLocator.DELETE)
        element.click()

    def confirm_delete(self):
        elements = self.driver.find_elements(*MembershipPageLocator.CONFIRM_DELETE)
        element = elements[0]
        element.click()

    def get_count_memberships(self):
        elements = self.driver.find_elements(*MembershipPageLocator.MEMBERSHIP_ITEMS)
        return len(elements)

    def set_membership_name(self):
        return 'test'

    def erase_test_membership(self):
        element = self.set_membership_name()
        element2 = self.get_new_membership_name()
        if element == element2.text:
            self.hover_test_membership()
            self.wait(3)
            self.click_delete_test_membership()
            self.confirm_delete()
        else:
            self.driver.quit()
