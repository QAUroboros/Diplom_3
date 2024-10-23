import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from data import BASE_URL


@pytest.fixture(params=["chrome", "firefox"])
def open_browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif request.param == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError("Неподдерживаемый браузер. Используйте 'chrome' или 'firefox'.")

    driver.get(BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()


