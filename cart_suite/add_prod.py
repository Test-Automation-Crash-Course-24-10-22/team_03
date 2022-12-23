from drive import Drive
from pages.prod_list_page import ProductListPage
from pages.prod_page import ProductPage
from selenium.webdriver.support import expected_conditions
import time


# Verifying the user's ability to add one available product item to the Cart & closure of Cart pop-up via the button
class AddProduct(Drive):
    def test_add_product(self):
        self.driver.get(ProductListPage.page)
        time.sleep(3)
        # Clicking on product's image to open product's page
        av_prod_a = self.wait.until(expected_conditions.element_to_be_clickable(ProductListPage.product_image))
        av_prod_a.click()
        # Clicking 'Купити' button
        buy = self.wait.until(expected_conditions.element_to_be_clickable(ProductPage.buy_button))
        buy.click()
        # Close via 'Продовжити покупки' button
        con = self.wait.until(expected_conditions.element_to_be_clickable(ProductPage.continue_button))
        con.click()
        quantity = int(self.wait.until(expected_conditions.presence_of_element_located(ProductPage.counter_icon)).text)
        # Checking the counter icon
        self.assertEqual(quantity, 1)
