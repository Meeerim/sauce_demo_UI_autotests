import allure

from sauce_demo_UI_autotests.model.application import app


@allure.tag("web")
@allure.feature(f'Add Product to Cart')
@allure.story("Verify that users can add items to the cart and the cart updates accordingly.")
def test_add_product_to_cart(login):
    with allure.step("From main page find the cheapest items and  to the cart"):
        app.main_page.open_homepage().\
            filter_by_price().\
            add_to_cart_two_cheapest_products()
    with allure.step("Verify that the number of items in the cart has increased by one"):
        app.cart_page.open().\
            verify_products_added()



@allure.tag("web")
@allure.feature(f'Remove Item from Cart')
@allure.story("Verify that users can remove items from the cart and the cart updates accordingly.")
def test_remove_product_from_cart(login,add_products_to_cart):
    with allure.step("Go to Cart Page and check the current number of items in the cart."):
        app.cart_page.open().\
            verify_cart_page_has_two_cart_items()
    with allure.step('Remove an item from the cart and verify that the number of items in the cart has decreased by '
                     'one.'):
        app.cart_page.remove_first_product().\
            verify_only_one_product_left()


@allure.tag("web")
@allure.feature(f'Cart checkout')
@allure.story('Verify that users can proceed to the checkout page from the cart page.')
def test_cart_checkout(login):
    with allure.step('Click on the "Proceed to Checkout" button.'):
        app.cart_page.open().\
            enter_checkout_button()
    with allure.step('Verify that the user is redirected to the checkout page.'):
        app.cart_page.verify_checkout_page()

