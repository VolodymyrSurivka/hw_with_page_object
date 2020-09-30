from .base_page import BasePage
from .locators import BackOfficeLoginPageLocators
import time


class LoginPage(BasePage):

    def login_in_bo(self, login, password):
        form_login_field = self.browser.find_element(*BackOfficeLoginPageLocators.USER_LOGIN)
        form_login_field.send_keys(login)
        form_password_field = self.browser.find_element(*BackOfficeLoginPageLocators.USER_PASSWORD)
        form_password_field.send_keys(password)
        sign_in_button = self.browser.find_element(*BackOfficeLoginPageLocators.SIGN_IN_BUTTON)
        sign_in_button.click()
        time.sleep(1)
