from abstract_page import AbstractPage
from locators.home_admin_loc import HomeAdminLocator


class HomeAdminPage(AbstractPage):
    def click_site_name(self):
        element = self.driver.find_element(*HomeAdminLocator.USERNAME)
        element.click()