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
        price_for_one = int(self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='cart-receipt__sum-price']/span[1]"))).text)
        # Clicking on plus
        plus = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@data-testid='cart-counter-increment-button']")))
        plus.click()
        amount = int(self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@data-testid='cart-counter-input']"))).get_attribute('value'))
        # self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(3)  # The previous row is no help at all, so...
        self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        price_for_two = int(self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='cart-receipt__sum-price']/span[1]"))).text)
        if amount == 2 and price_for_two == price_for_one * 2:
            # Closing cart pop-up via cross
            cross = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class='modal__close']")))
            cross.click()
            # Check the counter icon
            amount = int(self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='counter counter--green ng-star-inserted']"))).text)
            if amount == 2:
                return 'Passed'
        return 'Failed'

    # Removing Product from the Cart
    def rem_product(self):
        self.driver.get(self.product_page)
        self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        # Clicking on cart button
        buy = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//*[name()='use' and @*='#icon-basket']/../..)[1]")))
        buy.click()
        buy = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//*[name()='use' and @*='#icon-basket']/../..)[2]")))
        buy.click()
        # Clicking on cart icon
        cart = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class='header__button ng-star-inserted header__button--active']")))
        cart.click()
        # Clicking on three dots button
        dots = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@id='cartProductActions0']")))
        dots.click()
        # Remove product
        rem = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class='button button--medium button--with-icon button--link context-menu-actions__button']")))
        rem.click()
        # self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(3)  # The previous row is no help at all, so...
        sum = int(self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='cart-receipt__sum-price']/span[1]"))).text)
        price = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//p[@data-testid='cost']"))).text.split(" ", 2)
        price = int(''.join(price[:len(price)-1]))
        if sum == price:
            # Remove another product
            dots = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@id='cartProductActions0']")))
            dots.click()
            rem = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class='button button--medium button--with-icon button--link context-menu-actions__button']")))
            rem.click()
            header = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//h4[@class='cart-dummy__heading']"))).text
            mes = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//p[@class='cart-dummy__caption']"))).text
            if header == 'Кошик порожній' and mes == 'Але це ніколи не пізно виправити :)':
                return 'Passed'
        return 'Failed'

    '''Verifying the user's ability to open the Cart via the text 'Вже в кошику' in the product overview,
    remove one product item from the cart, & inability to remove all of them by using the '-' button'''
    def rem_item(self):
        self.driver.get(self.product_page)
        self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        # Adding two items of any product to the cart
        buy = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//*[name()='use' and @*='#icon-basket']/../..)")))
        buy.click()
        cart = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class='header__button ng-star-inserted header__button--active']")))
        cart.click()
        plus = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@data-testid='cart-counter-increment-button']")))
        plus.click()
        # Clicking on minus
        minus = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@data-testid='cart-counter-decrement-button']")))
        minus.click()
        # self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(3)  # The previous row is no help at all, so...
        minus_symb = self.driver.find_element(By.XPATH, "//button[@data-testid='cart-counter-decrement-button']").value_of_css_property('color')
        amount = int(self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@data-testid='cart-counter-input']"))).get_attribute('value'))
        price = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//p[@data-testid='cost']"))).text.split(" ", 2)
        price = int(''.join(price[:len(price) - 1]))
        sum = int(self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='cart-receipt__sum-price']/span[1]"))).text)
        if amount == 1 and price == sum and minus_symb == 'rgba(166, 165, 165, 1)':
            minus.click()
            minus_symb_new = self.driver.find_element(By.XPATH, "//button[@data-testid='cart-counter-decrement-button']").value_of_css_property('color')
            amount_new = int(self.wait.until(expected_conditions.presence_of_element_located( (By.XPATH, "//input[@data-testid='cart-counter-input']"))).get_attribute('value'))
            price_new = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//p[@data-testid='cost']"))).text.split(" ", 2)
            price_new = int(''.join(price_new[:len(price_new) - 1]))
            sum_new = int(self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='cart-receipt__sum-price']/span[1]"))).text)
            if minus_symb_new == minus_symb and amount_new == amount and price_new == price and sum_new == sum:
                return 'Passed'
        return 'Failed'

    # Verifying the user's ability to open the Cart via a Pop-up message
    def pop_up(self):
        self.driver.get(self.product_page)
        # self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(3)  # The previous row is no help at all, so...
        # Clicking on cart button
        buy = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//app-buy-button[@class='toOrder ng-star-inserted']")))
        buy.click()
        cart = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[@aria-label='Открыть корзину']")))
        cart.click()
        # Checking if the heading is 'Кошик'
        head = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//h3[@class='modal__heading']"))).text
        if head == 'Кошик':
            return 'Passed'
        return 'Failed'
