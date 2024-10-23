import allure
from page.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from config import DOMAIN


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открытие главной страницы сайта")
    def open_home_page(self):
        self.navigate(DOMAIN, HomePageLocators.LOGIN_BUTTON)

    @allure.step("Проверка, отображения кнопки 'Войти в аккаунт'")
    def is_login_button_displayed(self):
        return self.wait_for_element(HomePageLocators.LOGIN_BUTTON).is_displayed()

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_login_button(self):
        self.action_click(HomePageLocators.LOGIN_BUTTON)

    @allure.step("Клик по флуоресцентной булочке")
    def click_fluorescent_bun(self):
        self.action_click(HomePageLocators.BUN_FLUORESCENT)

    @allure.step("Получение имени флуоресцентной булочки")
    def get_fluorescent_bun_name(self):
        return self.wait_for_element(HomePageLocators.NAME_BUN_FLUORESCENT).text

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_checkout_button(self):
        self.action_click(HomePageLocators.CHECKOUT_BUTTON)