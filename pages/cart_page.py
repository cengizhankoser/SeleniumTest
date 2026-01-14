from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    remove_button = (By.XPATH, "//button[contains(@data-test,'remove-sauce-labs-')]")
    checkout_button = (By.ID, "checkout")
    item_name = (By.CLASS_NAME, "inventory_item_name")
    title = (By.CLASS_NAME, "title")
    continue_shopping_button = (By.ID, "continue-shopping")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    cart_item = (By.CLASS_NAME, "cart_item")


    def get_item_name(self):
        return self.get_text(self.item_name)
    
    def click_remove_button(self):
        self.click(self.remove_button)
    
    def click_checkout_button(self):
        self.click(self.checkout_button)
    
    def get_title(self):
        return self.get_text(self.title)
    
    def click_continue_shopping_button(self):
        self.click(self.continue_shopping_button)
    
    def get_cart_badge_count(self):
        return self.get_text(self.cart_badge)
    
    def get_cart_item_count(self):
        return len(self.find_elements(self.cart_item))


