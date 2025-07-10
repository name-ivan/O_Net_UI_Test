from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from locators.twitch_locators import Locators
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    page_url = ''

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def search(self, text_to_search):
        self.wait_for_clickable(Locators.BROWSE_BUTTON_LOC).click()
        search_input = self.wait_for_visible(Locators.SEARCH_INPUT_FIELD_LOC)
        search_input.clear()
        search_input.send_keys(text_to_search)
        search_input.send_keys(Keys.ENTER)
        self.wait_for_visible(Locators.VIEW_ALL_RESULTS_INDICATOR_LOC)
