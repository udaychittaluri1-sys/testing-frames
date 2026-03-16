from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import EXPLICIT_WAIT

def wait_visible(driver, locator):
    return WebDriverWait(driver, EXPLICIT_WAIT).until(
        EC.visibility_of_element_located(locator)
    )

def wait_clickable(driver, locator):
    return WebDriverWait(driver, EXPLICIT_WAIT).until(
        EC.element_to_be_clickable(locator)
    )

def wait_present(driver, locator):
    return WebDriverWait(driver, EXPLICIT_WAIT).until(
        EC.presence_of_element_located(locator)
    )

def wait_page_loaded(driver):
    WebDriverWait(driver, EXPLICIT_WAIT).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )