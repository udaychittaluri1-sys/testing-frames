import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("email,password",[
("admin@test.com","wrong"),
("invalid@email.com","123"),
("","")
])
def test_invalid_login(driver,email,password):

    login=LoginPage(driver)
    login.login(email,password)

    assert "login" in driver.current_url