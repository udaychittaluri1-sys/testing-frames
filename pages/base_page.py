from utils.wait_utils import wait_visible, wait_clickable

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):

        element = wait_clickable(self.driver, locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element
        )

        element.click()

    def type(self, locator, text):

        element = wait_visible(self.driver, locator)

        element.clear()

        element.send_keys(text)

    def text(self, locator):

        return wait_visible(self.driver, locator).text