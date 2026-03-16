from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_valid_admin_login(driver):

    login=LoginPage(driver)
    login.login("admin@example.com","Admin@123")

    dashboard=DashboardPage(driver)

    assert dashboard.verify_dashboard()