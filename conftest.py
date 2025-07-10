import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.result_page import ResultPage
from pages.opened_video_page import OpenedVideoPage


@pytest.fixture(params=['Pixel 2', 'iPhone 12 Pro'], scope='function')
def driver(request):
    # Configure Chrome to emulate a mobile device (Pixel 2)
    mobile_emulation = {"deviceName": request.param}

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # Optional: run in headless mode to speed up test execution
    # chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_options)
    driver.device_name = request.param
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver):
    return MainPage(driver)


@pytest.fixture()
def result_page(driver):
    return ResultPage(driver)


@pytest.fixture()
def opened_video_page(driver):
    return OpenedVideoPage(driver)