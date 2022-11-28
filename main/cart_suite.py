from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Cart:
    def __init__(self, driver, page):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60, ignored_exceptions=(NoSuchElementException, StaleElementReferenceException,))
        self.product_page = driver.get(page)

    # Verifying the user's ability to add one available product item to the Cart & closure of Cart pop-up via the button
    def add_product(self):
        # Clicking on product's image to open product's page
        av_prod_a = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='goods-tile__availability goods-tile__availability--available ng-star-inserted'][contains(text(), 'Готовий до відправлення') or contains(text(), 'Є в наявності') or contains(text(), 'Закінчується')]/preceding-sibling::a[@class='goods-tile__picture ng-star-inserted']")))
        av_prod_a.click()
        # Clicking 'Купити' button
        buy = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[@class='buy-button button button--with-icon button--green button--medium ng-star-inserted']")))
        buy.click()
        # Close via 'Продовжити покупки' button
        con = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[@data-testid='continue-shopping-link']")))
        con.click()
        # Check the counter icon
        amount = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='counter counter--green ng-star-inserted']"))).text
        if int(amount) == 1:
            return 'Passed'
        else:
            return 'Failed'

