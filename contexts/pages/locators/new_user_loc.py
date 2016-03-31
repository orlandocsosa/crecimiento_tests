from abstract_locator import AbstractLocator
from abc import ABCMeta
from selenium.webdriver.common.by import By


class NewUserLocator(AbstractLocator):
    __metaclass__ = ABCMeta
    USER = (By.ID, "user_login")
    EMAIL = (By.ID, "email")
    NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    SHOW_PASS = (By.CLASS_NAME, "wp-generate-pw")
    PASS = (By.ID, "pass1-text")
    CONFIRM_PASS = (By.NAME, "pw_weak")
    USER_NOTIF = (By.ID, "send_user_notification")
    CREATE = (By.ID, "createusersub")
    ADMIN_BAR = (By.ID, "wpadminbar")
