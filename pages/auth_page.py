from pages.base_page import BasePage
from locators import AuthPageLocators


class AuthPage(BasePage):
    def fill_fields_and_log_in(self, email, password):
        self.find_element(AuthPageLocators.LOCATOR_EMAIL_FIELD).send_keys(email)
        self.find_element(AuthPageLocators.LOCATOR_PASSWORD_FIELD).send_keys(password)
        self.find_element(AuthPageLocators.LOCATOR_LOG_IN_BUTTON).click()

    def check_auth_form_header(self):
        self.find_element(AuthPageLocators.LOCATOR_AUTH_FORM_HEADER)

    def check_error_message(self):
        self.find_element(AuthPageLocators.LOCATOR_ERROR_MESSAGE)

    def check_forgot_password(self):
        self.find_element(AuthPageLocators.LOCATOR_FORGOT_PASSWORD).click()
        self.find_element(AuthPageLocators.LOCATOR_FORGOT_PASSWORD_HEADER)
        self.find_element(AuthPageLocators.LOCATOR_EMAIL_FIELD)
        self.find_element(AuthPageLocators.LOCATOR_CAPTCHA_IMAGE)
        self.find_element(AuthPageLocators.LOCATOR_CAPTCHA_FILED)
        self.find_element(AuthPageLocators.LOCATOR_GO_BACK_BUTTON).click()

    def vk_auth(self):
        self.find_element(AuthPageLocators.LOCATOR_VK_AUTH).click()

    def ok_auth(self):
        self.driver.back()
        self.find_element(AuthPageLocators.LOCATOR_OK_AUTH).click()

    def mailru_auth(self):
        self.driver.back()
        self.find_element(AuthPageLocators.LOCATOR_MAILRU_AUTH).click()

    def google_auth(self):
        self.driver.back()
        self.find_element(AuthPageLocators.LOCATOR_GOOGLE_AUTH).click()

    def yandex_auth(self):
        self.driver.back()
        self.find_element(AuthPageLocators.LOCATOR_YANDEX_AUTH).click()

    def click_user_agreement_link(self):
        self.driver.back()
        self.find_element(AuthPageLocators.LOCATOR_USER_AGREEMENT_LINK).click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_register_new_user_link(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.find_element(AuthPageLocators.LOCATOR_REGISTER_NEW_USER_LINK).click()