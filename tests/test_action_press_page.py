from playwright.sync_api import expect
from utils.data import action, title_action
from utils.hard_file import action_count


class TestActionPage:
    def test_action_press_page(self, action_page, assertions):
        assertions.assert_elements_count(action_page.collections_of_repeating_locators(), action_count, "action")
        assertions.base_assertions(action_page)
        expect(action_page.recommended_publications_locator()).to_have_text(action)

    def test_url_action_page(self, action_page):
        expect(action_page.page).to_have_title(title_action)
        expect(action_page.page).to_have_url(action_page.composite_url())
