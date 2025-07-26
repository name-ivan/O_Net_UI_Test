from selenium.webdriver.common.by import By


class CommonLocators:
    BROWSE_BUTTON = (By.CSS_SELECTOR, 'a[href="/directory"]')
    TRY_APP_POPUP = (By.CSS_SELECTOR, 'img[alt="Browser logo"]')
