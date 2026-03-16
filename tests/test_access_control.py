from pages.login_page import LoginPage
from pages.users_page import UsersPage

def test_admin_users_access(driver):

    login=LoginPage(driver)
    login.login("admin@example.com","Admin@123")

    users=UsersPage(driver)

    users.open_users()

    assert users.verify_users_table()

def test_non_admin_users_access(driver):
    login=LoginPage(driver)
    login.login("john@example.com","John@123")
    users=UsersPage(driver)
    users.open_users()
    assert users.verify_users_table()
    