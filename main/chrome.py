from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import cart_suite as cart
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.get('https://rozetka.com.ua/ua/')
print('\nTesting Cart Functionality...')
cart_suite = cart.Cart(driver, 'https://rozetka.com.ua/ua/headphones/c80027/producer=samsung/')
print('Test Case 1:', cart_suite.add_product())
driver.quit()