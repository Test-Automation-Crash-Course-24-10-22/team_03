from drive import Drive
from pages.prod_list_page import ProdListPage
from pages.cart_page import CartPage
import allure


@allure.issue('https://github.com/Test-Automation-Crash-Course-24-10-22/team_03/issues/5',
              "Opening the Cart via Pop-up message")
@allure.severity(allure.severity_level.MINOR)
@allure.description("""Verifying the user's ability to open the Cart via a Pop-up message""")
class OpenCartPop(Drive):
    @allure.step("Checking if header is correct")
    def check_header(self, header):
        self.assertEqual(header, 'Кошик')

    def test_pop_up(self):
        prod_list_page = ProdListPage(self.driver)
        cart_page = CartPage(self.driver)
        prod_list_page.open()
        self.driver.implicitly_wait(3)
        # Clicking on cart button
        prod_list_page.cart_button_click()
        # Clicking on pop-up message
        prod_list_page.pop_up_click()
        # Checking if header is correct
        header = cart_page.get_cart_header()
        self.check_header(header)
