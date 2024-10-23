from selenium.webdriver.common.by import By


class FeedLocators:
    FEED_ORDERS = (By.XPATH, "//div[contains(@class, 'feed__order')]")
