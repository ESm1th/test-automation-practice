import pytest

from pages.index import IndexPage


class TestIndexPage:

    @pytest.fixture
    def index_page(self, browser):
        index_page = IndexPage(browser)
        index_page.load()
        return index_page

    def test_add_product_to_cart(self, index_page):
        index_page.add_product_to_cart()
        assert index_page.shopping_cart.quantity == 1

    def test_layer_cart_data(self, index_page):
        product_card = index_page.product_card
        product_card.add_to_cart()
        layer_cart = index_page.layer_cart
        assert product_card.product_name == layer_cart.product_name
        assert product_card.product_price == layer_cart.product_price
        assert layer_cart.product_quantity == 1

    @pytest.mark.cart
    def test_check_empty_cart(self, index_page):
        assert index_page.shopping_cart.is_empty()
        assert index_page.shopping_cart.quantity == '(empty)'

    @pytest.mark.cart
    def test_check_cart_with_product(self, index_page):
        index_page.add_product_to_cart()
        assert not index_page.shopping_cart.is_empty()
        assert index_page.shopping_cart.products_quantity == 1

    @pytest.mark.cart
    def test_check_cart_dropdown_prices(self, index_page):
        index_page.add_product_to_cart()
        index_page.shopping_cart.show_content()

        product_price = index_page.product_card.product_price
        shipping_price = index_page.shopping_cart.shipping_price

        assert shipping_price == 2
        assert index_page.shopping_cart.total_price == (
            product_price + shipping_price
        )

    @pytest.mark.remove
    def test_remove_product_from_cart(self, index_page):
        index_page.add_product_to_cart()
        index_page.shopping_cart.show_content()
        index_page.shopping_cart.remove_product()
        assert index_page.shopping_cart.is_empty()

    @pytest.mark.quick_view
    def test_quick_view_displayed(self, index_page):
        index_page.show_quick_view()
        assert index_page.quick_view.is_displayed()

    @pytest.mark.quick_view
    def test_quick_view_add_quantity(self, index_page):
        index_page.show_quick_view()
        index_page.quick_view.increase_quantity(num=2)
        assert index_page.quick_view.quantity == 3

    @pytest.mark.quick_view
    def test_quick_view_change_size(self, index_page):
        index_page.show_quick_view()
        index_page.close_quick_view()
