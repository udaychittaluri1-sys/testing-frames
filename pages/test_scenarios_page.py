from pages.base_page import BasePage
from config.locators import *

class ScenariosPage(BasePage):

    def open_page(self):

        self.click(NAV_SCENARIOS)

    def handle_alert(self):

        self.click(ALERT_BTN)

        alert = self.driver.switch_to.alert

        alert.accept()

    def handle_confirm(self):

        self.click(CONFIRM_BTN)

        self.driver.switch_to.alert.dismiss()

    def handle_prompt(self):

        self.click(PROMPT_BTN)

        alert = self.driver.switch_to.alert

        alert.send_keys("test")

        alert.accept()

    def handle_iframe(self):

        iframe = self.driver.find_element(*IFRAME)

        self.driver.switch_to.frame(iframe)

        self.driver.switch_to.default_content()

    def handle_tabs(self):

        main = self.driver.current_window_handle

        self.click(NEW_TAB)

        for window in self.driver.window_handles:

            if window != main:

                self.driver.switch_to.window(window)

                self.driver.close()

        self.driver.switch_to.window(main)