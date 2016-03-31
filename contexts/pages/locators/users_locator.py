from abstract_locator import AbstractLocator
from abc import ABCMeta
from selenium.webdriver.common.by import By


class UsersPageLocator(AbstractLocator):
    __metaclass__ = ABCMeta
    NEW_USER = (By.CLASS_NAME, "name")
    NEW_USER_CHECKBOX = (By.CLASS_NAME, "customer")
    GROUP_SELECTOR = (By.ID, "bulk-action-selector-top")
    APPLY_BUTTON = (By.ID, "doaction")
    USERS = (By.CLASS_NAME, 'username')
