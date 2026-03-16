from pages.login_page import LoginPage
from pages.test_scenarios_page import ScenariosPage

def test_trigger_alerts(driver):

    login = LoginPage(driver)
    login.login("admin@example.com","Admin123")

    page = ScenariosPage(driver)

    page.open_page()

    page.handle_alert()

    page.handle_confirm()

    page.handle_prompt()
    assert "Alert handled" in driver.page_source
    
def test_accept_alert(driver):

    login = LoginPage(driver)
    login.login("admin@example.com","Admin123")

    page = ScenariosPage(driver)

    page.open_page()

    login = LoginPage(driver)
    login.login("admin@example.com","Admin123")
    page.open_page()

    page.handle_alert()

    assert "Alert handled" in driver.page_source

def test_trigger_confirm_and_dismiss(driver):

    login = LoginPage(driver)
    login.login("admin@example.com","Admin123")
    page = ScenariosPage(driver)
    page.open_page()
    page.handle_confirm(dismiss=True)
    assert "Confirm dismissed" in driver.page_source
    
    