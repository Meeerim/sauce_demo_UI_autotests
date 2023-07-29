from selene import browser, have, be
from selene.support.jquery_style_selectors import s


class CartPage:
    def open(self):
        browser.open('/cart.html')
        return self

    def verify_products_added(self):
        browser.all('//a[@id="item_2_title_link"]/div[@class="inventory_item_name"]').should(have.texts("Sauce Labs Onesie"))
        browser.all('//a[@id="item_0_title_link"]/div[@class="inventory_item_name"]').should(have.texts('Sauce Labs Bike Light'))
        return self

    def verify_cart_page_has_two_cart_items(self):
        cart_items = browser.all('.cart_item')
        assert len(cart_items) == 2, f"Expected 2 cart items, but found {len(cart_items)}"
        return self

    def remove_first_product(self):
        browser.element('#remove-sauce-labs-onesie').click()
        return self

    def verify_only_one_product_left(self):
        cart_items = browser.all('.cart_item')
        assert len(cart_items) == 1, f"Expected 2 cart items, but found {len(cart_items)}"
        return self

    def enter_checkout_button(self):
        browser.element('#checkout').click()
        return self

    def verify_checkout_page(self):
        browser.should(have.url_containing('/checkout-step-one.html'))
        return self
