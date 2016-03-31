from abstract_locator import AbstractLocator
from abc import ABCMeta
from selenium.webdriver.common.by import By


class WpAdminLocator(AbstractLocator):
    __metaclass__ = ABCMeta
    USERS = (By.CLASS_NAME, "wp-menu-name")  # 17
    NEW = (By.PARTIAL_LINK_TEXT, "adir nuevo")
