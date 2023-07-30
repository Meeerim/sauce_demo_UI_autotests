from selene import browser, have


class LogInPage:
    def open(self):
        browser.open('/')
        return self

    def fill_username(self, username):
        browser.element('#user-name').type(username)
        return self

    def fill_password(self, password):
        browser.element('#password').type(password)
        return self

    def login_button(self):
        browser.element('#login-button').click()
        return self

    def check_expected_error_message(self):
        browser.element('.error-message-container.error').should(have.text('Epic sadface: Username and password do '
                                                                           'not match any user in this service'))
        return self
