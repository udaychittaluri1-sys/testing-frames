from pages.base_page import BasePage
from config.locators import *

class UsersPage(BasePage):

    def open_users(self):

        self.click(NAV_USERS)

    def verify_users_table(self):

        return self.driver.find_element(*USERS_TABLE).is_displayed()