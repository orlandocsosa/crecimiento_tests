from abstract_locator import AbstractLocator
from abc import ABCMeta
from selenium.webdriver.common.by import By


class AddMembershipLocator(AbstractLocator):
    __metaclass__ = ABCMeta
    DRIPPED_CONTENT_RADIO = (By.CLASS_NAME,'wpmui-radio')
    MEMBERSHIP_NAME = (By.ID,'name')
