from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуем проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Substring 'login' is not presented"

    def should_be_login_form(self):
        # реализуем проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login form is not presented"

    def should_be_register_form(self):
        # реализуем проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_REG_EMAIL), "Registration form is not presented"
