from selenium.webdriver.common.by import By


class IngredientBunLocators:
    INGREDIENT_MODAL = (By.XPATH, "//p[contains(text(),'Флюоресцентный бургер')]")
    COUNTER_LOCATOR = (By.XPATH, "//span[@class='counter__num']")