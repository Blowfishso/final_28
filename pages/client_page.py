from pages.base_page import BasePage
from locators import ClientPageLocators


class ClientPage(BasePage):
    def check_avatar(self):
        avatar = self.find_element(ClientPageLocators.LOCATOR_USER_AVATAR)
        return avatar

    def log_out(self):
        self.find_element(ClientPageLocators.LOCATOR_LOGOUT_BUTTON).click()