from drive import Drive
from pages.prod_list_page import ProdListPage
from pages.cart_page import CartPage
import allure
import time


@allure.issue('https://github.com/Test-Automation-Crash-Course-24-10-22/team_03/issues/4',
              "Removing Product Item from Cart")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""Verifying the user's ability to open the Cart via the text 'Вже в кошику' in the product 
overview, remove one product item from the cart, & inability to remove all of them by using the '-' button""")
class RemItem(Drive):
    @allure.step("Adding two items of any product to the cart")
    def add_two_items(self, l_p, c_p):
        l_p.cart_button_click()  # Clicking on cart-button
        l_p.cart_icon()  # Clicking on cart icon
        c_p.plus_click()  # Clicking on plus

    @allure.step("Checking if minus is inactive")
    def check_minus_color(self, m_s_c):
        self.assertEqual(m_s_c, 'rgba(166, 165, 165, 1)')

    @allure.step("Checking if quantity equals 1")
    def check_quantity(self, quantity):
        self.assertEqual(quantity, 1)

    @allure.step("Checking if first product price equals order price")
    def check_price(self, price, order):
        self.assertEqual(price, order)

    @allure.step("Checking that nothing changes after clicking on minus")
    def check_changes(self, m_s_n, m_s, q_n, q, p_n, p, o_n, o):
        self.assertEqual(m_s_n, m_s)
        self.assertEqual(q_n, q)
        self.assertEqual(p_n, p)
        self.assertEqual(o_n, o)

    def test_rem_item(self):
        prod_list_page = ProdListPage(self.driver)
        cart_page = CartPage(self.driver)
        prod_list_page.open()
        time.sleep(3)
        self.add_two_items(prod_list_page, cart_page)
        time.sleep(3)
        # Clicking on minus
        cart_page.minus_click()
        time.sleep(3)
        # Getting minus color
        minus_symb_color = cart_page.get_minus_color()
        # Checking if minus is inactive
        self.check_minus_color(minus_symb_color)
        # Checking if quantity equals 1
        quantity = cart_page.get_first_product_quantity()
        self.check_quantity(quantity)
        # Checking if first product price equals order price
        price = cart_page.get_first_product_price()
        order = cart_page.get_order_price()
        self.check_price(price, order)
        # Clicking on minus again
        cart_page.minus_click()
        time.sleep(3)
        # Checking that nothing changes after clicking on minus
        minus_symb_new = cart_page.get_minus_color()
        quantity_new = cart_page.get_first_product_quantity()
        price_new = cart_page.get_first_product_price()
        order_new = cart_page.get_order_price()
        self.check_changes(minus_symb_new, minus_symb_color, quantity_new, quantity, price_new, price, order_new, order)