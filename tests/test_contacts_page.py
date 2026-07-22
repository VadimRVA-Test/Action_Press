from playwright.sync_api import expect
from utils.data import contacts, title_contacts
from utils.hard_file import contact_count


class TestContactPage:
    def test_contacts_page(self, action_page, contacts_page, assertions):
        action_page.footer_control.click_footer_contacts_button()
        assertions.assert_elements_count(contacts_page.collections_of_repeating_locators(), contact_count, "contacts")
        assertions.base_assertions(contacts_page)
        expect(contacts_page.static_page_locator()).to_have_text(contacts)

    def test_url_contacts_page(self, action_page, contacts_page):
        action_page.footer_control.click_footer_contacts_button()
        expect(action_page.page).to_have_title(title_contacts)
        expect(action_page.page).to_have_url(action_page.composite_url(contacts_page.CONTACTS_URL))
