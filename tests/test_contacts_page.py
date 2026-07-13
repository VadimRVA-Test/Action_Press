from playwright.sync_api import expect


def test_contacts_page(contacts_page):
    contacts_page.open_page(contacts_page.CONTACTS_URL)
    expect(contacts_page.page).to_have_url("https://action-press.ru/about/contacts/")
    for locator in contacts_page.visible_elements():
        expect(locator).to_be_visible()
