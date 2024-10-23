import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))

    def navigate(self, url, expected_element=None):
        self.driver.get(url)
        if expected_element:
            self.wait_for_element(expected_element)

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_all_elements_located(locator))

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def action_click(self, locator, expected_element=None):
        element = self.wait_for_element(locator)
        element.click()
        if expected_element:
            self.wait_for_element(expected_element)

    def wait_for_url(self, url, timeout=15):
        WebDriverWait(self.driver, timeout).until(expected_conditions.url_to_be(url))
