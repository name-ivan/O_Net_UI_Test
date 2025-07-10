import allure


@allure.title("Verify Twitch video loads after searching for a game")
@allure.description("The test emulates a user searching for 'StarCraft II' on the Twitch mobile site and verifies the video loads.")
def test_the_twitch(driver, main_page, result_page, opened_video_page):
    print(f"\nRunning on device: {driver.device_name}")

    with allure.step("Open the Twitch main page"):
        main_page.open_page()

    with allure.step("Search for 'StarCraft II'"):
        main_page.search('StarCraft II')

    with allure.step("Scroll down twice"):
        result_page.scroll_down(200, 2)
    
    with allure.step("Wait for search results and click the first video"):
        result_page.click_result_video()
        
    with allure.step("Verify video player is visible"):
        assert opened_video_page.verify_video_opened(), "Video did not load properly"

    with allure.step("Save and attach screenshot of the loaded video"):
        opened_video_page.save_and_attach_screenshot("video_loaded")
