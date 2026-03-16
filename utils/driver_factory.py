from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import GRID_URL, HEADLESS

def get_driver():

    options = Options()

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1920,1080")

    if GRID_URL:
        driver = webdriver.Remote(
            command_executor=GRID_URL,
            options=options
        )
    else:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    driver.maximize_window()

    return driver