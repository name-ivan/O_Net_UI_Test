from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from locators.main_page_locators import MainPageLocators as main_loc
from locators.common_locators import CommonLocators as common_loc
from locators.result_page_locators import ResultPageLocators as result_loc
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    page_url = ''

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def search(self, text_to_search):
        self.wait_for_clickable(common_loc.BROWSE_BUTTON).click()
        search_input = self.wait_for_visible(main_loc.SEARCH_INPUT_FIELD)
        search_input.clear()
        search_input.send_keys(text_to_search)
        search_input.send_keys(Keys.ENTER)
        self.wait_for_visible(result_loc.VIEW_ALL_RESULTS_INDICATOR)

    def search_new(self, text_to_search):
        self.wait_for_clickable(common_loc.BROWSE_BUTTON).click()

        # Handle optional "Try the App" popup if it appears
        try:
            self.wait_for_visible(common_loc.TRY_APP_POPUP, timeout=5).click()
        except TimeoutError:
            pass  # Popup didn't appear, proceed normally

        search_input = self.wait_for_visible(main_loc.SEARCH_INPUT_FIELD)
        search_input.clear()
        search_input.send_keys(text_to_search)
        search_input.send_keys(Keys.ENTER)
        self.wait_for_visible(result_loc.VIEW_ALL_RESULTS_INDICATOR)
