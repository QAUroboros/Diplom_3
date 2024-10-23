import allure
import pytest
from page.ingridient_bun_page import IngredientPage
from page.order_page import OrderPage
from page.profile_account_page import ProfilePage
from page.feed_page import FeedPage
from page.progress_page import ProgressPage


@pytest.mark.usefixtures("login")
class TestOrderFlow:

    @allure.title('Увеличение счётчика ингредиента при добавлении в заказ')
    def test_ingredient_counter_increases_after_addition(self, open_browser):
        ingredient_page = IngredientPage(open_browser)
        ingredient_page.add_ingredient()
        assert ingredient_page.is_counter_increased(), "Счётчик ингредиента не увеличился после добавления"

    @allure.title('Возможность залогиненного пользователя оформить заказ')
    def test_logged_in_user_can_place_order(self, open_browser):
        order_page = OrderPage(open_browser)
        order_page.open_orders_page()
        order_page.place_order()
        assert order_page.is_order_placed(), "Заказ не был успешно оформлен"

    @allure.title('Открытие всплывающего окна с деталями заказа')
    def test_order_details_popup_opens_on_click(self, open_browser):
        order_page = OrderPage(open_browser)
        order_page.open_orders_page()
        order_page.click_order()
        assert order_page.is_order_details_popup_displayed(), "Модальное окно с деталями заказа не открылось"

    @allure.title('Заказы пользователя отображаются в «Ленте заказов»')
    def test_user_orders_displayed_in_order_feed(self, open_browser):
        profile_page = ProfilePage(open_browser)
        feed_page = FeedPage(open_browser)
        profile_page.open_user_orders()
        user_orders = profile_page.get_user_orders()
        feed_page.open_feed()
        feed_orders = feed_page.get_feed_orders()
        for order in user_orders:
            assert order in feed_orders, f"Заказ {order} не отображается в ленте заказов"

    @allure.title('Увеличение счётчика «Выполнено за всё время» при создании нового заказа')
    def test_total_orders_counter_increases(self, open_browser):
        order_page = OrderPage(open_browser)
        order_page.open_orders_page()
        initial_count = order_page.get_total_orders_count()
        order_page.place_order()
        new_count = order_page.get_total_orders_count()
        assert new_count == initial_count + 1, "Счётчик выполненных заказов за всё время не увеличился"

    @allure.title('Увеличение счётчика «Выполнено за сегодня» при создании нового заказа')
    def test_today_orders_counter_increases(self, open_browser):
        order_page = OrderPage(open_browser)
        order_page.open_orders_page()
        initial_count = order_page.get_today_orders_count()
        order_page.place_order()
        new_count = order_page.get_today_orders_count()
        assert new_count == initial_count + 1, "Счётчик выполненных заказов за сегодня не увеличился"

    @allure.title('Появление номера заказа в разделе «В работе» после оформления')
    def test_order_number_appears_in_in_progress_section(self, open_browser):
        order_page = OrderPage(open_browser)
        order_page.open_orders_page()
        order_page.place_order()
        order_id = order_page.get_order_id()
        progress_page = ProgressPage(open_browser)
        progress_page.open_in_progress_orders()
        assert order_id in progress_page.get_in_progress_order_ids(), f"Заказ {order_id} не отображается в разделе «В работе»"