from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.get('https://rozetka.com.ua/ua/')
driver.quit()