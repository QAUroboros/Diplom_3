import allure
from page.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from locators.login_locators import LoginLocators
from config import URL


class PersonalAccount(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PersonalAccountLocators

    @allure.step("Кликнуть по кнопке выхода")
    def click_button_exit(self):
        self.action_click(self.locators.BUTTON_EXIT, LoginLocators.TITLE_FORM)

    @allure.step("Пользователь разлогинился")
    def is_logged_out(self):
        return self.wait_for_element(LoginLocators.TITLE_FORM).is_displayed()

    @allure.step("Проверка отображения кнопки Выход")
    def is_exit_button_displayed(self):
        return self.is_element_visible(self.locators.BUTTON_EXIT)

    @allure.step("Кликнуть по кнопке Выход")
    def click_buttons_exit(self):
        self.action_click(self.locators.BUTTON_EXIT)

    @allure.step("Проверка что находимся на странице логина после выхода")
    def is_loged_out(self):
        return self.is_at_url(URL.SIGN_IN.value)

    @allure.step("Проверка на нахождения в личном кабинете")
    def is_at_personal_area(self):
        return self.is_element_visible(self.locators.TITLE_PERSONAL_AREA)
