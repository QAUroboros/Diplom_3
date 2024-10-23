from locators.login_locators import LoginLocators
from config import URL
from page.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.navigate(URL.SIGN_IN.value, LoginLocators.TITLE_FORM)

    def enter_email(self, email):
        self.enter_text(LoginLocators.EMAIL, email)

    def enter_password(self, password):
        self.enter_text(LoginLocators.PASSWORD, password)

    def click_login(self):
        self.action_click(LoginLocators.BUTTON_LOGIN, LoginLocators.CHECKOUT_BUTTON)

    def go_to_forgot_password(self):
        self.action_click(LoginLocators.LINK_FORGOT_PASSWORD)

    def login(self, email, password):
        self.open_login_page()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()