from selenium.webdriver.common.by import By


class Locators:
    BROWSE_BUTTON_LOC = (By.CSS_SELECTOR, 'a[href="/directory"]')
    SEARCH_INPUT_FIELD_LOC = (By.CSS_SELECTOR, 'input[type="search"]')
    VIEW_ALL_RESULTS_INDICATOR_LOC = (By.CSS_SELECTOR, 'p[aria-label="View All Channel Search Results"]')  # load indicator
    VIDEO_RESULT_LOC = (By.XPATH, '(//a[starts-with(@href, "/videos/") and .//img[contains(@src, "thumb")]])[1]')
    START_WATCHING_BUTTON_LOC = (By.CSS_SELECTOR, 'button[data-a-target="content-classification-gate-overlay-start-watching-button"]')
    CLICKED_VIDEO_OPENED_LOC = (By.CSS_SELECTOR, 'div[data-a-target="video-player"]')
