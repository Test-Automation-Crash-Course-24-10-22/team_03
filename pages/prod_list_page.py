from pages.page import Page
from locators.prod_list_page_locators import ProductListLocators
from selenium.webdriver.support import expected_conditions
import allure


class ProdListPage(Page):
    def __init__(self, driver):
        super(ProdListPage, self).__init__(driver)
        self.page = 'https://rozetka.com.ua/ua/headphones/c80027/producer=samsung/'

    @allure.step("Clicking on product's image to open product's page")
    def prod_click(self):
        av_prod_a = self.wait.until(expected_conditions.element_to_be_clickable(ProductListLocators.product_image))
        self.driver.execute_script("arguments[0].click();", av_prod_a)

    @allure.step("Clicking on cart button")
    def cart_button_click(self):
        buy = self.wait.until(expected_conditions.element_to_be_clickable(ProductListLocators.first_prod_cart_button))
        self.driver.execute_script("arguments[0].click();", buy)

    @allure.step("Clicking on pop-up message")
    def pop_up_click(self):
        cart = self.wait.until(expected_conditions.presence_of_element_located(ProductListLocators.pop_up_message))
        self.driver.execute_script("arguments[0].click();", cart)

    @allure.step("Clicking on cart icon")
    def cart_icon(self):
        cart = self.wait.until(expected_conditions.element_to_be_clickable(ProductListLocators.cart_icon))
        self.driver.execute_script("arguments[0].click();", cart)
