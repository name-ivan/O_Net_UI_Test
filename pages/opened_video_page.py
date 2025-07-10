from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from locators.twitch_locators import Locators


class OpenedVideoPage(BasePage):
    """
    Represents the opened Twitch video page.
    """

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def verify_video_opened(self):
        """Returns True if the video player is visible."""
        video_player = self.wait_for_visible(Locators.CLICKED_VIDEO_OPENED_LOC)
        return video_player.is_displayed()
