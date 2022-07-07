from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from utilities.custom_logger import customLogger
from traceback import print_stack


class SeleniumDriver():

    log = customLogger()

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'class':
            return By.CLASS_NAME
        elif locatorType == 'link':
            return By.LINK_TEXT
        else:
            self.log.debug("Locator type ", locatorType, " not correct/supported")
        return False

    def getElement(self, locatorType, locator):
        element = None

        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info('Element found with locator: ', locator, ' and locator type: ', locatorType)
        except:
            self.log.info('Element not found with locator: ', locator, ' and locator type: ', locatorType)
        return element

    def getElements(self, locatorType, locator):
        elements = []

        try:
            locatorType = locatorType.lower()
            byType = self.getByType()
            elements = self.driver.find_elements(byType, locator)
            self.log.info('Elements found with locator: ', locator, ' and locator type: ', locatorType)
        except:
            self.log.info('Elements not found with locator: ', locator, ' and locator type: ', locatorType)
        return elements

    def clickElement(self, locatorType, locator):
        try:
            element = self.getElement(locatorType, locator)
            element.click()
            self.log.info('Clicked on element with locator: ' , locator , ' locatorType: ' , locatorType)
        except:
            self.log.info('Cannot click on the element with locator: ' , locator , ' locatorType: ' , locatorType)
            print_stack()

    def sendKeys(self, data, locatorType, locator):
        try:
            element = self.getElement(locatorType, locator)
            element.send_keys(data)
            self.log.info('Sent data on element with locator: ' , locator , ' locatorType: ' , locatorType)
        except:
            self.log.info('Cannot send data on the element with locator: ' , locator , ' locatorType: ' , locatorType)
            print_stack()

    def isElementPresent(self, locatorType, locator):
        try:
            element = self.getElement(locatorType, locator)
            if element is not None:
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False
 
    def waitForElement(self, locatorType, locator, timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: ", str(timeout), " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                ignored_exceptions=[NoSuchElementException,
                                                    ElementNotVisibleException,
                                                    ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable(byType, locator))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element
