from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond

from pages.base import BasePage
from pages.locators import IndexPageLocators, QuickProductViewLocators


class IndexPage(BasePage):
    
    url = 'http://automationpractice.com/'
    locators = IndexPageLocators()
    elements = {}

    def load(self):
        self.browser.get(self.url)
    
    @property
    def title(self):
        return self.browser.title

    @property
    def product_card(self):
        if not self.elements.get('product_card'):
            self.elements['product_card'] = self.get_product_card()
        return self.elements['product_card']

    @property
    def quick_view_button(self):
        if not self.elements.get('quick_view_button'):
            self.elements['quick_view_button'] = self.get_quick_view_button()
        return self.elements['quick_view_button']
    
    @property
    def quick_view(self):
        if not self.elements.get('quick_view'):
            self.elements['quick_view'] = self.get_quick_view()
        return self.elements['quick_view']

    def get_product_card(self):
        return self.browser.find_element(*self.locators.PRODUCT_CARD)

    def get_quick_view_button(self):
        return self.browser.find_element(*self.locators.QUICK_LINK_BUTTON)

    def get_quick_view(self):
        return self.browser.find_element(*self.locators.PRODUCT)

    def show_quick_view_button(self):
        ActionChains(self.browser).move_to_element(
            self.product_card
        ).perform()

    def show_quick_view(self):
        ActionChains(self.browser).move_to_element(
            self.quick_view_button
        ).click().perform()
        WebDriverWait(self.browser, 30).until(
            cond.frame_to_be_available_and_switch_to_it(
                self.locators.QUICK_VIEW
            )
        )


class QuickViewProductPage(BasePage):

    locators = QuickProductViewLocators()

    def load(self):
        index_page = IndexPage(self.browser)
        index_page.load()
        index_page.show_quick_view_button()
        index_page.show_quick_view()