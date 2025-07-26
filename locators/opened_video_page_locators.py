from selenium.webdriver.common.by import By


class OpenedVideoPageLocators:
    VIDEO_PLAYER = (By.CSS_SELECTOR, 'div[data-a-target="video-player"]')
    START_WATCHING_BUTTON = (By.CSS_SELECTOR, 'button[data-a-target="content-classification-gate-overlay-start-watching-button"]')
