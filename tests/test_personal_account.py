import pytest
import allure
from config import URL
from page.login_page import LoginPage
from page.personal_account_page import PersonalAccountPage
from page.header_page import HeaderPage
from page.profile_account_page import ProfilePage


@pytest.mark.usefixtures("login")
class TestPersonalAccountAuthorizedUser:

    @allure.title("Переход в личный кабинет авторизованным пользователем")
    def test_redirect_to_personal_area_authorized_user(self, login):
        header = HeaderPage(login)
        personal_account = PersonalAccountPage(login)
        header.go_to_personal_account()
        assert personal_account.is_at_personal_area(), "Пользователь не перешел в личный кабинет"
        assert personal_account.is_exit_button_displayed(), "Кнопка выхода не отображается в личном кабинете"

    @allure.title("Выход из личного кабинета авторизованным пользователем")
    def test_logout_from_personal_area_authorized_user(self, login):
        header = HeaderPage(login)
        personal_account = PersonalAccountPage(login)
        header.go_to_personal_account()
        personal_account.click_exit_button()
        assert personal_account.is_logged_out(), "Пользователь не был перенаправлен на страницу логина после выхода"


class TestPersonalAccountUnauthorizedUser:

    @allure.title("Переход на страницу логина для неавторизованного пользователя при попытке доступа к личному кабинету")
    def test_redirect_to_login_page_for_unauthorized_user(self, open_browser):
        header = HeaderPage(open_browser)
        personal_account = PersonalAccountPage(open_browser)
        header.go_to_personal_account()
        assert personal_account.is_logged_out(), "Пользователь не был перенаправлен на страницу логина"
        assert personal_account.is_login_form_displayed(), "Форма логина не отображается"

    @allure.title("Неавторизованный пользователь не может зайти в личный кабинет")
    def test_access_personal_area_without_login(self, open_browser):
        header = HeaderPage(open_browser)
        personal_account = PersonalAccountPage(open_browser)
        header.go_to_personal_account()
        assert personal_account.is_at_personal_area(), "Неавторизованный пользователь смог перейти в личный кабинет"


@pytest.mark.usefixtures("login")
class TestUserProfile:

    @allure.title("Изменение информации в профиле пользователя")
    def test_change_user_profile_info(self, login):
        profile_page = ProfilePage(login)
        profile_page.go_to_profile_tab()
        new_name = "TestUser"
        profile_page.enter_name(new_name)
        profile_page.click_save_button()
        assert profile_page.get_name() == new_name, "Имя пользователя не было успешно изменено"
