from config import URL
from locators.forgot_password_locators import ForgotPasswordBurger
from page.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_forgot_password_page(self):
        self.navigate(URL.FORGOT_PASSWORD.value, ForgotPasswordBurger.BUTTON_RESTORE_PASSWORD)

    def enter_email(self, email):
        self.enter_text(ForgotPasswordBurger.EMAIL, email)

    def click_button_restore_password(self):
        self.action_click(ForgotPasswordBurger.BUTTON_RESTORE_PASSWORD)
