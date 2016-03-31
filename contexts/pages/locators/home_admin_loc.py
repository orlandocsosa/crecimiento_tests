from abstract_locator import AbstractLocator
from abc import ABCMeta
from selenium.webdriver.common.by import By


class HomeAdminLocator(AbstractLocator):
    __metaclass__ = ABCMeta
    USERNAME = (By.ID, "wp-admin-bar-site-name")

