import allure
from page.home_page import HomePage


class TestConstructor:

    @allure.title('Открытие модального окна ингредиента')
    def test_open_ingredient_modal(self, web_driver):
        home_page = HomePage(web_driver)
        ingredient_modal = IngredientModalPage(web_driver)

        home_page.open_home_page()
        home_page.click_fluorescent_bun()

        assert ingredient_modal.is_modal_open(), "Модальное окно не открылось"
        name_ingredient = home_page.get_fluorescent_bun_name()
        name_ingredient_in_modal = ingredient_modal.get_ingredient_name_in_modal()
        assert name_ingredient == name_ingredient_in_modal, "Названия ингредиентов не совпадают"

    @allure.title('Закрытие модального окна ингредиента')
    def test_close_ingredient_modal(self, web_driver):
        home_page = HomePage(web_driver)
        ingredient_modal = IngredientModalPage(web_driver)
        home_page.open_home_page()
        home_page.click_fluorescent_bun()
        assert ingredient_modal.is_modal_open(), "Модальное окно не открылось"
        ingredient_modal.close_modal()
        assert ingredient_modal.is_modal_closed(), "Модальное окно не закрылось"