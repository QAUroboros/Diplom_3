from selenium.webdriver.common.by import By


class IngredientDetails_locators:
    INGREDIENT_MODAL = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div")
    MODAL_TITLE = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    MODAL_NAME_INGREDIENT = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div/p")
    MODAL_BUTTON_CLOSE = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div/following::button[1]")