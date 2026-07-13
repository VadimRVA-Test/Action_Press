from playwright.sync_api import expect


def test_action_press_page(action_page):
    action_page.open_page()
    expect(action_page.page).to_have_url("https://action-press.ru/")
    # action_page.close_button.accept_cookies_button_locator().click()
    # action_page.close_button.close_jiva_button_locator().click()
    for locator in action_page.header_control.visible_elements():
        expect(locator).to_be_visible()
    for locator in action_page.menu_catalog.visible_elements():
        expect(locator).to_be_visible()
    for locator in action_page.menu_news.visible_elements():
        expect(locator).to_be_visible()
    for locator in action_page.menu_advantages.visible_elements():
        expect(locator).to_be_visible()
    for locator in action_page.visible_elements():
        expect(locator).to_be_visible()
