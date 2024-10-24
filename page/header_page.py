import allure
from page.base_page import BasePage
from locators.header_locators import HeaderLocators


class HeaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HeaderLocators

    @allure.step("Кликнуть по элементу ")
    def click_header_button(self, locator):
        self.action_click(locator, self.locators.LINK_LOGO)

    @allure.step("Переход в конструктор")
    def go_to_constructor(self):
        self.action_click(self.locators.LINK_CONSTRUCTOR, self.locators.LINK_LOGO)

    @allure.step("Переход в ленту заказов")
    def go_to_order_feed(self):
        self.action_click(self.locators.LINK_ORDER_FEED)

    @allure.step("Переходи в личный кабинет")
    def go_to_personal_account(self):
        self.action_click(self.locators.LINK_LOGO)

    @allure.step("Нахождение на главной странице")
    def is_at_main_page(self):
        return self.is_element_visible(self.locators.LINK_CONSTRUCTOR)

    @allure.step("Проверка на наличие элемента")
    def is_element_visible(self, locator, timeout=15):
        return self.wait_for_element(locator, timeout).is_displayed()

    @allure.step("клик по логотипу")
    def click_logo(self):
        self.action_click(self.locators.LINK_LOGO)
