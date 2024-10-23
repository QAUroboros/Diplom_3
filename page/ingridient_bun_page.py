import allure
from page.base_page import BasePage
from locators.ingridient_bun_locators import IngredientBunLocators


class IngredientPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Добавление ингредиента 'Флюоресцентный бургер' в конструктор")
    def add_ingredient(self):

        ingredient = self.wait_for_element(IngredientBunLocators.INGREDIENT_MODAL)
        ingredient.click()

    @allure.step("Проверка увеличения счетчика ингредиентов")
    def is_counter_increased(self):
        counter = self.wait_for_element(IngredientBunLocators.COUNTER_LOCATOR)
        return int(counter.text) > 0