from drive import Drive
from pages.prod_list_page import ProductListPage
from pages.cart_page import CartPage
from selenium.webdriver.support import expected_conditions


# Removing Product from the Cart
class RemItem(Drive):
    """Verifying the user's ability to open the Cart via the text 'Вже в кошику' in the product overview,
        remove one product item from the cart, & inability to remove all of them by using the '-' button"""
    def test_rem_item(self):
        self.driver.get(ProductListPage.page)
        self.driver.implicitly_wait(3)
        # Adding two items of any product to the cart
        buy = self.wait.until(expected_conditions.element_to_be_clickable(ProductListPage.first_prod_cart_button))
        buy.click()
        cart = self.wait.until(expected_conditions.element_to_be_clickable(ProductListPage.cart_icon))
        cart.click()
        plus = self.wait.until(expected_conditions.element_to_be_clickable(CartPage.plus_button))
        plus.click()
        # Clicking on minus
        minus = self.wait.until(expected_conditions.element_to_be_clickable(CartPage.minus_button))
        minus.click()
        self.driver.implicitly_wait(3)
        minus_symb_color = self.driver.find_element(CartPage.minus_button_symbol[0], CartPage.minus_button_symbol[1]).\
            value_of_css_property('color')
        # Checking if minus is inactive
        self.assertEqual(minus_symb_color, 'rgba(166, 165, 165, 1)')
        quantity = int(self.wait.until(expected_conditions.presence_of_element_located(CartPage.first_prod_quantity)).get_attribute('value'))
        # Checking if quantity equals 1
        self.assertEqual(quantity, 1)
        price = self.wait.until(expected_conditions.presence_of_element_located(CartPage.first_prod_price)).text.split(" ", 2)
        price = int(''.join(price[:len(price) - 1]))
        order_price = int(self.wait.until(expected_conditions.presence_of_element_located(CartPage.order_price)).text)
        # Checking if first product price equals order price
        self.assertEqual(price, order_price)
        # Clicking on minus again
        minus.click()
        minus_symb_new = self.driver.find_element(CartPage.minus_button_symbol[0], CartPage.minus_button_symbol[1]). \
            value_of_css_property('color')
        quantity_new = int(self.wait.until(expected_conditions.presence_of_element_located(CartPage.first_prod_quantity)).get_attribute('value'))
        price_new = self.wait.until(expected_conditions.presence_of_element_located(CartPage.first_prod_price)).text.split(" ", 2)
        price_new = int(''.join(price_new[:len(price_new) - 1]))
        order_price_new = int(self.wait.until(expected_conditions.presence_of_element_located(CartPage.order_price)))
        # Checking that nothing changes after clicking on minus
        self.assertEqual(minus_symb_new, minus_symb_color)
        self.assertEqual(quantity_new, quantity)
        self.assertEqual(price_new, price)
        self.assertEqual(order_price_new, order_price)