import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    MoveTargetOutOfBoundsException,
    StaleElementReferenceException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from . import locators
from .base import BaseWebElement
from .utils import polling


class ProductCard(BaseWebElement):

    """Represents product card on `index` page."""

    locators = locators.ProductCardLocators()

    def add_to_cart(self):
        """Add product to shopping cart."""
        self.move_to()
        self.add_to_cart_button.click()

    @property
    def add_to_cart_button(self, timeout: int = 10):
        """
        Finds `add to card` button on product card, move to it, waits when
        button will become clickable and returns it.
        """
        button = self.find_element(*self.locators.ADD_TO_CART_BUTTON)
        ActionChains(self.parent).move_to_element(button).perform()
        WebDriverWait(self.parent, timeout).until(
            EC.element_to_be_clickable(self.locators.ADD_TO_CART_BUTTON)
        )
        return button

    def move_to(self) -> None:
        """
        Method scrolls view to product card and move mouse to it
        to show hidden buttons.
        """
        self.parent.execute_script(
            'arguments[0].scrollIntoView()',
            self.element
        )
        ActionChains(self.parent).move_to_element(self.element).perform()

    @property
    def product_name(self):
        """Returns product name from product card element."""
        product = self.find_element(*self.locators.PRODUCT_NAME_LINK)
        return product.text

    @property
    def product_price(self):
        """Returns product price from product card element."""
        price = self.find_element(*self.locators.PRODUCT_PRICE)
        return float(price.text.replace('$', ''))

    @property
    def quick_view_button(self):
        """Returns `quick view button` element."""
        return self.find_element(*self.locators.QUICK_VIEW_BUTTON)

    def show_quick_view(self, timeout: int = 10) -> None:
        """
        Moves to product card element, finds `quick view button`, clicks on it
        and waits when quick view will be loaded and then switches
        to quick view <iframe>.
        """
        self.move_to()
        self.quick_view_button.click()
        WebDriverWait(self.parent, timeout).until(
            EC.frame_to_be_available_and_switch_to_it(self.locators.QUICK_VIEW)
        )


class LayerCart(BaseWebElement):

    """
    Represents `layer cart` on index page. This cart appears after clicking
    on `add to cart` button on product card.
    """

    locators = locators.LayerCartLocators()

    @property
    def checkout_button(self):
        """Returns `checkout button` element."""
        return self.find_element(*self.locators.CHECKOUT_BUTTON)

    @property
    def continue_button(self):
        """Returns `continue button` element by clicking on it `layer cart`
        will be closed."""
        return self.find_element(*self.locators.CONTINUE_BUTTON)

    @property
    def product_name(self):
        """Returns product name from `layer cart` element."""
        product_name = self.find_element(*self.locators.PRODUCT_TITLE)
        return product_name.text

    @property
    def product_price(self):
        """Returns product price from `layer cart` element."""
        product_price = self.find_element(*self.locators.PRODUCT_PRICE)
        return float(product_price.text.replace('$', ''))

    @property
    def product_quantity(self):
        """Returns product quantity from `layer cart` element."""
        product_quantity = self.find_element(*self.locators.PRODUCT_QUANTITY)
        return int(product_quantity.text)


class ShoppingCart(BaseWebElement):

    """
    Represents shopping cart element that positions on top right angle after
    navbar on `index page`.
    """

    locators = locators.ShoppingCartLocators()

    @property
    def content(self):
        """Returns `content` of shopping cart."""
        return self.find_element(*self.locators.CONTENT)

    @property
    def empty(self):
        """
        Returns `empty` shopping cart element.
        This element is visible if there are no products in shopping cart.
        """
        return self.find_element(*self.locators.EMPTY_CART)

    @property
    def quantity(self):
        """
        Returns `(empty)` string if shopping cart is empty, otherwise returns
        quantity of products in shopping cart.
        """
        if not self.is_empty():
            quantity = self.find_element(*self.locators.CART_QUANTITY)
            return int(quantity.text)
        return self.empty.text

    def is_empty(self):
        """
        Checking if shopping cart is empty or not. Returns boolean value.
        """
        if self.empty.is_displayed():
            return True
        return False

    def move_to(self):
        """
        Moves mouse to shopping cart element to show hidden `dropdown` content.
        """
        cart_link = self.find_element(*self.locators.CART_LINK)
        ActionChains(self.parent).move_to_element(cart_link).perform()

    def show_content(self, timeout: int = 10) -> None:
        """
        Moves mouse to shopping cart element to show hidden `dropdown` content.
        If shopping cart not visible in the browsers view, method scrolls view
        to cart element and then moves mouse pointer to it.
        """
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
        """Returns list of products elements in shopping cart."""
        return self.find_elements(*self.locators.PRODUCTS)

    @property
    def products_quantity(self):
        """Returns products quantity in shopping cart."""
        return len(self.products)

    def remove_product(self, item_number: int = 0, timeout: int = 10) -> None:
        """
        Removes product from product list in shopping cart by position
        number.
        """
        if not self.content.is_displayed():
            self.show_content()

        product = self.products[item_number]
        remove_button = product.find_element(*self.locators.PRODUCT_REMOVE)
        remove_button.click()
        WebDriverWait(self.parent, timeout).until(
            EC.invisibility_of_element_located(product)
        )

    def remove_all_products(self):
        """
        Removes all products from shopping cart.
        """
        if not self.content.is_displayed():
            self.show_content()
        for product_number in range(len(self.products)):
            self.remove_product(product_number)

    @property
    def shipping_price(self):
        """Returns shipping price."""
        shipping_price = self.find_element(*self.locators.SHIPPING_PRICE)
        return float(shipping_price.text.replace('$', ''))

    @property
    def total_price(self):
        """
        Returns total price of shopping cart including prices of all
        products plus shipping price.
        """
        total_price = self.find_element(*self.locators.TOTAL_PRICE)
        return float(total_price.text.replace('$', ''))


class QuickView(BaseWebElement):

    """
    Represents `quick view` of product. This element represented as <iframe>.
    It appears after clicking on products card's `quick view`
    button.
    """

    locators = locators.QuickViewLocators()

    def change_size(self, size: str):
        """Changes size of product in <select> element."""
        self.size_select.select_by_value(size)

    def decrease_quantity(self):
        """Decreases quantity of product by clicking on `minus button`."""
        self.minus_button.click()

    def increase_quantity(self, num: int = 1, timeout: int = 1):
        """Increases quantity of product by clicking on `plus button`."""
        for _ in range(num):
            self.plus_button.click()
            time.sleep(timeout)

    @property
    def minus_button(self):
        """Returns `minus button` element."""
        return self.find_element(*self.locators.MINUS_BUTTON)

    @property
    def plus_button(self):
        """Returns `plus button` element."""
        return self.find_element(*self.locators.PLUS_BUTTON)

    @property
    def price(self):
        """Returns price of product."""
        price = self.find_element(*self.locators.PRICE)
        return float(price.text.remove('$', ''))

    @property
    def quantity(self):
        """Returns quantity of product."""
        quantity = self.find_element(*self.locators.QUANTITY_INPUT)
        return int(quantity.get_attribute('value'))

    @property
    @polling(StaleElementReferenceException, retry=5)
    def size(self):
        """Returns size of product."""
        return self.find_element(*self.locators.SIZE_RENDERED).text

    @property
    def selected_size_option(self):
        """Returns selected size value of sizes <select> element."""
        return self.size_select.first_selected_option.value

    @property
    def size_select(self):
        """Returns size's <select> element as instance of selenium `Select`."""
        element = self.find_element(*self.locators.SIZE_SELECT)
        return Select(element)
