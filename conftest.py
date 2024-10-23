import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from data.data import BASE_URL
from helpers import get_faker_user
from page.login_page import LoginPage
from page.order_page import OrderPage
from page.registration_page import RegisterPage
from config import DOMAIN


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to run tests on: chrome or firefox")


@pytest.fixture
def open_browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError("Неподдерживаемый браузер. Используйте 'chrome' или 'firefox'.")

    driver.get(BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def signup(open_browser):
    user = get_faker_user()
    name = user["name"]
    email = user["email"]
    password = user["password"]
    register_page = RegisterPage(open_browser)
    register_page.signup(name, email, password)
    return {"email": email, "password": password}


@pytest.fixture
def login(open_browser, signup):
    login_page = LoginPage(open_browser)
    login_page.login(signup["email"], signup["password"])
    return open_browser


@pytest.fixture
def login_user(open_browser):
    login_page = LoginPage(open_browser)
    login_page.login('username', 'password')
    return login_page


@pytest.fixture
def open_order_page(open_browser, login_user):
    order_page = OrderPage(open_browser)
    order_page.open_orders_page()
    return order_page
