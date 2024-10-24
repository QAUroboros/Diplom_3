import allure
from locators.login_locators import LoginLocators
from config import URL
from page.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открытие страницы логин ")
    def open_login_page(self):
        self.navigate(URL.SIGN_IN.value, LoginLocators.TITLE_FORM)

    @allure.step("Ввод в поле email")
    def enter_email(self, email):
        self.enter_text(LoginLocators.EMAIL, email)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.enter_text(LoginLocators.PASSWORD, password)

    @allure.step("Клик по кнопке Войти")
    def click_login(self):
        self.action_click(LoginLocators.BUTTON_LOGIN, LoginLocators.CHECKOUT_BUTTON)

    @allure.step("Переход на страницу Забыл пароль")
    def go_to_forgot_password(self):
        self.action_click(LoginLocators.LINK_FORGOT_PASSWORD)

    @allure.step("Авторизация")
    def login(self, email, password):
        self.open_login_page()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()