from playwright.sync_api import Page

from tests.ui_tests.Locators.main import Main
from tests.ui_tests.pages.base import Base

MAIN_URL = "https://rbc.ru"


class MainPage(Base):
    """Методы для страницы входа в консоль"""

    def __init__(self, page: Page):
        super().__init__(page)

    def goto(self):
        """Открывает страницу входа в консоль"""
        self.open(MAIN_URL)

    def click_close_tv_popup_button(self):
        """Отмечает чек-бокс согласия с Условиями использования"""
        self.click(Main.CLOSE_TV_POPUP_BTN)

    def click_button_profile(self):
        """Нажимает кнопку Вход в консоль"""
        self.click(Main.PROFILE_BTN)

