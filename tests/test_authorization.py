import re
from playwright.sync_api import expect, BrowserContext
from tests.credentials import credentials, credentials2


def test_authorization(action_page, auth_page, context: BrowserContext):
    action_page.open_page()
    expect(action_page.page).to_have_url("https://action-press.ru/")
    button = action_page.header_control.button_auth_reg_locator()
    with context.expect_page() as new_page:
        button.click()
    new_page = new_page.value
    url = auth_page.AUTH_URL
    expect(new_page).to_have_url(re.compile(re.escape(url) + ".*"))
    auth_page.page = new_page
    for locator in auth_page.visible_elements():
        expect(locator).to_be_visible()
    auth_page.authorize(credentials[0], credentials[1])
    action_page.open_page()
    new_page.close()
    expect(action_page.header_control.profile_name_locator()).to_have_text(credentials2)
    action_page.header_control.profile_name_locator().click()
    for locator in auth_page.header_control.profile_button():
        expect(locator).to_be_visible()
