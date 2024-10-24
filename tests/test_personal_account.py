import pytest
import allure
from config import URL
from locators.login_locators import LoginLocators
from page.login_page import LoginPage
from page.personal_account_page import PersonalAccount
from page.header_page import HeaderPage
from page.profile_account_page import ProfilePage


@pytest.mark.usefixtures("login")
class TestPersonalAccount:

    @allure.step("Переход на страницу в личный кабинет для авторизации юзера")
    def test_redirect_to_personal_area_authorized_user(self, open_browser):
        header = HeaderPage(open_browser)
        personal_account = PersonalAccount(open_browser)
        header.go_to_personal_account()
        assert personal_account.is_at_personal_area(), "Пользователь не перешел в личный кабинет"
        assert personal_account.is_exit_button_displayed(), "Кнопка выхода не отображается в личном кабинете"

    @allure.step("Переход на странцу логина для неавторизованного юзера")
    def test_redirect_to_login_page_for_unauthorized_user(self, open_browser):
        home_page = LoginPage(open_browser)
        header = HeaderPage(open_browser)
        home_page.open_login_page()
        header.go_to_personal_account()
        assert home_page.is_at_url(URL.SIGN_IN.value), "Пользователь не был перенаправлен на страницу логина"
        assert home_page.wait_for_element(LoginLocators.TITLE_FORM).is_displayed(), "Форма логина не отображается"

    @allure.step("Выходи с личного кабинета авторизованным юзером")
    def test_logout_from_personal_area_authorized_user(self, open_browser):
        header = HeaderPage(open_browser)
        personal_account = PersonalAccount(open_browser)
        header.go_to_personal_account()
        personal_account.click_button_exit()

    @allure.step("Изменение информации в профиле пользователя")
    def test_change_user_profile_info(self, open_browser):
        profile_page = ProfilePage(open_browser)
        profile_page.open_user_orders()
        profile_page.go_to_profile_tab()
        new_name = "TestUser"
        profile_page.enter_name(new_name)
        profile_page.click_save_button()
        assert profile_page.get_name() == new_name, "Имя пользователя не было успешно изменено"

    @allure.step("Юзер не может зайти в личный кабинет без автризации")
    def test_access_personal_area_without_login(self, open_browser):
        header = HeaderPage(open_browser)
        personal_account = PersonalAccount(open_browser)
        header.go_to_personal_account()
        assert personal_account.is_at_url(URL.SIGN_IN.value), "Неавторизованный пользователь смог перейти в личный кабинет"
