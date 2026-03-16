import pytest
from utils.driver_factory import get_driver
from config.settings import BASE_URL
from utils.wait_utils import wait_page_loaded
from utils.screenshot_utils import capture_screenshot

@pytest.fixture
def driver():

    driver = get_driver()

    driver.get(BASE_URL)

    wait_page_loaded(driver)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        driver = item.funcargs["driver"]

        capture_screenshot(driver, item.name)