from pages.base_page import BasePage
from config.locators import *

class DashboardPage(BasePage):

    def verify_dashboard(self):
        return self.text(DASHBOARD_HEADER)