from drive import Drive
from pages.prod_list_page import ProdListPage
from pages.prod_page import ProdPage
from pages.cart_page import CartPage
import allure
import time


@allure.issue('https://github.com/Test-Automation-Crash-Course-24-10-22/team_03/issues/2',
              "Adding Second Product Item to the Cart")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""Verifying the user's ability to add another available product item to the Cart & closure of 
pop-up via the cross""")
class AddItem(Drive):
    @allure.step("Checking if the first product quantity equals 2")
    def check_first_prod_quantity(self, quantity):
        self.assertEqual(quantity, 2)

    @allure.step("Checking if the price for two equals 2 price for one multiplied by two")
    def check_price(self, price_for_two, price_for_one):
        self.assertEqual(price_for_two, price_for_one * 2)

    @allure.step("Checking if the counter icon equals 2")
    def check_quantity(self, quantity):
        self.assertEqual(quantity, 2)

    def test_add_item(self):
        prod_list_page = ProdListPage(self.driver)
        prod_page = ProdPage(self.driver)
        cart_page = CartPage(self.driver)
        prod_list_page.open()
        time.sleep(3)
        # Clicking on product
        prod_list_page.prod_click()
        # Clicking on buy button
        prod_page.buy_button_click()
        # Opening the product page again
        prod_page.open()
        time.sleep(3)
        # Opening the cart
        prod_page.cart_text_click()
        price_for_one = cart_page.get_order_price()
        # Clicking on plus
        cart_page.plus_click()
        time.sleep(3)
        # Checking if the first product quantity equals 2
        quantity = cart_page.get_first_product_quantity()
        self.check_first_prod_quantity(quantity)
        # Checking if the price per two equals 2 price per one multiplied by two
        price_for_two = cart_page.get_order_price()
        self.check_price(price_for_two, price_for_one)
        # Closing cart pop-up via cross
        cart_page.cross_click()
        # Checking the counter icon
        quantity = prod_page.get_counter()
        self.check_quantity(quantity)
