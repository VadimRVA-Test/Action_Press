import pytest
from playwright.sync_api import sync_playwright, Page
from pages.action_press_page import ActionPressPage
from pages.about_page import AboutPage
from pages.contacts_page import ContactsPage
from pages.payment_page import PaymentPage
from pages.auth_page import AuthPage
from utils.base_assertions import Assertions


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True, slow_mo=1000)
    yield browser
    browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context()
    try:
        yield context
    finally:
        context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    return page


@pytest.fixture
def auth_page(page):
    return AuthPage(page)


@pytest.fixture
def action_page(page):
    main_page = ActionPressPage(page)
    main_page.open_page()
    return main_page


@pytest.fixture
def about_page(page):
    return AboutPage(page)


@pytest.fixture
def contacts_page(page):
    return ContactsPage(page)


@pytest.fixture
def payment_page(page):
    return PaymentPage(page)


@pytest.fixture
def assertions(page):
    return Assertions(page)
