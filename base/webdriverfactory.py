from selenium import webdriver
import traceback

class WebDriverfactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseURL = "https://www.saucedemo.com/"

        if self.browser == 'chrome':
            driver = webdriver.Chrome()
        # won't work
        elif self.browser == 'firefox':
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()
        
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseURL)

        return driver
