import pytest

from pages.index import IndexPage


class TestIndexPage:

    @pytest.fixture
    def index_page(self, browser):
        index_page = IndexPage(browser)
        index_page.load()
        return index_page

    def test_add_product_to_cart(self, index_page):
        """
        Given: index page loaded and shopping cart is empty
        When:  moving to product card and clicking on `add to cart` button
        Then:  shopping cart quantity equals 1
        """
        index_page.add_product_to_cart()
        assert index_page.shopping_cart.quantity == 1

    def test_layer_cart_data(self, index_page):
        """
        Given: index page loaded and shopping cart is empty
        When:  moving to product card and clicking on `add to cart` button
        Then:  product name, product price on product card element equals
               to product name and product price on `layer cart` element
        And:   product quantity on `layer cart` element equals 1
        """
        product_card = index_page.product_card
        product_card.add_to_cart()
        layer_cart = index_page.layer_cart
        assert product_card.product_name == layer_cart.product_name
        assert product_card.product_price == layer_cart.product_price
        assert layer_cart.product_quantity == 1

    @pytest.mark.cart
    def test_check_empty_cart(self, index_page):
        """
        Given: index page loaded
        Then:  shopping cart is empty
        And:   shopping cart quantity is labeled with `(empty)` string
        """
        assert index_page.shopping_cart.is_empty()
        assert index_page.shopping_cart.quantity == '(empty)'

    @pytest.mark.cart
    def test_check_cart_with_product(self, index_page):
        """
        Given: index page loaded and shopping cart is empty
        When:  moving to product card and clicking on `add to cart` button
        Then:  shopping cart quantity equals 1
        And:   shopping cart is not labeled with `(empty)` string
        """
        index_page.add_product_to_cart()
        assert not index_page.shopping_cart.is_empty()
        assert index_page.shopping_cart.products_quantity == 1

    @pytest.mark.cart
    def test_check_cart_dropdown_prices(self, index_page):
        """
        Given: index page loaded and shopping cart is empty
        When:  moving to product card and clicking on `add to cart` button
        Then:  shopping cart shipping price equals 2
        And:   shopping cart total price equals to sum of product price and
               shipping price
        """
        index_page.add_product_to_cart()
        index_page.shopping_cart.show_content()

        product_price = index_page.product_card.product_price
        shipping_price = index_page.shopping_cart.shipping_price

        assert shipping_price == 2
        assert index_page.shopping_cart.total_price == (
            product_price + shipping_price
        )

    @pytest.mark.cart
    def test_remove_product_from_cart(self, index_page):
        """
        Given: index page loaded and shopping cart is empty
        When:  moving to product card and clicking on `add to cart` button
        And:   moving to shopping cart and removing product
        Then:  shopping cart is not labeled with `(empty)` string
        """
        index_page.add_product_to_cart()
        index_page.shopping_cart.show_content()
        index_page.shopping_cart.remove_product()
        assert index_page.shopping_cart.is_empty()

    @pytest.mark.quick_view
    def test_quick_view_displayed(self, index_page):
        """
        Given: index page loaded
        When:  moving to product card and clicking on `quick view` button
        Then:  quick view of product should be displayed
        """
        index_page.show_quick_view()
        assert index_page.quick_view.is_displayed()

    @pytest.mark.quick_view
    def test_quick_view_add_quantity(self, index_page):
        """
        Given: index page loaded
        When:  moving to product card and clicking on `quick view` button
        And:   increasing quantity of product by clicking on `plus` button
               2 time
        Then:  quantity of product on quick view should be equals 3
        """
        index_page.show_quick_view()
        index_page.quick_view.increase_quantity(num=2)
        assert index_page.quick_view.quantity == 3

    @pytest.mark.quick_view
    @pytest.mark.parametrize(
        'value, size', [('2', 'M'), ('3', 'L')]
    )
    def test_quick_view_change_size(self, index_page, value: str, size: str):
        """
        Given: index page loaded
        When:  moving to product card and clicking on `quick view` button
        And:   changing size of product by selecting needed value in select box
        Then:  size of product on quick view should not be equals product size
               before changing it
        And:   size on quick view should be equals to selected size in
               select box
        """
        index_page.show_quick_view()
        size_before = index_page.quick_view.size
        index_page.quick_view.change_size(value)
        assert not size_before == index_page.quick_view.size
        assert index_page.quick_view.size == size
