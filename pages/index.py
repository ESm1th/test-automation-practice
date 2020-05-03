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

    def show_quick_view(self, mobil: bool = False):
        """
        Depending on the mobile or non-mobile browser, it receives
        the `quick link` button element, moves to it and clicks on it
        to load the `iframe` quick view.

        @param mobil:  if True browser has mobil window size else browser
                            has desktop window size
        """
        self.move_to_product_card()
        self.product_card.quick_view_button.click()

        WebDriverWait(self.browser, 30).until(
            EC.frame_to_be_available_and_switch_to_it(
                self.locators.QUICK_VIEW
            )
        )
