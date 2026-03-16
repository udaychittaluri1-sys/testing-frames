from pages.base_page import BasePage
from config.locators import *
from utils.wait_utils import wait_page_loaded

class LoginPage(BasePage):

 def login(self,email,password):
    self.type(EMAIL,email)
    self.type(PASSWORD,password)
    self.click(LOGIN_BTN)

    wait_page_loaded(self.driver)