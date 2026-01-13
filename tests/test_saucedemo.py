import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from data.test_data import TestData


"""

def test_login_correct(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.driver.get(TestData.base_url)
    login_page.login(TestData.correct_username, TestData.correct_password)
    assert "inventory.html" in driver.current_url
    assert inventory_page.get_title() == "Products"

def test_login_wrong_username(driver):
    login_page = LoginPage(driver)
    login_page.driver.get(TestData.base_url)
    login_page.login(TestData.wrong_username, TestData.correct_password)
    assert TestData.error_message in login_page.get_error_message()

def test_login_wrong_password(driver):
    login_page = LoginPage(driver)
    login_page.driver.get(TestData.base_url)
    login_page.login(TestData.correct_username, TestData.wrong_password)
    assert TestData.error_message in login_page.get_error_message()

def test_login_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.driver.get(TestData.base_url)
    login_page.login("",TestData.correct_password)
    assert TestData.username_required in login_page.get_error_message()

def test_login_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.driver.get(TestData.base_url)
    login_page.login(TestData.correct_username,"")
    assert TestData.password_required in login_page.get_error_message()
"""



def test_add_random_items_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.driver.get(TestData.base_url)
    login_page.login(TestData.correct_username, TestData.correct_password)

    inventory_page = InventoryPage(driver)
    selected_indices = inventory_page.add_random_items_to_cart()
    count = str(len(selected_indices))

    assert inventory_page.get_cart_badge_count() == str(count)

    current_buttons = inventory_page.get_add_to_cart_buttons()

    for index in selected_indices:
        assert current_buttons[index].text == "Remove"



