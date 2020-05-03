from selenium.webdriver.common.by import By


BUTTON_CONTAINER = './/div[@class="button-container"]'


class ProductCardLocators:
    ADD_TO_CART_BUTTON = (
        By.XPATH, f'{BUTTON_CONTAINER}/a[@title="Add to cart"]'
    )
    MORE_BUTTON = (
        By.XPATH, f'{BUTTON_CONTAINER}/a[@title="View"]'
    )
    QUICK_VIEW_BUTTON = (
        By.XPATH, './/a[@class="quick-view"]'
    )
    PRODUCT_NAME_LINK = (
        By.XPATH, './/a[@class="product-name"]'
    )
    PRODUCT_PRICE = (
        By.XPATH,
        './/div[@class="right-block"]//span[@class="price product-price"]'
    )


class ShoppingCartLocators:
    EMPTY_CART = (By.CLASS_NAME, 'ajax_cart_no_product')
    CART_QUANTITY = (
        By.XPATH, './/span[@class="ajax_cart_quantity unvisible"]'
    )
    PRODUCTS = (By.XPATH, './/dl[@class="products"]/dt')
    SHIPPING_PRICE = (
        By.XPATH,
        './/div[@class="cart-prices-line first-line"]/span'
    )
    TOTAL_PRICE = (
        By.XPATH,
        './/div[@class="cart-prices-line last-line"]/span'
    )


class LayerCartLocators:
    PRODUCT_TITLE = (By.ID, 'layer_cart_product_title')
    PRODUCT_QUANTITY = (By.ID, 'layer_cart_product_quantity')
    PRODUCT_PRICE = (By.ID, 'layer_cart_product_price')
    CONTINUE_BUTTON = (
        By.XPATH,
        f'{BUTTON_CONTAINER}/span[@title="Continue shopping"]'
    )
    CHECKOUT_BUTTON = (
        By.XPATH,
        f'{BUTTON_CONTAINER}/a[@title="Proceed to checkout"]'
    )
