import allure
from page.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from config import URL


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PersonalAccountLocators()

    @allure.step("Кликнуть по кнопке выхода")
    def click_exit_button(self):
        self.action_click(self.locators.BUTTON_EXIT)

    @allure.step("Проверка отображения кнопки Выход")
    def is_exit_button_displayed(self):
        return self.is_element_visible(self.locators.BUTTON_EXIT)

    @allure.step("Проверка, что пользователь разлогинился и находится на странице логина")
    def is_logged_out(self):
        return self.is_at_url(URL.SIGN_IN.value)

    @allure.step("Проверка, что пользователь находится в личном кабинете")
    def is_at_personal_area(self):
        return self.is_element_visible(self.locators.TITLE_PERSONAL_AREA)

    @allure.step("Проверка отображения формы логина")
    def is_login_form_displayed(self):
        return self.is_element_visible(self.locators.TITLE_FORM)