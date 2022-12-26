from drive import Drive
from pages.prod_list_page import ProdListPage
from pages.prod_page import ProdPage
import allure
import time


@allure.issue('https://github.com/Test-Automation-Crash-Course-24-10-22/team_03/issues/1',
              "Adding Available Product to the Cart")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""Verifying the user's ability to add one available product item to the Cart & closure of Cart 
pop-up via the button""")
class AddProduct(Drive):
    @allure.step("Checking if the counter icon equals 1")
    def check_quantity(self, quantity):
        self.assertEqual(quantity, 1)

    def test_add_product(self):
        prod_list_page = ProdListPage(self.driver)
        prod_page = ProdPage(self.driver)
        prod_list_page.open()
        time.sleep(3)
        # Clicking on product
        prod_list_page.prod_click()
        # Clicking on buy button
        prod_page.buy_button_click()
        # Close via continue button
        prod_page.con_button_click()
        # Checking the counter icon
        quantity = prod_page.get_counter()
        self.check_quantity(quantity)

