import allure
from config import URL
from locators.forgot_password_locators import ForgotPasswordBurger
from page.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ForgotPasswordBurger

    @allure.step("Открытие страницы восстановления пароля")
    def open_forgot_password_page(self):
        self.navigate(URL.FORGOT_PASSWORD.value, self.locators.BUTTON_RESTORE_PASSWORD)

    @allure.step("Ввод email для восстановления пароля")
    def enter_email(self, email):
        self.enter_text(self.locators.EMAIL, email)

    @allure.step("Ожидание отображения кнопки восстановления пароля")
    def wait_for_restore_password_button(self, timeout=10):
        self.wait_for_element(self.locators.BUTTON_RESTORE_PASSWORD, timeout=timeout)

    @allure.step("Клик по кнопке восстановить пароль")
    def click_button_restore_password(self):
        self.action_click(self.locators.BUTTON_RESTORE_PASSWORD)

    @allure.step("Проверка отображения кнопки восстановления пароля")
    def is_restore_password_button_displayed(self):
        return self.is_element_visible(self.locators.BUTTON_RESTORE_PASSWORD)
