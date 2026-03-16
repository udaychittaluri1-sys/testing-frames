from selenium.webdriver.common.by import By


# LOGIN
EMAIL = (By.NAME, "email")
PASSWORD = (By.NAME, "password")
LOGIN_BTN = (By.XPATH, "//button[@type='Sign In']")
LOGIN_ERROR = (By.XPATH, "//p[contains(@class,'error')]")

# DASHBOARD
DASHBOARD_HEADER = (By.XPATH, "//h1")

# NAVIGATION
NAV_USERS = (By.XPATH, "//button[contains(.,'Users')]")
NAV_PROJECTS = (By.XPATH, "//button[contains(.,'Projects')]")
NAV_TASKS = (By.XPATH, "//button[contains(.,'Tasks')]")
NAV_SCENARIOS = (By.XPATH, "//button[contains(.,'Test Scenarios')]")

# USERS
USERS_TABLE = (By.XPATH, "//table")

# PROJECTS
CREATE_PROJECT = (By.XPATH, "//button[contains(.,'Create')]")
PROJECT_NAME = (By.XPATH, "//input")
PROJECT_DESC = (By.XPATH, "//textarea")
SAVE_PROJECT = (By.XPATH, "//button[contains(.,'Save')]")
SEARCH_PROJECT = (By.XPATH, "//input[contains(@placeholder,'Search')]")

# TASKS
TASK_STATUS = (By.XPATH, "//select")
UPDATE_TASK = (By.XPATH, "//button[contains(.,'Update')]")

# TEST SCENARIOS
ALERT_BTN = (By.XPATH, "//button[contains(.,'Alert')]")
CONFIRM_BTN = (By.XPATH, "//button[contains(.,'Confirm')]")
PROMPT_BTN = (By.XPATH, "//button[contains(.,'Prompt')]")

IFRAME = (By.XPATH, "//iframe")

NEW_TAB = (By.XPATH, "//button[contains(.,'New Tab')]")
POPUP = (By.XPATH, "//button[contains(.,'Popup')]")