from selenium.webdriver.common.by import By
from .base_page import BasePage
import  random

class InventoryPage(BasePage):
    add_to_cart_button = (By.CLASS_NAME, "btn_inventory")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    cart_link = (By.CLASS_NAME, "shopping_cart_link")
    title = (By.CLASS_NAME, "title")

    def get_title(self):
        return self.get_text(self.title)
    
    def add_item_to_cart(self):
        self.click(self.add_to_cart_button)

    def add_random_items_to_cart(self, count):
        buttons = self.find_elements(self.add_to_cart_button)
        random_buttons = random.sample(buttons, count)

        for button in random_buttons:
            button.click()

        
    def get_cart_badge_count(self):
        return self.get_text(self.cart_badge)
    
    def click_cart_link(self):
        self.click(self.cart_link)