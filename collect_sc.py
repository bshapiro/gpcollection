from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys

driver = webdriver.Chrome(ChromeDriverManager().install())


def site_login(username, password):
    driver.get("https://play.globalpoker.com/login")
    time.sleep(5)  # wait for login page to load
    driver.find_element_by_id("1-email").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("submit").click()


def collect_sc():
    get_coins_button = driver.find_element_by_class_name("skin__cta-button")
    get_coins_button.click()
    time.sleep(5)  # wait for coin collection area to process
    elements = driver.find_elements_by_css_selector("[title*='Daily Bonus']")
    for element in elements:
        print(element.get_attribute('innerHTML'))
        element.click()
    time.sleep(3)  # wait for coins to process


if __name__ == "__main__":
    time.sleep(10)  # wait for your internet to connect
    username = sys.argv[1]
    password = sys.argv[2]
    site_login(username, password)
    time.sleep(10)  # wait for lobby page to load
    collect_sc()
    driver.quit()
