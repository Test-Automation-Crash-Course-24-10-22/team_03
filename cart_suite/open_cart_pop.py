from drive import Drive
from pages.prod_list_page import ProductListPage
from pages.cart_page import CartPage
from selenium.webdriver.support import expected_conditions


# Verifying the user's ability to open the Cart via a Pop-up message
class OpenCartPop(Drive):
    def test_pop_up(self):
        self.driver.get(ProductListPage.page)
        self.driver.implicitly_wait(3)
        # Clicking on cart button
        buy = self.wait.until(expected_conditions.element_to_be_clickable(ProductListPage.first_prod_cart_button))
        buy.click()
        # Clicking on pop-up message
        cart = self.wait.until(expected_conditions.presence_of_element_located(ProductListPage.pop_up_message))
        cart.click()
        header = self.wait.until(expected_conditions.presence_of_element_located(CartPage.page_header)).text
        # Checking if page heading is 'Кошик'
        self.assertEqual(header, 'Кошик')
