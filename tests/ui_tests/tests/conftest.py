import pytest
from playwright.sync_api import sync_playwright, Page

from tests.ui_tests.pages.main_page import MainPage


@pytest.fixture
def page():
    """
    Запускает браузер Chrome
    Открывает окно браузера с указаными размерами
    Переходит на base_url
    После прохождения закрывается страница, браузер
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(args=['--disable-notifications'], headless=False)
        context = browser.new_context(viewport={"width": 1000, "height": 720})
        page = context.new_page()
        page.base_url = 'https://rbc.ru/'

        yield page

        page.close()
        context.close()
        browser.close()


def handle_dialog(dialog):
    assert dialog.type == 'beforeunload'
    dialog.dismiss()


@pytest.fixture
def main_page(page: Page):
    """Возвращает главную страницу"""
    return MainPage(page)
