import allure
from page.base_page import BasePage
from locators.ingridient_details_locators import IngredientDetails_locators


class IngredientDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = IngredientDetails_locators

    @allure.step("Проверка, что модальное окно ингредиента открыто")
    def is_modal_open(self):
        return self.is_element_visible(self.locators.MODAL_TITLE)

    @allure.step("Проверка, что модальное окно ингредиента закрыто")
    def is_modal_closed(self):
        return self.is_element_invisible(self.locators.MODAL_TITLE)

    @allure.step("Получение названия ингредиента из модального окна")
    def get_ingredient_name_in_modal(self):
        return self.wait_for_element(IngredientDetails_locators.MODAL_NAME_INGREDIENT).text

    @allure.step("Закрытие модального окна ингредиента")
    def close_modal(self):
        self.action_click(self.locators.MODAL_BUTTON_CLOSE)
        self.wait_for_element_to_disappear(self.locators.MODAL_TITLE)