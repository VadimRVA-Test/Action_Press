from playwright.sync_api import expect
from utils.data import about_content_title, about_static, about_banner_title, title_about
from utils.hard_file import about_count


class TestAboutPage:
    def test_about_page(self, action_page, about_page, assertions):
        action_page.footer_control.click_footer_about_button()
        assertions.assert_elements_count(about_page.collections_of_repeating_locators(), about_count, "about")
        assertions.base_assertions(about_page)
        expect(about_page.content_title_locator()).to_have_text(about_content_title)
        expect(about_page.banner_text_title_locator()).to_have_text(about_banner_title)
        expect(about_page.static_locator()).to_have_text(about_static)

    def test_url_about_page(self, action_page, about_page):
        action_page.footer_control.click_footer_about_button()
        expect(action_page.page).to_have_title(title_about)
        expect(action_page.page).to_have_url(action_page.composite_url(about_page.ABOUT_URL))
