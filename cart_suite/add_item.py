from drive import Drive
from pages.prod_list_page import ProductListPage
from pages.prod_page import ProductPage
from pages.cart_page import CartPage
from selenium.webdriver.support import expected_conditions


# Verifying the user's ability to add another available product item to the Cart & closure of pop-up via the cross
class AddItem(Drive):
    def test_add_item(self):
        self.driver.get(ProductListPage.page)
        self.driver.implicitly_wait(3)
        # Clicking on product's image to open product's page
        av_prod_a = self.wait.until(expected_conditions.element_to_be_clickable(ProductListPage.product_image))
        av_prod_a.click()
        # Clicking 'Купити' button
        buy = self.wait.until(expected_conditions.element_to_be_clickable(ProductPage.buy_button))
        buy.click()
        self.driver.get(ProductListPage.page)
        self.waitDocLoad()
        # Opening the product page again
        av_prod_a = self.wait.until(expected_conditions.element_to_be_clickable(ProductListPage.product_image))
        av_prod_a.click()
        # Clicking on the text 'В кошику'
        cart = self.wait.until(expected_conditions.element_to_be_clickable(ProductPage.in_cart_text))
        cart.click()
        price_for_one = int(self.wait.until(expected_conditions.presence_of_element_located(CartPage.order_price)).text)
        # Clicking on plus
        plus = self.wait.until(expected_conditions.element_to_be_clickable(CartPage.plus_button))
        plus.click()
        quantity = int(self.wait.until(expected_conditions.presence_of_element_located(CartPage.first_prod_quantity)).get_attribute('value'))
        # Checking if quantity equals 2
        self.assertEqual(quantity, 2)
        self.driver.implicitly_wait(3)
        price_for_two = int(self.wait.until(expected_conditions.presence_of_element_located(CartPage.order_price)).text)
        # Checking the order price correct
        self.assertEqual(price_for_two, price_for_one * 2)
        # Closing cart pop-up via cross
        cross = self.wait.until(expected_conditions.element_to_be_clickable(CartPage.cross))
        cross.click()
        quantity = int(self.wait.until(expected_conditions.presence_of_element_located(ProductPage.counter_icon)).text)
        # Checking the counter icon
        self.assertEqual(quantity, 2)
