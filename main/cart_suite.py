import time

from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Cart:
    def __init__(self, driver, page):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30, ignored_exceptions=(NoSuchElementException, StaleElementReferenceException, TimeoutException))
        self.product_page = page

    # Verifying the user's ability to add one available product item to the Cart & closure of Cart pop-up via the button
    def add_product(self):
        self.driver.get(self.product_page)
        self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        # Clicking on product's image to open product's page
        av_prod_a = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='goods-tile__availability goods-tile__availability--available ng-star-inserted'][contains(text(), 'Готовий до відправлення') or contains(text(), 'Є в наявності') or contains(text(), 'Закінчується')]/preceding-sibling::a[@class='goods-tile__picture ng-star-inserted']")))
        av_prod_a.click()
        # Clicking 'Купити' button
        buy = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class='buy-button button button--with-icon button--green button--medium ng-star-inserted']")))
        buy.click()
        # Close via 'Продовжити покупки' button
        con = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@data-testid='continue-shopping-link']")))
        con.click()
        # Check the counter icon
        amount = int(self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='counter counter--green ng-star-inserted']"))).text)
        if amount == 1:
            return 'Passed'
        else:
            return 'Failed'

    # Verifying the user's ability to add another available product item to the Cart & closure of pop-up via the cross
    def add_item(self):
        self.driver.get(self.product_page)
        self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        # Clicking on product's image to open product's page
        av_prod_a = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='goods-tile__availability goods-tile__availability--available ng-star-inserted'][contains(text(), 'Готовий до відправлення') or contains(text(), 'Є в наявності') or contains(text(), 'Закінчується')]/preceding-sibling::a[@class='goods-tile__picture ng-star-inserted']")))
        av_prod_a.click()
        # Clicking 'Купити' button
        buy = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class='buy-button button button--with-icon button--green button--medium ng-star-inserted']")))
        buy.click()
        self.driver.get(self.product_page)
        self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        # Opening the product page again
        av_prod_a = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='goods-tile__availability goods-tile__availability--available ng-star-inserted'][contains(text(), 'Готовий до відправлення') or contains(text(), 'Є в наявності') or contains(text(), 'Закінчується')]/preceding-sibling::a[@class='goods-tile__picture ng-star-inserted']")))
        av_prod_a.click()
        # Clicking on the text 'В кошику'
        cart = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[@class='buy-button__label ng-star-inserted']")))
        cart.click()
        price_per_one = int(self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='cart-receipt__sum-price']/span[1]"))).text)
        # Clicking on plus
        plus = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@data-testid='cart-counter-increment-button']")))
        plus.click()
        amount = int(self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@data-testid='cart-counter-input']"))).get_attribute('value'))
        # self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(3)  # The previous row is no help at all, so...
        self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        price_per_two = int(self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='cart-receipt__sum-price']/span[1]"))).text)
        if amount == 2 and price_per_two == price_per_one * 2:
            # Closing cart pop-up via cross
            cross = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class='modal__close']")))
            cross.click()
            # Check the counter icon
            amount = int(self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='counter counter--green ng-star-inserted']"))).text)
            if amount == 2:
                return 'Passed'
        return 'Failed'

