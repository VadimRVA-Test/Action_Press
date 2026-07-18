from playwright.sync_api import expect
from utils.data import (ABOUT_URL,
                        header,
                        catalog,
                        menu_news,
                        all_news,
                        menu_advantages,
                        about_content_title,
                        about_static, about_banner_title)
from utils.hard_file import menu_news_count, menu_advantage_count, about_count


def test_about_page(action_page, about_page, assertions):
    action_page.footer_control.footer_about_button_locator().click()
    about_page.page = action_page.page
    expect(about_page.page).to_have_url(ABOUT_URL)
    assertions.all_locator(about_page.header_control.visible_elements())
    expect(about_page.header_control.header_locator()).to_have_attribute("data-qa-locator", header)
    expect(about_page.menu_catalog.catalog_locator()).to_have_text(catalog)
    assertions.all_locator(about_page.menu_catalog.visible_elements())
    expect(about_page.menu_catalog.catalog_locator()).to_have_text(catalog)
    assertions.all_locator(about_page.menu_news.visible_elements())
    count_elements = assertions.all_index_locator(about_page.menu_news.list_elements())
    assert assertions.all_index_locator(about_page.menu_news.list_elements()) == menu_news_count, (
        f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements}")
    expect(about_page.menu_news.news_locator()).to_have_text(menu_news)
    expect(about_page.menu_news.all_news_locator()).to_have_text(all_news)
    expect(about_page.menu_advantages.advantages_locator()).to_have_text(menu_advantages)
    count_elements2 = assertions.all_index_locator(about_page.menu_advantages.list_elements())
    assert assertions.all_index_locator(about_page.menu_advantages.list_elements()) == menu_advantage_count, (
        f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements2}")
    count_elements3 = assertions.all_index_locator(about_page.list_elements())
    assert assertions.all_index_locator(about_page.list_elements()) == about_count, (
        f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements3}")
    expect(about_page.content_title_locator()).to_have_text(about_content_title)
    expect(about_page.banner_text_title_locator()).to_have_text(about_banner_title)
    expect(about_page.static_locator()).to_have_text(about_static)
