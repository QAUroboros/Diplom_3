from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    PASSWORD = (By.XPATH, "//input[@name = 'Введите новый пароль']")
    BUTTON_ACTION_PASSWORD = (By.XPATH, "//*[contains(@class, 'input__icon-action')]")