from selenium.webdriver.common.by import By


class CartLocators:
    plus_button = (By.XPATH, "//button[@data-testid='cart-counter-increment-button']")
    first_prod_quantity = (By.XPATH, "//input[@data-testid='cart-counter-input']")
    first_prod_price = (By.XPATH, "//p[@data-testid='cost']")
    order_price = (By.XPATH, "//div[@class='cart-receipt__sum-price']/span[1]")
    cross = (By.XPATH, "//button[@class='modal__close']")
    three_dots_button = (By.XPATH, "//button[@id='cartProductActions0']")
    remove_option = (By.XPATH, "//button[@class='button button--medium button--with-icon button--link "
                               "context-menu-actions__button']")
    empty_cart_header = (By.XPATH, "//h4[@class='cart-dummy__heading']")
    empty_cart_message = (By.XPATH, "//p[@class='cart-dummy__caption']")
    minus_button = (By.XPATH, "//button[@data-testid='cart-counter-decrement-button']")
    minus_button_symbol = (By.XPATH, "//button[@data-testid='cart-counter-decrement-button']")
    page_header = (By.XPATH, "//h3[@class='modal__heading']")
