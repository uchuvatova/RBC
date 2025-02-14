from playwright.sync_api import Page, Response


class Base:
    """Базовые методы для переиспользования в классах страниц"""
    def __init__(self, page: Page):
        """
        Создает экземпляр класса Page, чтобы он был доступен во всех методах класса Base,
        что позволит выполнять действия на веб-страницах
        """
        self.page = page

    def open(self, uri) -> Response | None:
        """
        Открывает URL
        :param uri: str
        :return:
        """
        return self.page.goto(uri, wait_until='domcontentloaded')

    def click(self, locator: str) -> None:
        """
        Делает клик по локатору, при необходимости сам делает скролл к нужному элементу
        :param locator: str
        :return:
        """
        self.page.click(locator)

