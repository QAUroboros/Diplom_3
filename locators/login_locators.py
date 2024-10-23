from selenium.webdriver.common.by import By


class LoginLocators:
    TITLE_FORM = (By.XPATH, "//h2[text()='Вход']")
    EMAIL = (By.XPATH, "//input[@name='name']")
    PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")
    LINK_FORGOT_PASSWORD = (By.XPATH, "//a[@href='/forgot-password']")
    CHECKOUT_BUTTON = (By.XPATH, "//section[2]/div/button[text()='Оформить заказ']")