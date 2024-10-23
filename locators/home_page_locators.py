from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGIN_BUTTON = (By.XPATH, "//section[2]/div/button[text()='Войти в аккаунт']")
    CHECKOUT_BUTTON = (By.XPATH, "//section[2]/div/button[text()='Оформить заказ']")
    DIV_BUNS = (By.XPATH, "//span[text()='Булки']/parent::div")
    BUN_FLUORESCENT = (By.XPATH, "//p[contains(text(), 'Флюоресцентная булка')]/parent::a")
    NAME_BUN_FLUORESCENT = (By.XPATH, "//p[contains(text(), 'Флюоресцентная булка')]")