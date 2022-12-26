from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException,\
    ElementClickInterceptedException
import allure


class Page:
    def __init__(self, driver, page=None):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10, ignored_exceptions=(NoSuchElementException, TimeoutException,
                                                                               StaleElementReferenceException,
                                                                               ElementClickInterceptedException))
        self.page = page

    # def wait_doc_load(self):
    #     self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

    @allure.step("Openning page")
    def open(self):
        if self.page:
            self.driver.get(self.page)
