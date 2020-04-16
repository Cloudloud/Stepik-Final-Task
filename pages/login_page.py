from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print(self.browser.current_url)
        assert "login" in self.browser.current_url, "ожидался другой url страницы"

        # реализуйте проверку на корректный url адрес

        assert True

    def should_be_login_form(self):
        login_form_email_input=self.is_element_present(*LoginPageLocators.LOGIN_FORM_USERNAME_INPUT)
        login_form_pass_input=self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASSWORD_INPUT)
        login_form_submit_btn=self.is_element_present(*LoginPageLocators.LOGIN_FORM_SUBMIT_BUTTON)
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        reg_form_email_input=self.is_element_present(*LoginPageLocators.REGISTER_FORM_EMAIL_INPUT)
        reg_form_pass_input=self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASSWORD_INPUT)
        reg_form_confirm_pass_input=self.is_element_present(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD_INPUT)
        reg_form_submit_btn=self.is_element_present(*LoginPageLocators.REGISTER_FORM_SUBMIT_BUTTON)

        assert True