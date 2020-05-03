from selenium.webdriver.common.by import By


class IndexPageLocators:
    PRODUCT_CARD = (By.CLASS_NAME, 'product-container')
    SHOPPING_CART = (By.XPATH, '//div[@class="shopping_cart"]')
    LAYER_CART = (By.ID, 'layer_cart')
