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
        if element:
            element.clear()
            element.send_keys(text)

    @allure.step("Клик по элементу: {locator}")
    def action_click(self, locator, expected_element=None):
        element = self.wait_for_element(locator)
        if element:
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
            element = self.wait_for_element(locator, timeout)
            if element:
                return element.is_displayed()
            return False
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
        if element:
            element.clear()
            element.send_keys(text)

    @allure.step("Получение текста элемента: {locator}")
    def get_element_text(self, locator):
        element = self.wait_for_element(locator)
        if element:
            return element.text
        return ""

    @allure.step("Прокрутка до элемента: {locator}")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        else:
            print(f"Element to scroll to not found: {locator}")
            self.save_screenshot('scroll_to_element_exception.png')

    @allure.step("Сохранение скриншота страницы")
    def save_screenshot(self, file_name):
        try:
            self.driver.save_screenshot(file_name)
        except Exception as e:
            print(f"Failed to save screenshot {file_name}: {e}")
