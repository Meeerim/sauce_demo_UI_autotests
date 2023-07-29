from selene import browser, have, command


class MainJobsPage:
    def verify_main_page(self):
        browser.should(have.url_containing('/inventory.html'))
        return self

    def open_homepage(self):
        browser.open('/inventory.html')
        return self

    def filter_by_price(self):
        browser.element("//select[@class='product_sort_container']/option[@value='lohi']").click()
        return self

    def add_to_cart_two_cheapest_products(self):
        browser.element('#add-to-cart-sauce-labs-onesie').click()
        browser.element('#add-to-cart-sauce-labs-bike-light').click()
        return self

    def add_one_product(self):
        browser.element('#add-to-cart-sauce-labs-bike-light').click()
        return self
