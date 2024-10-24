import time
import allure
from page.home_page import HomePage
from page.ingridient_details_page import IngredientDetailsPage


class TestConstructor:

    @allure.title('Открытие модального окна ингредиента')
    def test_open_ingredient_modal(self, open_browser):
        home_page = HomePage(open_browser)
        ingredient_details = IngredientDetailsPage(open_browser)
        home_page.open_home_page()
        print("Home page opened")
        home_page.click_fluorescent_bun()
        print("Clicked on fluorescent bun")
        assert ingredient_details.is_modal_open(), "Модальное окно не открылось"
        name_ingredient = home_page.get_fluorescent_bun_name()
        name_ingredient_in_modal = ingredient_details.get_ingredient_name_in_modal()
        assert name_ingredient == name_ingredient_in_modal, "Названия ингредиентов не совпадают"

    @allure.title('Закрытие модального окна ингредиента')
    def test_close_ingredient_modal(self, open_browser):
        home_page = HomePage(open_browser)
        ingredient_details = IngredientDetailsPage(open_browser)
        home_page.open_home_page()
        home_page.click_fluorescent_bun()
        assert ingredient_details.is_modal_open(), "Модальное окно не открылось"
        ingredient_details.close_modal()
        assert ingredient_details.is_modal_closed(), "Модальное окно не закрылось"