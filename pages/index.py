from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond

from pages.base import BasePage
from pages.locators import IndexPageLocators


class IndexPage(BasePage):

    url = 'http://automationpractice.com/'
    locators = IndexPageLocators()

    def load(self):
        """
        Loads `index` page of web store.
        """
        self.browser.get(self.url)

    @property
    def title(self):
        """
        Returns web page title.
        """
        return self.browser.title

    def get_product_card(self):
        """
        Returns `product card element`.
        """
        return self.browser.find_element(*self.locators.PRODUCT_CARD)

    def get_quick_view_button(self, locator):
        """
        Returns `quick view link` button by locator.
        """
        return self.browser.find_element(*locator)

    def get_quick_view(self):
        """
        Returns products `quick view` element.
        """
        return self.browser.find_element(*self.locators.PRODUCT)

    def show_quick_view_button(self):
        """
        Moves mouse to product card element to show hidden button link
        on desktop browser.
        """
        product_card = self.get_product_card()
        ActionChains(self.browser).move_to_element(product_card).perform()

    def show_quick_view(self, mobil=False):
        """
        Depending on the mobile or non-mobile browser, it receives
        the `quick link` button element, moves to it and clicks on it
        to load the iframe` quick view`.

        :param mobil bool:  if True browser has mobil window size else browser
                            has desktop window size
        """
        if mobil:
            quick_view_button = self.get_quick_view_button(
                self.locators.QUICK_LINK_BUTTON_MOBIL
            )
        else:
            quick_view_button = self.get_quick_view_button(
                self.locators.QUICK_LINK_BUTTON
            )

        ActionChains(self.browser).move_to_element(
            quick_view_button
        ).click().perform()

        WebDriverWait(self.browser, 30).until(
            cond.frame_to_be_available_and_switch_to_it(
                self.locators.QUICK_VIEW
            )
        )

    def get_shopping_cart_quantity(self):
        """
        Gets quantity of products in the shopping cart.
        """
        display_prop = self.browser.find_element(
            *self.locators.SHOPPING_CART_EMPTY
        ).value_of_css_property('display')

        if display_prop != 'none':
            return 0

        quantity = self.browser.find_element(
            *self.locators.SHOPPING_CART_QUANTITY
        ).get_attribute('innerHTML')

        return int(quantity)
