from drive import Drive
from pages.prod_list_page import ProductListPage
from pages.cart_page import CartPage
from selenium.webdriver.support import expected_conditions


# Removing Product from the Cart
class RemProduct(Drive):
    def test_rem_prod(self):
        self.driver.get(ProductListPage.page)
        self.driver.implicitly_wait(3)
        # Clicking on cart button
        buy = self.wait.until(expected_conditions.element_to_be_clickable(ProductListPage.first_prod_cart_button))
        buy.click()
        buy = self.wait.until(expected_conditions.element_to_be_clickable(ProductListPage.second_prod_cart_button))
        buy.click()
        # Clicking on cart icon
        cart = self.wait.until(expected_conditions.element_to_be_clickable(ProductListPage.cart_icon))
        cart.click()
        # Clicking on three dots button
        dots = self.wait.until(expected_conditions.element_to_be_clickable(CartPage.three_dots_button))
        dots.click()
        # Removing product
        rem = self.wait.until(expected_conditions.element_to_be_clickable(CartPage.remove_option))
        rem.click()
        self.driver.implicitly_wait(3)
        order_price = int(self.wait.until(expected_conditions.presence_of_element_located(CartPage.order_price)).text)
        price = self.wait.until(expected_conditions.presence_of_element_located(CartPage.first_prod_price)).text.split(" ", 2)
        price = int(''.join(price[:len(price) - 1]))
        # Checking if price is correct
        self.assertEqual(order_price, price)
        # Removing another product
        dots = self.wait.until(expected_conditions.element_to_be_clickable(CartPage.three_dots_button))
        dots.click()
        rem = self.wait.until(expected_conditions.element_to_be_clickable(CartPage.remove_option))
        rem.click()
        header = self.wait.until(expected_conditions.element_to_be_clickable(CartPage.empty_cart_header)).text
        # Checking if header is correct
        self.assertEqual(header, 'Кошик порожній')
        mes = self.wait.until(expected_conditions.element_to_be_clickable(CartPage.empty_cart_message)).text
        # Checking if message is correct
        self.assertEqual(mes, 'Але це ніколи не пізно виправити :)')