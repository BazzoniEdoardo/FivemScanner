from playwright.sync_api import sync_playwright

from modules.GuiModule import *


class ServerConnection:
    def __init__(self, id: str):
        self.id = id

        #Request's Url
        self.serverUrl = "https://servers-frontend.fivem.net/api/servers/single/" + self.id

        #Request's Json Data
        self.jsonData = None

    # Requesting all the server data
    def RequestServerInfo(self):

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)

            page = browser.new_page(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/139.0.0.0 Safari/537.36"
            )

            with page.expect_response(self.serverUrl) as resp_info:
                page.goto(self.serverUrl)
            response = resp_info.value

            if response.status != 200:
                PrintError(response.status)

            self.jsonData = response.json()

            browser.close()


