from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    assert inventory.is_loaded()


def test_invalid_login_shows_error(driver):
    login = LoginPage(driver)
    login.open()
    login.login("wrong_user", "wrong_pass")

    assert "Username and password do not match" in login.get_error_message()