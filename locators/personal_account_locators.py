from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    TITLE_PERSONAL_AREA = None
    BUTTON_EXIT = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3')]")
    TITLE_FORM = (By.XPATH, "//h2[text()='Вход']")