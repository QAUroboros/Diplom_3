from selenium.webdriver.common.by import By


class OrderPageLocators:
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ORDER_CONFIRMATION = (By.XPATH, "//h1[contains(text(), 'Ваш заказ начали готовить')]")
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//*[contains(text(), 'Выполнено за все время')]/following-sibling::span")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//*[contains(text(), 'Выполнено за сегодня')]/following-sibling::span")
    ORDERS_PAGE = (By.XPATH, "//*[contains(text(), 'Лента заказов')]")
    ORDER_DETAILS_POPUP = (By.XPATH, "//div[contains(@class, 'modal')]//h2[contains(text(), 'Детали заказа')]")
    ORDER_NUMBER_IN_PROGRESS = (By.XPATH, "//p[contains(text(), '№')]")