from abstract_locator import AbstractLocator
from abc import ABCMeta
from selenium.webdriver.common.by import By


class MembershipPageLocator(AbstractLocator):
    __metaclass__ = ABCMeta
    CREATE_MEMB_BUTTON = (By.ID,'create_new_ms_button')
    POP_UP_MEMBERSHIP = (By.CLASS_NAME,'button-primary')
    MEMBERSHIP_NAME = (By.CLASS_NAME,'the-name')
