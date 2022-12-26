from drive import Drive
from pages.prod_list_page import ProdListPage
from pages.cart_page import CartPage
import allure
import time


@allure.issue('https://github.com/Test-Automation-Crash-Course-24-10-22/team_03/issues/3',
              "Removing Product from the Cart")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""Verifying the user's ability to open the Cart via the text 'Вже в кошику' in the product overview,
        remove one product item from the cart, & inability to remove all of them by using the '-' button""")
class RemProduct(Drive):
    @allure.step("Checking if price is correct")
    def check_price(self, order_price, price):
        self.assertEqual(order_price, price)

    @allure.step("Checking if header is correct")
    def check_header(self, header):
        self.assertEqual(header, 'Кошик')

    @allure.step("Checking if message is correct")
    def check_message(self, mes):
        self.assertEqual(mes, 'Але це ніколи не пізно виправити :)')

    def test_rem_prod(self):
        prod_list_page = ProdListPage(self.driver)
        cart_page = CartPage(self.driver)
        prod_list_page.open()
        time.sleep(3)
        # Clicking on cart button
        prod_list_page.cart_button_click()
        prod_list_page.cart_button_click2()
        # Clicking on cart icon
        prod_list_page.cart_icon()
        # Clicking on three dots button
        cart_page.first_product_dots_click()
        # Removing product
        cart_page.rem_option_click()
        time.sleep(3)
        # Checking if price is correct
        order_price = cart_page.get_order_price()
        price = cart_page.get_first_product_price()
        self.check_price(order_price, price)
        # Removing another product
        cart_page.first_product_dots_click()
        cart_page.rem_option_click()
        # Checking if header is correct
        header = cart_page.get_cart_header()
        self.check_header(header)
        # Checking if message is correct
        mes = cart_page.get_cart_message()
        self.check_message(mes)
