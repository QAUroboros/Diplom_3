import allure
from page.base_page import BasePage
from locators.profile_account_locators import ProfileAccountLocators
from config import URL


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProfileAccountLocators

    @allure.step("Переход на страницу заказов")
    def open_user_orders(self):
        self.navigate(URL.USER_PROFILE.value, self.locators.USER_ORDERS)

    @allure.step("Получение списка заказа")
    def get_user_orders(self):
        orders = self.find_elements(self.locators.USER_ORDERS)
        return [order.text for order in orders]

    @allure.step("Переход на профиль")
    def go_to_profile_tab(self):
        self.action_click(self.locators.PROFILE_TAB)

    @allure.step("Ввод имени")
    def enter_name(self, name):
        self.clear_fields(self.locators.INPUT_NAME, name)

    @allure.step("Клик по кнопке сохранить")
    def click_save_button(self):
        self.action_click(self.locators.BUTTON_SAVE)

    @allure.step("Получение имение пользователя")
    def get_name(self):
        return self.get_element_text(self.locators.INPUT_NAME)

    @allure.step("Выход с аккаунта")
    def logout(self):
        self.action_click(self.locators.LOGOUT_BUTTON)