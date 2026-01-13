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
    
    def get_button_text(self, button):
        return button.text

    def get_add_to_cart_buttons(self):
        return self.find_elements(self.add_to_cart_button)
    
    def add_item_to_cart(self):
        self.click(self.add_to_cart_button)

    def add_random_items_to_cart(self):
        buttons = self.find_elements(self.add_to_cart_button)
        all_indices = list(range(len(buttons)))
        count = random.randint(1, len(buttons))
        selected_indices = random.sample(all_indices, count)

        for index in selected_indices:
            buttons[index].click()

        
        return selected_indices

        
    def get_cart_badge_count(self):
        return self.get_text(self.cart_badge)
    
    def click_cart_link(self):
        self.click(self.cart_link)