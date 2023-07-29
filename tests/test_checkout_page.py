import allure

from sauce_demo_UI_autotests.data.users import user
from sauce_demo_UI_autotests.model.application import app


@allure.tag("web")
@allure.feature(f'Successful Checkout with Valid User Information')
@allure.story('Verify that a user with valid information can successfully complete the checkout process and reach the '
              'order confirmation page.')
def test_successful_checkout(login):
    with allure.step('From main page choose any product and add to cart'):
        app.main_page.open_homepage(). \
            filter_by_price().\
            add_one_product()
    with allure.step('Navigate to the checkout page and fill in valid user information'):
        app.checkout_page.open().\
             fill_first_name(user.first_name).\
             fill_last_name(user.last_name).\
             fill_zip_code(user.zip_code).\
             go_to_second_part()
    with allure.step('Verify that url redirected to second part of checkout'):
        app.checkout_page.verify_url_redirected()
    with allure.step('Verify second part consist of payment and delivery information'):
        app.checkout_page.verify_payment_info().\
            verify_shipping_info().\
            verify_item_total_price_is_expected()
    with allure.step('Once checkout information confirmed to be expected, finish the checkout'):
        app.checkout_page.enter_finish_button()
    with allure.step('Verify successful completion of checkout'):
        app.checkout_page.verify_url_changed().\
            verify_expected_messages_shown()
    with allure.step('Click back home button and return to main page'):
        app.checkout_page.enter_back_home_button()
        app.main_page.verify_main_page()





