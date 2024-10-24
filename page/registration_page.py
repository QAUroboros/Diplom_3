import allure
from page.base_page import BasePage
from locators.registration_locators import RegistrationLocators
from config import URL


class RegisterPage(BasePage):
    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.locators = RegistrationLocators

    @allure.step("Открытие страницы регистрации")
    def open_register_page(self):
        self.navigate(URL.SIGN_UP.value, self.locators.EMAIL)

    @allure.step("Ввод имени: {name}")
    def enter_name(self, name):
        self.enter_text(self.locators.NAME, name)

    @allure.step("Ввод email: {email}")
    def enter_email(self, email):
        self.enter_text(self.locators.EMAIL, email)

    @allure.step("Ввод пароля: {password}")
    def enter_password(self, password):
        self.enter_text(self.locators.PASSWORD, password)

    @allure.step("Клик по кнопке регистрации")
    def click_register(self):
        self.action_click(self.locators.SUBMIT_BUTTON, self.locators.TITLE_FORM)

    @allure.step("Регистрация нового пользователя с именем {name}, email {email}")
    def signup(self, name, email, password):
        self.open_register_page()
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_register()

    @allure.step("Проверка, что регистрация прошла успешно и отображается страница логина")
    def is_registration_successful(self):
        return self.wait_for_element(self.locators.TITLE_FORM).is_displayed()