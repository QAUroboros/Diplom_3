from page.login_page import LoginPage
from config import URL
from page.forgot_password_page import ForgotPasswordPage
from page.resset_password_page import ResetPasswordPage
from locators.forgot_password_locators import ForgotPasswordBurger
import allure


class TestForgotPassword:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_page_opening_forgot_password(self, open_browser):
        login_page = LoginPage(open_browser)
        login_page.open_login_page()
        login_page.go_to_forgot_password()
        url = open_browser.current_url
        assert url == URL.FORGOT_PASSWORD.value, f"Ожидался URL: {URL.FORGOT_PASSWORD.value}, но получен: {url}"

    @allure.title('Проверка ввода почты на странице восстановления пароля и клика по кнопке «Восстановить»')
    def test_page_enter_email_and_redirect_reset_password(self, open_browser):
        forgot_password = ForgotPasswordPage(open_browser)
        forgot_password.open_forgot_password_page()
        forgot_password.enter_email("test@example.com")
        forgot_password.wait_for_element(ForgotPasswordBurger.BUTTON_RESTORE_PASSWORD)
        forgot_password.click_button_restore_password()
        forgot_password.wait_for_url(URL.PASSWORD_CHANGE.value, timeout=30)
        url = open_browser.current_url
        assert url == URL.PASSWORD_CHANGE.value, f"Ожидался URL: {URL.PASSWORD_CHANGE.value}, но получен: {url}"

    @allure.title('Проверка отображения скрытого пароля')
    def test_whether_hidden_password(self, open_browser):
        forgot_password = ForgotPasswordPage(open_browser)
        reset_password = ResetPasswordPage(open_browser)
        forgot_password.open_forgot_password_page()
        forgot_password.enter_email("test@example.com")
        forgot_password.wait_for_element(ForgotPasswordBurger.BUTTON_RESTORE_PASSWORD)
        forgot_password.click_button_restore_password()
        forgot_password.wait_for_url(URL.PASSWORD_CHANGE.value)
        reset_password.enter_password()
        assert reset_password.get_attribute_password() == "password", "Пароль отображается открытым"

    @allure.title('Проверка отображения видимого пароля')
    def test_whether_visible_password(self, open_browser):
        forgot_password = ForgotPasswordPage(open_browser)
        reset_password = ResetPasswordPage(open_browser)
        forgot_password.open_forgot_password_page()
        forgot_password.enter_email("test@example.com")
        forgot_password.click_button_restore_password()
        reset_password.enter_password()
        reset_password.click_button_action_password()
        assert reset_password.get_attribute_password() == "text", "Пароль не отображается открытым"