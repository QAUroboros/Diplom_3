import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переход на страницу: {url}")
    def transition(self, url):
        self.driver.get(url)

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_for_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located(locator)
            )
            return element
        except Exception as e:
            print(f"Exception in wait_for_element: {e}")
            self.driver.save_screenshot('wait_for_element_exception.png')
            return None

    @allure.step("Переход по URL: {url}")
    def navigate(self, url, expected_element=None):
        self.driver.get(url)
        if expected_element:
            self.wait_for_element(expected_element)

    @allure.step("Получение списка элементов: {locator}")
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_all_elements_located(locator))

    @allure.step("Ввод текста: {text} в элемент {locator}")
    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Клик по элементу: {locator}")
    def action_click(self, locator, expected_element=None):
        element = self.wait_for_element(locator)
        element.click()
        if expected_element:
            self.wait_for_element(expected_element)

    @allure.step("Ожидание URL страницы")
    def wait_for_url(self, url, timeout=15):
        WebDriverWait(self.driver, timeout).until(expected_conditions.url_to_be(url))

    @allure.step("Получение текущего URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверка, что пользователь на странице с URL: {url}")
    def is_at_url(self, url):
        return self.get_current_url() == url

    @allure.step("Ожидание исчезновения элемента: {locator}")
    def wait_for_element_to_disappear(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Проверка, что элемент виден: {locator}")
    def is_element_visible(self, locator, timeout=30):
        try:
            return self.wait_for_element(locator, timeout).is_displayed()
        except:
            return False

    @allure.step("Проверка, что элемент невиден: {locator}")
    def is_element_invisible(self, locator, timeout=30):
        try:
            return WebDriverWait(self.driver, timeout).until(
                expected_conditions.invisibility_of_element_located(locator))
        except:
            return False

    @allure.step("Ожидание исчезновения перекрывающего элемента: {locator}")
    def wait_for_overlay_to_disappear(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Очистка поля и ввод текста: {locator}")
    def clear_fields(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента: {locator}")
    def get_element_text(self, locator):
        return self.wait_for_element(locator).text
