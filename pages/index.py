from pages.base import BasePage
from pages.locators import IndexPageLocators
from pages.elements import index_page as elements


class IndexPage(BasePage):

    url = 'http://automationpractice.com/'
    locators = IndexPageLocators()
    elements = {}

    def add_product_to_cart(self):
        """
        Add product to cart from product card by clicking button 'Add to cart'.
        """
        self.product_card.add_to_cart()
        self.layer_cart.continue_button.click()

    @property
    def product_card(self):
        """Returns `product_card` element."""
        return self.get_element(
            'product_card', self.locators.PRODUCT_CARD, elements.ProductCard
        )

    @property
    def layer_cart(self):
        """Returns `layer_cart` element."""
        return self.get_element(
            'layer_cart', self.locators.LAYER_CART, elements.LayerCart
        )

    @property
    def shopping_cart(self):
        """Returns `shopping_cart` element."""
        return self.get_element(
            'shopping_cart', self.locators.SHOPPING_CART, elements.ShoppingCart
        )

    @property
    def quick_view(self):
        """Returns `quick_view` iframe for specific product"""
        return self.get_element(
            'quick_view', self.locators.QUICK_VIEW, elements.QuickView
        )

    def show_quick_view(self):
        """Show product's `quick_view` <iframe> and switch to it."""
        self.product_card.show_quick_view()

    def close_quick_view(self):
        """
        Switch to default content to find `close` button and close
        `quick_view`.
        """
        self.browser.switch_to.default_content()
        close_btn = self.browser.find_element(*self.locators.CLOSE_QUICK_VIEW)
        close_btn.click()
