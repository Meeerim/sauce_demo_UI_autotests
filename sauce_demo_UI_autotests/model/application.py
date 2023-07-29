from selene import browser

from sauce_demo_UI_autotests.model.pages.cart_page import CartPage
from sauce_demo_UI_autotests.model.pages.checkout_page import CheckoutPage
from sauce_demo_UI_autotests.model.pages.login_page import LogInPage
from sauce_demo_UI_autotests.model.pages.main_page import MainJobsPage


class Application:
    def __init__(self):

        self.user_log_in = LogInPage()
        self.main_page = MainJobsPage()
        self.cart_page = CartPage()
        self.checkout_page = CheckoutPage()

    def open(self):
        browser.open('/')
        return self


app = Application()
