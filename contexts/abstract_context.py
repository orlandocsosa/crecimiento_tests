from abc import ABCMeta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as SeleniumKeys
import unittest

class AbstractContext(unittest.TestCase):
    __metaclass__ = ABCMeta
    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Firefox()
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
