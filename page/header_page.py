import allure
from page.base_page import BasePage
from locators.header_locators import HeaderLocators


class HeaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HeaderLocators

    def click_header_button(self, locator, element_name="Элемент"):
        self.action_click(locator, self.locators.LINK_LOGO)

    def go_to_constructor(self):
        self.action_click(self.locators.LINK_CONSTRUCTOR, self.locators.LINK_LOGO)

    def go_to_order_feed(self):
        self.action_click(self.locators.LINK_ORDER_FEED)

    def go_to_personal_account(self):
        self.action_click(self.locators.LINK_LOGO)

    def is_at_main_page(self):
        return self.is_element_visible(self.locators.LINK_CONSTRUCTOR)

    def is_element_visible(self, locator, timeout=15):
        return self.wait_for_element(locator, timeout).is_displayed()

    def click_logo(self):
        self.action_click(self.locators.LINK_LOGO)
