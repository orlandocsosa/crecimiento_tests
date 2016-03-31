from selenium import webdriver
from abc import ABCMeta
import time

class AbstractPage(object):
    __metaclass__ = ABCMeta

    def __init__(self, driver):
        self.driver = driver
        """:type : webdriver.Remote """

    def wait(self, secs):
        time.sleep(secs)


    def adjustedClick(self, element, blockingElement):
        self.driver.execute_script(""
                                   "arguments[0].scrollIntoView(true); "
                                   "window.scrollBy("
                                   "0,"
                                   "arguments[1].offsetHeight * -1"
                                   ")"
                                   "", element,blockingElement) #pasar elemento navbar como arg[1] !!!
        element.click()
