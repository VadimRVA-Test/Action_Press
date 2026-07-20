import re
from playwright.sync_api import expect, BrowserContext
from utils.credentials import credentials2
from utils.data import AUTHORIZ_URL


class TestAuthorization:
    def test_visible_authorization_page(self, auth_page, context: BrowserContext, assertions):
        auth_page.open_page()
        with context.expect_page() as new_page:
            auth_page.header_control.click_button_profile()
        auth_page.page = new_page.value
        assertions.all_locator(auth_page.collection_of_unique_locator())

    def test_url_authorization_page(self, action_page, context: BrowserContext):
        with context.expect_page() as new_page:
            action_page.header_control.click_button_profile()
        action_page.page = new_page.value
        expect(action_page.page).to_have_url(re.compile(re.escape(AUTHORIZ_URL) + ".*"))

    def test_authorization(self, auth_user_page):
        expect(auth_user_page.header_control.profile_name_locator()).to_have_text(credentials2)

    def test_menu_auth_user(self, auth_user_page, assertions):
        auth_user_page.header_control.click_button_profile()
        assertions.all_locator(auth_user_page.header_control.profile_button_locators())
