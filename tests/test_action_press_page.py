from playwright.sync_api import expect
from utils.data import menu_news, all_news, menu_advantages, URl, action, catalog, header
from utils.hard_file import menu_news_count, menu_advantage_count, action_count


def test_action_press_page(action_page, assertions):
    expect(action_page.page).to_have_url(URl)
    assertions.all_locator(action_page.header_control.visible_elements())
    expect(action_page.header_control.header_locator()).to_have_attribute("data-qa-locator", header)
    expect(action_page.menu_catalog.catalog_locator()).to_have_text(catalog)
    assertions.all_locator(action_page.menu_catalog.visible_elements())
    expect(action_page.menu_catalog.catalog_locator()).to_have_text(catalog)
    assertions.all_locator(action_page.menu_news.visible_elements())
    count_elements = assertions.all_index_locator(action_page.menu_news.list_elements())
    assert assertions.all_index_locator(action_page.menu_news.list_elements()) == menu_news_count, (
        f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements}")
    expect(action_page.menu_news.news_locator()).to_have_text(menu_news)
    expect(action_page.menu_news.all_news_locator()).to_have_text(all_news)
    expect(action_page.menu_advantages.advantages_locator()).to_have_text(menu_advantages)
    count_elements2 = assertions.all_index_locator(action_page.menu_advantages.list_elements())
    assert assertions.all_index_locator(action_page.menu_advantages.list_elements()) == menu_advantage_count, (
        f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements2}")
    assertions.all_locator(action_page.visible_elements())
    count_elements3 = assertions.all_index_locator(action_page.list_elements())
    assert assertions.all_index_locator(action_page.list_elements()) == action_count, (
        f"Ожидали количество элементов {action_count}! Получили: {count_elements3}")
    expect(action_page.recommended_publications_locator()).to_have_text(action)
