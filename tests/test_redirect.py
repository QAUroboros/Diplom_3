import allure
import pytest
from page.header_page import HeaderPage
from page.home_page import HomePage
from page.order_page import OrderPage
from page.login_page import LoginPage
from config import DOMAIN, URL


@pytest.mark.usefixtures("login")
class TestRedirect:

    @allure.title('Переход по клику на «Конструктор»')
    def test_click_on_constructor(self, open_browser):
        header = HeaderPage(open_browser)
        home_page = HomePage(open_browser)
        header.go_to_constructor()
        home_page.wait_for_element(home_page.locators.DIV_BUNS)
        assert home_page.is_at_url(DOMAIN), f"Ожидался URL: {DOMAIN}, но получен: {home_page.get_current_url()}"

    @allure.title('Переход по клику на «Лента заказов»')
    def test_click_on_order_feed(self, open_browser):
        header = HeaderPage(open_browser)
        order_page = OrderPage(open_browser)
        header.go_to_order_feed()
        order_page.wait_for_element(order_page.locators.ORDERS_PAGE)
        assert order_page.is_at_order_feed(), f"Ожидался URL: {URL.ORDER_STREAM.value}, но получен: {order_page.get_current_url()}"

    @allure.title('Переход по клику на логотип Stellar Burgers')
    def test_click_on_logo_redirects_to_home(self, open_browser):
        header = HeaderPage(open_browser)
        home_page = HomePage(open_browser)
        header.go_to_order_feed()
        header.click_logo()
        home_page.wait_for_element(home_page.locators.LOGIN_BUTTON)
        assert home_page.is_at_url(DOMAIN), f"Ожидался URL: {DOMAIN}, но получен: {home_page.get_current_url()}"

    @allure.title('Переход на страницу логина при доступе к ленте заказов без авторизации')
    def test_redirect_to_login_when_unauthorized_user_access_feed(self, open_browser):
        login_page = LoginPage(open_browser)
        header = HeaderPage(open_browser)
        login_page.open_login_page()
        header.go_to_order_feed()
        assert login_page.is_at_url(URL.SIGN_IN.value), "Пользователь не был перенаправлен на страницу логина"