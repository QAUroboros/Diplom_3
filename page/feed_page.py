import allure
from page.base_page import BasePage
from locators.feed_locators import FeedLocators
from config import URL


class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = FeedLocators

    @allure.step("Открытие страницы с лентой заказов")
    def open_feed(self):
        self.navigate(URL.ORDER_STREAM.value, self.locators.FEED_ORDERS)

    @allure.step("Получение списка заказов из ленты")
    def get_feed_orders(self):
        orders = self.find_elements(self.locators.FEED_ORDERS)
        return [order.text for order in orders]