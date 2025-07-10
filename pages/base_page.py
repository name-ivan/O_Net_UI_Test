from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
from urllib.parse import urljoin
import allure


class BasePage:
    """Base class for all page objects. Provides common utilities for navigation and interaction."""

    base_url = 'https://m.twitch.tv/'
    page_url = None

    def __init__(self, driver: WebDriver, timeout: int = 10):
        """Initialize with WebDriver and wait timeout."""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def open_page(self):
        """Open the full page URL (base + relative path)."""
        if self.page_url is None:
            raise NotImplementedError(f'{self.__class__.__name__} does not define page_url')

        full_url = urljoin(self.base_url, self.page_url)
        self.driver.get(full_url)

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def scroll_down(self, pixels: int, times: int = 1):
        """Scroll down the page by given pixels."""
        for _ in range(times):
            self.driver.execute_script(f'window.scrollBy(0, {pixels})')

    def save_screenshot(self, name: str) -> Path:
        """
        Saves a screenshot and returns the file path.
        Screenshot is saved in the 'screenshots' directory.
        """
        screenshot_dir = Path(__file__).parent.parent / 'screenshots'
        screenshot_dir.mkdir(exist_ok=True)
        screenshot_path = screenshot_dir / f'{name}.png'
        self.driver.save_screenshot(str(screenshot_path))
        return screenshot_path

    def save_and_attach_screenshot(self, name: str) -> Path:
        """
        Saves a screenshot and attaches it to the Allure report.
        Returns the path to the saved screenshot.
        """
        screenshot_path = self.save_screenshot(name)
        if screenshot_path.exists():
            allure.attach.file(
                str(screenshot_path),
                name=name,
                attachment_type=allure.attachment_type.PNG
            )
        return screenshot_path
