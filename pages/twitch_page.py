# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.keys import Keys
# from pathlib import Path
# import allure
# from locators.locators import Locators
# from time import sleep
# from pages.base_page import BasePage


# class TwitchPage(BasePage):
#     """
#     Page Object Model for Twitch mobile web interactions.
#     """
#     page_url = ''

#     def __init__(self, driver: WebDriver):
#         """
#         Initialize the TwitchPage with a Selenium WebDriver instance.
#         """
#         super().__init__(driver)

#     # def navigate_to_twitch(self):
#     #     """
#     #     Navigate to the Twitch mobile homepage.
#     #     """
#     #     self.driver.get('https://m.twitch.tv/')

#     def click_browse_button(self):
#         """
#         Wait for and click the 'Browse' button on the Twitch homepage.
#         """
#         browse_button = WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable(Locators.BROWSE_BUTTON_LOC)
#         )
#         browse_button.click()

#     def search_query(self, text_to_search):
#         """
#         Enter a search term into the Twitch search input and submit it.
        
#         Args:
#             text_to_search (str): The term to search for.
#         """
#         search_input = WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located(Locators.SEARCH_INPUT_FIELD)
#         )
#         search_input.send_keys(text_to_search)
#         search_input.send_keys(Keys.ENTER)

#     def wait_for_results_to_load(self):
#         """
#         Wait until the search results are fully loaded (when 'View All' appears).
#         """
#         WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located(Locators.VIEW_ALL_HTEXT)
#         )

#     def scroll(self, number_of_scrolls, scrolling_length):
#         """
#         Scroll the page down multiple times by a specified pixel length.

#         Args:
#             number_of_scrolls (int): How many times to scroll.
#             scrolling_length (int): The number of pixels to scroll each time.
#         """
#         for _ in range(number_of_scrolls):
#             self.driver.execute_script(f"window.scrollBy(0, {scrolling_length})")
#             sleep(3)

#     def click_the_video(self):
#         """
#         Click on the first video in the search results.
#         """
#         the_video = WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable(Locators.THE_VIDEO)
#         )
#         the_video.click()

#     def handle_adult_content_warning(self):
#         """
#         Attempt to click the 'Start Watching' button if the adult content overlay appears.
#         """
#         try:
#             start_button = WebDriverWait(self.driver, 5).until(
#                 EC.element_to_be_clickable(Locators.WATCH_LATER_BUTTON)
#             )
#             start_button.click()
#         except TimeoutException:
#             pass

#     def verify_video_opened(self):
#         """
#         Verify that the video player is visible after clicking a video.

#         Returns:
#             bool: True if the video player is displayed, False otherwise.
#         """
#         video_player = WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located(Locators.CLICKED_VIDEO_OPENED)
#         )
#         return video_player.is_displayed()

#     def save_screenshot_to_folder(self):
#         """
#         Save a screenshot of the current page into the screenshots folder.

#         Returns:
#             Path: The full path to the saved screenshot.
#         """
#         screenshots_dir = Path(__file__).parent.parent / "screenshots"
#         screenshots_dir.mkdir(exist_ok=True)
#         screenshot_path = screenshots_dir / f'twitch_{self.driver.device_name.replace(" ", "_").lower()}_video_loaded.png'
#         self.driver.save_screenshot(str(screenshot_path))
#         return screenshot_path
