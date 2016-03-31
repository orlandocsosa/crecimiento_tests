from abstract_locator import AbstractLocator
from abc import ABCMeta
from selenium.webdriver.common.by import By


class AdminLoginLocator(AbstractLocator):
    __metaclass__ = ABCMeta
    USERNAME = (By.ID, "user_login")
    PASSWORD = (By.ID, "user_pass")
    LOG_IN = (By.ID, "wp-submit")
    NAV_BAR = (By.CLASS_NAME,'navbar')
