from selenium.webdriver.common.by import By


class ProductCardLocators:
    BUTTON_CONTAINER = './/div[@class="button-container"]'
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
    QUICK_VIEW = (By.CLASS_NAME, 'fancybox-iframe')


class ShoppingCartLocators:
    EMPTY_CART = (By.CLASS_NAME, 'ajax_cart_no_product')
    CART_QUANTITY = (
        By.XPATH, './/span[@class="ajax_cart_quantity unvisible"]'
    )
    CART_LINK = (By.XPATH, './/a[@title="View my shopping cart"]')
    CONTENT = (By.XPATH, './/div[@class="cart_block block exclusive"]')
    PRODUCTS = (By.XPATH, './/dl[@class="products"]/dt')
    PRODUCT_REMOVE = (
        By.XPATH,
        './/a[@class="ajax_cart_block_remove_link"]'
    )
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
    BUTTON_CONTAINER = './/div[@class="button-container"]'
    CONTINUE_BUTTON = (
        By.XPATH,
        f'{BUTTON_CONTAINER}/span[@title="Continue shopping"]'
    )
    CHECKOUT_BUTTON = (
        By.XPATH,
        f'{BUTTON_CONTAINER}/a[@title="Proceed to checkout"]'
    )


class QuickViewLocators:
    PRICE = (By.ID, 'our_price_display')
    QUANTITY_INPUT = (By.ID, 'quantity_wanted')
    PLUS_BUTTON = (By.XPATH, '//i[@class="icon-plus"]')
    MINUS_BUTTON = (By.XPATH, '//i[@class="icion-minus"]')
    SIZE_SELECT = (By.ID, 'group_1')
