from selene import browser, have, be


class CheckoutPage():
    def open(self):
        browser.open('/checkout-step-one.html')
        return self

    def fill_first_name(self, first_name):
        browser.element('#first-name').type(first_name)
        return self

    def fill_last_name(self, last_name):
        browser.element('#last-name').type(last_name)
        return self

    def fill_zip_code(self, code):
        browser.element('#postal-code').type(code)
        return self

    def go_to_second_part(self):
        browser.element('#continue').click()
        return self

    def verify_url_redirected(self):
        browser.should(have.url_containing('/checkout-step-two.html'))
        return self

    def verify_payment_info(self):
        browser.element(
            "//div[contains(@class, 'summary_value_label') and contains(text(), 'SauceCard #31337')]").should(
            be.visible)
        return self

    def verify_shipping_info(self):
        browser.element(
            "//div[contains(@class, 'summary_value_label') and contains(text(), 'Free Pony Express Delivery!')]").should(
            be.visible)
        return self

    def verify_item_total_price_is_expected(self):
        browser.element('.summary_subtotal_label').should(have.texts('Item total: $9.99'))
        return self

    def enter_finish_button(self):
        browser.element('#finish').click()
        return self

    def verify_url_changed(self):
        browser.should(have.url_containing('/checkout-complete.html'))
        return self

    def verify_expected_messages_shown(self):
        browser.element('.complete-header').should(have.texts('Thank you for your order!'))
        browser.element('.complete-text').should(have.texts('Your order has been dispatched, and will arrive just as '
                                                            'fast as the pony can get there!'))
        return self

    def enter_back_home_button(self):
        browser.element('#back-to-products').click()
        return self


