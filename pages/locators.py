from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM_USERNAME_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORM_SUBMIT_BUTTON = (By.NAME, "login_submit")

    REGISTER_FORM_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_FORM_SUBMIT_BUTTON = (By.NAME, "registration_submit")


