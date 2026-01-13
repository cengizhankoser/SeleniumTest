from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    remove_button = (By.XPATH, "//button[contains(@data-test,'remove-sauce-labs-')]")
    checkout_button = (By.ID, "checkout")
    item_name = (By.CLASS_NAME, "inventory_item_name")

    def get_item_name(self):
        return self.get_text(self.item_name)
    
    def click_remove_button(self):
        self.click(self.remove_button)
    
    def click_checkout_button(self):
        self.click(self.checkout_button)

