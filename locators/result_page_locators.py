from selenium.webdriver.common.by import By


class ResultPageLocators:
    VIEW_ALL_RESULTS_INDICATOR = (By.CSS_SELECTOR, 'p[aria-label="View All Channel Search Results"]')
    VIDEO_RESULT = (By.XPATH, '(//a[starts-with(@href, "/videos/") and .//img[contains(@src, "thumb")]])[1]')
