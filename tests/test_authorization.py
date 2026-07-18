import re
from playwright.sync_api import expect, BrowserContext
from utils.credentials import credentials, credentials2
from utils.data import AUTHORIZ_URL


class TestAuthorization:
    def test_visible_authorization_page(self, auth_page, context: BrowserContext, assertions):
        auth_page.open_page()
        with context.expect_page() as new_page:
            auth_page.header_control.button_auth_reg_locator().click()
        auth_page.page = new_page.value
        assertions.all_locator(auth_page.visible_elements())
        expect(auth_page.page).to_have_url(re.compile(re.escape(AUTHORIZ_URL) + ".*"))

    def test_authorization(self, action_page, auth_page, context: BrowserContext):
        action_page.open_page()
        with context.expect_page() as new_page:
            action_page.header_control.button_auth_reg_locator().click()
        auth_page.page = new_page.value
        auth_page.authorize(credentials[0], credentials[1])
        action_page.open_page()
        expect(action_page.header_control.profile_name_locator()).to_have_text(credentials2)
