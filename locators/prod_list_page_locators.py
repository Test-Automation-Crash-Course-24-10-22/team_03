from selenium.webdriver.common.by import By


class ProductListLocators:
    product_image = (By.XPATH,
                     "//div[@class='goods-tile__availability goods-tile__availability--available ng-star-inserted']["
                     "contains(text(), 'Готовий до відправлення') or contains(text(), 'Є в наявності') or contains("
                     "text(), 'Закінчується')]/preceding-sibling::a[@class='goods-tile__picture ng-star-inserted']")
    first_prod_cart_button = (By.XPATH, "(//*[name()='use' and @*='#icon-basket']/../..)[1]")
    second_prod_cart_button = (By.XPATH, "(//*[name()='use' and @*='#icon-basket']/../..)[2]")
    cart_icon = (By.XPATH, "//button[@class='header__button ng-star-inserted header__button--active']")
    pop_up_message = (By.XPATH, "//button[@aria-label='Відкрити корзину']")
