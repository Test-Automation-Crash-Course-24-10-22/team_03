import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Drive(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_argument('--start-maximized')
        cls.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        cls.driver.get('https://rozetka.com.ua/ua/')
        cls.wait = WebDriverWait(cls.driver, 30, ignored_exceptions=(NoSuchElementException,
                                                                     StaleElementReferenceException, TimeoutException))

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    @classmethod
    def waitDocLoad(cls):
        cls.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')