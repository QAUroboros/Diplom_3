import allure
from page.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators
from helpers import get_faker_user


class ResetPasswordPage(BasePage):
    def __init__(self, web_driver):
        super().__init__(web_driver)

    @allure.step("Ввод пароля")
    def enter_password(self):
        self.enter_text(ResetPasswordLocators.PASSWORD, get_faker_user()["password"])

    @allure.step("Получение атрибута для пароля")
    def get_attribute_password(self):
        return str(self.driver.find_element(*ResetPasswordLocators.PASSWORD).get_attribute("type"))

    @allure.step("Клик по глазу для отображения либо скрытия пароля")
    def click_button_action_password(self):
        self.action_click(ResetPasswordLocators.BUTTON_ACTION_PASSWORD, ResetPasswordLocators.PASSWORD)