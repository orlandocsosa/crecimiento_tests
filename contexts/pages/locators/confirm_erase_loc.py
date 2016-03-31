from abstract_locator import AbstractLocator
from abc import ABCMeta
from selenium.webdriver.common.by import By


class ConfirmEraseLocator(AbstractLocator):
    __metaclass__ = ABCMeta
    CONFIRM_ERASE_BUTTON = (By.ID, "submit")
