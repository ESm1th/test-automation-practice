from base import BasePage
from index import IndexPage
from locators import QuickProductViewLocators


class QuickViewProductPage(BasePage):

    locators = QuickProductViewLocators()

    def load(self):
        index_page = IndexPage(self.browser)
        index_page.load()
        index_page.show_quick_view_button()
        index_page.show_quick_view()
