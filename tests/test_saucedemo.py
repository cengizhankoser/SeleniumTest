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
    assert TestData.inventory_html in driver.current_url
    assert inventory_page.get_title() == TestData.inventory_page_title

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

#Hem eklenen item sayısı sağ üstteki sepet'teki sayıyla aynı olup olmadığına, hem de add to cart butonuna basınca buton remove'a dönüşüp dönüşmediğine bakıyoruz.
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
        assert current_buttons[index].text == TestData.remove_from_cart

def test_remove_item_from_cart(driver):
    login_page = LoginPage(driver)
    login_page.driver.get(TestData.base_url)
    login_page.login(TestData.correct_username, TestData.correct_password)

    inventory_page = InventoryPage(driver)
    
    selected_indices = inventory_page.add_random_items_to_cart()
    initial_count = len(selected_indices)
    
    assert inventory_page.get_cart_badge_count() == str(initial_count)
    index_to_remove = selected_indices[0]

    current_buttons = inventory_page.get_add_to_cart_buttons()
    
    current_buttons[index_to_remove].click()

    updated_buttons = inventory_page.get_add_to_cart_buttons()
    assert updated_buttons[index_to_remove].text == TestData.add_to_cart

    expected_count = initial_count - 1

    if expected_count > 0:
        assert inventory_page.get_cart_badge_count() == str(expected_count)
    else:
        badges = driver.find_elements(*inventory_page.cart_badge)
        assert len(badges) == 0



def test_shopping_cart_link(driver):
    login_page = LoginPage(driver)
    login_page.driver.get(TestData.base_url)
    login_page.login(TestData.correct_username, TestData.correct_password)

    inventory_page = InventoryPage(driver)
    inventory_page.click_cart_link()

    cart_page = CartPage(driver)

    assert TestData.cart_html in driver.current_url
    assert cart_page.get_title() == TestData.cart_page_title

    
def test_continue_shopping_button(driver):
    login_page = LoginPage(driver)
    login_page.driver.get(TestData.base_url)
    login_page.login(TestData.correct_username, TestData.correct_password)

    inventory_page = InventoryPage(driver)
    inventory_page.click_cart_link()

    cart_page = CartPage(driver)
    cart_page.click_continue_shopping_button()

    assert TestData.inventory_html in driver.current_url
    assert inventory_page.get_title() == TestData.inventory_page_title
"""

def test_cart_page_remove_button(driver):
    login_page = LoginPage(driver)
    login_page.driver.get(TestData.base_url)
    login_page.login(TestData.correct_username, TestData.correct_password)


    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    selected_indices = inventory_page.add_random_items_to_cart()
    num_of_items_on_cart = len(selected_indices)
    assert inventory_page.get_cart_badge_count() == str(num_of_items_on_cart)

    inventory_page.click_cart_link()
    
    item_num_on_cart_page = cart_page.get_cart_item_count()
    assert cart_page.get_cart_badge_count() == str(num_of_items_on_cart)
    assert item_num_on_cart_page == num_of_items_on_cart 

    cart_page.click_remove_button()
    expected_count = num_of_items_on_cart - 1
    current_items_count = cart_page.get_cart_item_count()
    assert current_items_count == expected_count
    assert cart_page.get_cart_badge_count() == str(expected_count)





