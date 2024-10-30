import allure
from page.base_page import BasePage
from config import URL
from locators.progress_locators import ProgressLocators


class ProgressPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProgressLocators

    @allure.step("Открытие страницы с заказами в процессе выполнения")
    def open_in_progress_orders(self):
        self.transition(URL.ORDER_STREAM.value)

    @allure.step("Получение списка ID заказов в процессе выполнения")
    def get_in_progress_order_ids(self):
        orders = self.find_elements(self.locators.PROGRESS_ORDERS)
        return [order.text.split('№')[-1].strip() for order in orders]