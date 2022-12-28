from pages.base_page import BasePage
from locators import RegPageLocators
from selenium.webdriver.common.keys import Keys


class RegPage(BasePage):
    def fill_firstname(self, firstname):
        self.find_element(RegPageLocators.LOCATOR_FIRSTNAME_FIELD).send_keys(firstname)
        self.find_element(RegPageLocators.LOCATOR_REGISTER_HEADER).click()
        self.find_element(RegPageLocators.LOCATOR_FIRSTNAME_ERROR)
        self.find_element(RegPageLocators.LOCATOR_FIRSTNAME_FIELD).send_keys(Keys.CONTROL + "a")

    def fill_lastname(self, lastname):
        self.find_element(RegPageLocators.LOCATOR_LASTNAME_FIELD).send_keys(lastname)
        self.find_element(RegPageLocators.LOCATOR_REGISTER_HEADER).click()
        self.find_element(RegPageLocators.LOCATOR_LASTNAME_ERROR)
        self.find_element(RegPageLocators.LOCATOR_LASTNAME_FIELD).send_keys(Keys.CONTROL + "a")

    def fill_number_email(self, number_email):
        self.find_element(RegPageLocators.LOCATOR_NUMBER_EMAIL_FIELD).send_keys(number_email)
        self.find_element(RegPageLocators.LOCATOR_REGISTER_BUTTON).click()
        self.find_element(RegPageLocators.LOCATOR_NUMBER_EMAIL_ERROR)
        self.find_element(RegPageLocators.LOCATOR_NUMBER_EMAIL_FIELD).send_keys(Keys.CONTROL + "a")

    def fill_password(self, password):
        self.find_element(RegPageLocators.LOCATOR_PASSWORD_FIELD).send_keys(password)
        self.find_element(RegPageLocators.LOCATOR_REGISTER_BUTTON).click()
        self.find_element(RegPageLocators.LOCATOR_PASSWORD_FIELD).send_keys(Keys.CONTROL + "a")

    def fill_both_password_fields(self, password_1, password_2):
        self.find_element(RegPageLocators.LOCATOR_PASSWORD_FIELD).send_keys(password_1)
        self.find_element(RegPageLocators.LOCATOR_CONFIRM_PASSWORD_FIELD).send_keys(password_2)
        self.find_element(RegPageLocators.LOCATOR_REGISTER_BUTTON).click()

    def register_new_user(self, firstname, lastname, email, password):
        self.find_element(RegPageLocators.LOCATOR_FIRSTNAME_FIELD).send_keys(Keys.CONTROL + "a")
        self.find_element(RegPageLocators.LOCATOR_FIRSTNAME_FIELD).send_keys(firstname)
        self.find_element(RegPageLocators.LOCATOR_LASTNAME_FIELD).send_keys(Keys.CONTROL + "a")
        self.find_element(RegPageLocators.LOCATOR_LASTNAME_FIELD).send_keys(lastname)
        self.find_element(RegPageLocators.LOCATOR_NUMBER_EMAIL_FIELD).send_keys(Keys.CONTROL + "a")
        self.find_element(RegPageLocators.LOCATOR_NUMBER_EMAIL_FIELD).send_keys(email)
        self.find_element(RegPageLocators.LOCATOR_PASSWORD_FIELD).send_keys(Keys.CONTROL + "a")
        self.find_element(RegPageLocators.LOCATOR_PASSWORD_FIELD).send_keys(password)
        self.find_element(RegPageLocators.LOCATOR_CONFIRM_PASSWORD_FIELD).send_keys(Keys.CONTROL + "a")
        self.find_element(RegPageLocators.LOCATOR_CONFIRM_PASSWORD_FIELD).send_keys(password)
        self.find_element(RegPageLocators.LOCATOR_REGISTER_BUTTON).click()
        self.find_element(RegPageLocators.LOCATOR_REGISTER_CODE_1)
        self.find_element(RegPageLocators.LOCATOR_REGISTER_CODE_2)
        self.find_element(RegPageLocators.LOCATOR_REGISTER_CODE_3)
        self.find_element(RegPageLocators.LOCATOR_REGISTER_CODE_4)
        self.find_element(RegPageLocators.LOCATOR_REGISTER_CODE_5)
        self.find_element(RegPageLocators.LOCATOR_REGISTER_CODE_6)