from playwright.sync_api import expect


def test_abut_page(about_page):
    about_page.open_page(about_page.ABOUT_URL)
    expect(about_page.page).to_have_url("https://action-press.ru/about/")
    for locator in about_page.visible_elements():
        expect(locator).to_be_visible()
