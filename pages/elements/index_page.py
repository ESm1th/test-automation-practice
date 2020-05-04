import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from . import locators
from .base import BaseWebElement


class ProductCard(BaseWebElement):

    locators = locators.ProductCardLocators()

    def add_to_cart(self):
        self.move_to()
        self.add_to_cart_button.click()

    @property
    def add_to_cart_button(self, timeout: int = 10):
        button = self.find_element(*self.locators.ADD_TO_CART_BUTTON)
        ActionChains(self.parent).move_to_element(button).perform()
        WebDriverWait(self.parent, timeout).until(
            EC.element_to_be_clickable(self.locators.ADD_TO_CART_BUTTON)
        )
        return button

    @property
    def more_button(self):
        return self.find_element(*self.locators.MORE_BUTTON)

    def move_to(self) -> None:
        self.parent.execute_script(
            'arguments[0].scrollIntoView()',
            self.element
        )
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

    def show_quick_view(self, timeout: int = 10) -> None:
        self.move_to()
        self.quick_view_button.click()
        WebDriverWait(self.parent, timeout).until(
            EC.frame_to_be_available_and_switch_to_it(self.locators.QUICK_VIEW)
        )


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
        return float(product_price.text.replace('$', ''))

    @property
    def product_quantity(self):
        product_quantity = self.find_element(*self.locators.PRODUCT_QUANTITY)
        return int(product_quantity.text)


class ShoppingCart(BaseWebElement):

    locators = locators.ShoppingCartLocators()

    @property
    def content(self):
        return self.find_element(*self.locators.CONTENT)

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
        cart_link = self.find_element(*self.locators.CART_LINK)
        ActionChains(self.parent).move_to_element(cart_link).perform()

    def show_content(self, timeout: int = 10) -> None:
        try:
            self.move_to()
        except MoveTargetOutOfBoundsException:
            self.parent.execute_script(
                'arguments[0].scrollIntoView()', self.element
            )
            self.move_to()
        finally:
            if not self.content.is_displayed():
                WebDriverWait(self.parent, timeout).until(
                    EC.visibility_of(self.content)
                )

    @property
    def products(self):
        return self.find_elements(*self.locators.PRODUCTS)

    @property
    def products_quantity(self):
        return len(self.products)

    def remove_product(self, item_number: int = 0, timeout: int = 10) -> None:
        if not self.content.is_displayed():
            self.show_content()

        product = self.products[item_number]
        remove_button = product.find_element(*self.locators.PRODUCT_REMOVE)
        remove_button.click()
        WebDriverWait(self.parent, timeout).until(
            EC.invisibility_of_element_located(product)
        )

    def remove_all_products(self):
        if not self.content.is_displayed():
            self.show_content()
        for product_number in range(len(self.products)):
            self.remove_product(product_number)

    @property
    def shipping_price(self):
        shipping_price = self.find_element(*self.locators.SHIPPING_PRICE)
        return float(shipping_price.text.replace('$', ''))

    @property
    def total_price(self):
        total_price = self.find_element(*self.locators.TOTAL_PRICE)
        return float(total_price.text.replace('$', ''))


class QuickView(BaseWebElement):

    locators = locators.QuickViewLocators()

    def decrease_quantity(self):
        self.minus_button.click()

    def increase_quantity(self, num: int = 1, timeout: int = 10):
        for _ in range(num):
            self.plus_button.click()
            time.sleep(1)

    @property
    def minus_button(self):
        return self.find_element(*self.locators.MINUS_BUTTON)

    @property
    def plus_button(self):
        return self.find_element(*self.locators.PLUS_BUTTON)

    @property
    def price(self):
        price = self.find_element(*self.locators.PRICE)
        return float(price.text.remove('$', ''))

    @property
    def quantity(self):
        quantity = self.find_element(*self.locators.QUANTITY_INPUT)
        return int(quantity.get_attribute('value'))

    @property
    def size_select(self):
        element = self.find_element(*self.locators.SIZE_SELECT)
        return Select(element)

    @property
    def size(self):
        return self.size_select.first_selected_option.value
