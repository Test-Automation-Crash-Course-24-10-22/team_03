import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Drive(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_argument('--start-maximized')
        cls.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        cls.driver.get('https://rozetka.com.ua/ua/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()