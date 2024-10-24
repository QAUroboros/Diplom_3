from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGIN_BUTTON = (By.XPATH, "//section[2]/div/button[text()='Войти в аккаунт']")
    CHECKOUT_BUTTON = (By.XPATH, "//section[2]/div/button[text()='Оформить заказ']")
    DIV_BUNS = (By.XPATH, "//span[text()='Булки']/parent::div")
    BUN_FLUORESCENT = (By.XPATH, "//p[contains(text(), 'Флюоресцентная булка')]/parent::a")
    FLUORESCENT_BUN = (By.CSS_SELECTOR, "img[alt='Флюоресцентная булка R2-D3']")
    NAME_BUN_FLUORESCENT = (By.XPATH, "//p[contains(text(), 'Флюоресцентная булка')]")