from pages.page import Page
from locators.prod_page_locators import ProductLocators
from selenium.webdriver.support import expected_conditions
import allure


class ProdPage(Page):
    def __init__(self, driver):
        super(ProdPage, self).__init__(driver)

    @allure.step("Clicking 'Купити' button")
    def buy_button_click(self):
        buy = self.wait.until(expected_conditions.element_to_be_clickable(ProductLocators.buy_button))
        self.driver.execute_script("arguments[0].click();", buy)

    @allure.step("Opening the cart")
    def cart_text_click(self):
        cart = self.wait.until(expected_conditions.element_to_be_clickable(ProductLocators.in_cart_text))
        self.driver.execute_script("arguments[0].click();", cart)

    @allure.step("Close via 'Продовжити покупки' button")
    def con_button_click(self):
        con = self.wait.until(expected_conditions.element_to_be_clickable(ProductLocators.continue_button))
        self.driver.execute_script("arguments[0].click();", con)

    @allure.step("Checking the counter icon")
    def get_counter(self):
        return int(self.wait.until(expected_conditions.presence_of_element_located(ProductLocators.counter_icon)).text)
