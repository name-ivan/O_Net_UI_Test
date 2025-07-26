from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from locators.result_page_locators import ResultPageLocators as result_loc
from locators.opened_video_page_locators import OpenedVideoPageLocators as video_loc
from selenium.common.exceptions import TimeoutException


class ResultPage(BasePage):
    """
    Represents the Twitch search results page.
    """

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_available_video_result(self):
        """
        Clicks the first video result from the search results.
        If a mature content warning appears, clicks the 'Start Watching' button to proceed.
        """
        self.wait_for_visible(result_loc.VIEW_ALL_RESULTS_INDICATOR)
        self.wait_for_clickable(result_loc.VIDEO_RESULT).click()

        try:
            # Localized 5-second wait
            mature_content_button = self.wait_for_clickable(video_loc.START_WATCHING_BUTTON, timeout=5)
            mature_content_button.click()
        except TimeoutException:
            # No warning appeared — nothing to handle
            pass
