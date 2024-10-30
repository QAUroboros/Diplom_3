from selenium.webdriver.common.by import By


class HeaderLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[.='Личный Кабинет']")
    LINK_LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]/a")
    LINK_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    LINK_ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")