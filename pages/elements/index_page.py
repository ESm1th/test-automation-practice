from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import MoveTargetOutOfBoundsException

from . import locators
from .base import BaseWebElement


class ProductCard(BaseWebElement):

    locators = locators.ProductCardLocators()

    def add_to_cart(self):
        self.move_to()
        self.add_to_cart_button.click()

    @property
    def add_to_cart_button(self):
        return self.find_element(*self.locators.ADD_TO_CART_BUTTON)

    @property
    def more_button(self):
        return self.find_element(*self.locators.MORE_BUTTON)

    def move_to(self):
        ActionChains(self.parent).move_to_element(self.element).perform()

    @property
    def product_name(self):
        product = self.find_element(*self.locators.PRODUCT_NAME_LINK)
        return product.text

    @property
    def product_price(self):
        price = self.find_element(*self.locators.PRODUCT_PRICE)
        return float(price.text.replace('$', ''))

    @property
    def quick_view_button(self):
        return self.find_element(*self.locators.QUICK_VIEW_BUTTON)


class LayerCart(BaseWebElement):

    locators = locators.LayerCartLocators()

    @property
    def checkout_button(self):
        return self.find_element(*self.locators.CHECKOUT_BUTTON)

    @property
    def continue_button(self):
        return self.find_element(*self.locators.CONTINUE_BUTTON)

    @property
    def product_name(self):
        product_name = self.find_element(*self.locators.PRODUCT_TITLE)
        return product_name.text

    @property
    def product_price(self):
        product_price = self.find_element(*self.locators.PRODUCT_PRICE)
        return product_price.text

    @property
    def product_quantity(self):
        product_quantity = self.find_element(*self.locators.PRODUCT_QUANTITY) 
        return int(product_quantity.text)


class ShoppingCart(BaseWebElement):

    locators = locators.ShoppingCartLocators()

    @property
    def empty(self):
        return self.find_element(*self.locators.EMPTY_CART)

    @property
    def quantity(self):
        if not self.is_empty():
            quantity = self.find_element(*self.locators.CART_QUANTITY)
            return int(quantity.text)
        return self.empty.text

    def is_empty(self):
        if self.empty.is_displayed():
            return True
        return False

    def move_to(self):
        ActionChains(self.parent).move_to_element(self.element).perform()

    def show_content(self):
        try:
            self.move_to()
        except MoveTargetOutOfBoundsException:
            self.parent.execute_script(
                'arguments[0].scrollIntoView()', self.element
            )
            self.move_to()

    @property
    def products(self):
        return self.find_elements(*self.locators.PRODUCTS)

    @property
    def products_quantity(self):
        return len(self.products)

    @property
    def shipping_price(self):
        shipping_price = self.find_element(*self.locators.SHIPPING_PRICE)
        return float(shipping_price.text.replace('$', ''))

    @property
    def total_price(self):
        total_price = self.find_element(*self.locators.TOTAL_PRICE)
        return float(total_price.text.replace('$', ''))
