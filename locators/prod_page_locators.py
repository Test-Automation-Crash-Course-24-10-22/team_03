from selenium.webdriver.common.by import By


class ProductLocators:
    buy_button = (
       By.XPATH, "//button[@class='buy-button button button--with-icon button--green button--medium ng-star-inserted']")
    continue_button = (By.XPATH, "//button[@data-testid='continue-shopping-link']")
    counter_icon = (By.XPATH, "//span[@class='counter counter--green ng-star-inserted']")
    in_cart_text = (By.XPATH, "//span[@class='buy-button__label ng-star-inserted']")
