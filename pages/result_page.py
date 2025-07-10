from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from locators.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class ResultPage(BasePage):
    """
    Represents the Twitch search results page.
    """

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def click_result_video(self):
        """
        Clicks the first video result from the search results.
        If a mature content warning appears, clicks the 'Start Watching' button to proceed.
        """
        self.wait_for_visible(Locators.VIEW_ALL_HTEXT_LOC)
        self.wait_for_clickable(Locators.THE_VIDEO_LOC).click()

        try:
            # Localized 5-second wait
            wait_short = WebDriverWait(self.driver, 5)
            mature_content_button = wait_short.until(
                EC.element_to_be_clickable(Locators.START_WATCHING_BUTTON_LOC)
            )
            mature_content_button.click()
        except TimeoutException:
            # No warning appeared — nothing to handle
            pass
