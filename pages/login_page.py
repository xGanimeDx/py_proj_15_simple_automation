from base.basepage import BasePage
from utilities.custom_logger import customLogger

class LoginPage(BasePage):

    log = customLogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _username_field = ''
    _password_field = ''
    _login_button = ''