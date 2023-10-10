from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import  ActionChains

class Base:

    def __init__(self, context):
        self.driver = context.driver

    def find_element(self, locator, element):
        try:
            item = self.driver.find_element(locator, element)
            return item
        except NoSuchElementException:
            return None

    def wait_element(self, locator, element):
        try:
            item = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((locator, element)))
            return item
        except NoSuchElementException:
            return None

    def send_keys(self, locator, element, value):
        try:
            item = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator, element)))
            item.send_keys(value)
        except ElementNotInteractableException:
            ActionChains.move_to_element(locator, element).click().send_keys(value).perform()

    def click_element(self, locator, element):
        try:
            item = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator, element)))
            item.click()
        except ElementNotInteractableException:
            ActionChains.move_to_element(locator, element).click().perform()


