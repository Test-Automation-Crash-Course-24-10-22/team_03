from pages.page import Page
from locators.cart_page_locators import CartLocators
from selenium.webdriver.support import expected_conditions
import allure


class CartPage(Page):
    def __init__(self, driver):
        super(CartPage, self).__init__(driver)

    @allure.step("Getting order price")
    def get_order_price(self):
        return int(self.wait.until(expected_conditions.presence_of_element_located(CartLocators.order_price)).text)

    @allure.step("Getting first product quantity")
    def get_first_product_quantity(self):
        return int(self.wait.until(expected_conditions.presence_of_element_located(CartLocators.first_prod_quantity)).get_attribute('value'))

    @allure.step("Getting first product price")
    def get_first_product_price(self):
        price = self.wait.until(expected_conditions.presence_of_element_located(CartLocators.first_prod_price)).text.split(" ", 2)
        return int(''.join(price[:len(price) - 1]))

    @allure.step("Clicking on plus")
    def plus_click(self):
        plus = self.wait.until(expected_conditions.element_to_be_clickable(CartLocators.plus_button))
        self.driver.execute_script("arguments[0].click();", plus)

    @allure.step("Closing cart pop-up via cross")
    def cross_click(self):
        cross = self.wait.until(expected_conditions.element_to_be_clickable(CartLocators.cross))
        self.driver.execute_script("arguments[0].click();", cross)

    @allure.step("Getting page heading")
    def get_cart_header(self):
        return self.wait.until(expected_conditions.presence_of_element_located(CartLocators.page_header)).text

    @allure.step("Clicking on minus")
    def minus_click(self):
        minus = self.wait.until(expected_conditions.presence_of_element_located(CartLocators.minus_button))
        self.driver.execute_script("arguments[0].click();", minus)

    @allure.step("Getting minus color")
    def get_minus_color(self):
        return self.driver.find_element(CartLocators.minus_button_symbol[0], CartLocators.minus_button_symbol[1]).\
            value_of_css_property('color')

    @allure.step("Clicking on three dots button")
    def first_product_dots_click(self):
        dots = self.wait.until(expected_conditions.element_to_be_clickable(CartLocators.three_dots_button))
        self.driver.execute_script("arguments[0].click();", dots)

    @allure.step("Removing product from cart")
    def rem_option_click(self):
        rem = self.wait.until(expected_conditions.element_to_be_clickable(CartLocators.remove_option))
        self.driver.execute_script("arguments[0].click();", rem)

    @allure.step("Getting page message")
    def get_cart_message(self):
        return self.wait.until(expected_conditions.element_to_be_clickable(CartLocators.empty_cart_message)).text
