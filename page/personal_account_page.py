from page.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from locators.login_locators import LoginLocators
from config import URL


class PersonalAccount(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PersonalAccountLocators

    def click_button_exit(self):
        self.action_click(self.locators.BUTTON_EXIT, LoginLocators.TITLE_FORM)

    def is_logged_out(self):
        return self.wait_for_element(LoginLocators.TITLE_FORM).is_displayed()

    def is_exit_button_displayed(self):
        return self.is_element_visible(self.locators.BUTTON_EXIT)

    def click_buttons_exit(self):
        self.action_click(self.locators.BUTTON_EXIT)

    def is_loged_out(self):
        return self.is_at_url(URL.SIGN_IN.value)

    def is_at_personal_area(self):
        return self.is_element_visible(self.locators.TITLE_PERSONAL_AREA)
