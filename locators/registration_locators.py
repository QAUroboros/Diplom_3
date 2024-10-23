from selenium.webdriver.common.by import By


class RegistrationLocators:
    NAME = (By.XPATH, "//label[text()='Имя']/following::input[1]")
    EMAIL = (By.XPATH, "//label[text()='Email']/following::input[1]")
    PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    TITLE_FORM = (By.XPATH, "//h2[text()='Вход']")