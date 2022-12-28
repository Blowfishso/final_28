from selenium.webdriver.common.by import By


class AuthPageLocators:
    LOCATOR_EMAIL_FIELD = (By.ID, 'username')
    LOCATOR_PASSWORD_FIELD = (By.ID, 'password')
    LOCATOR_LOG_IN_BUTTON = (By.ID, 'kc-login')
    LOCATOR_AUTH_FORM_HEADER = (By.CLASS_NAME, 'card-container__title')
    LOCATOR_ERROR_MESSAGE = (By.ID, 'form-error-message')
    LOCATOR_FORGOT_PASSWORD = (By.ID, 'forgot_password')
    LOCATOR_FORGOT_PASSWORD_HEADER = (By.XPATH, "//h1[contains(text(),'Восстановление пароля')]")
    LOCATOR_CAPTCHA_IMAGE = (By.CLASS_NAME, 'rt-captcha__image-con')
    LOCATOR_CAPTCHA_FILED = (By.ID, 'captcha')
    LOCATOR_GO_BACK_BUTTON = (By.ID, 'reset-back')
    LOCATOR_USER_AGREEMENT_LINK = (By.LINK_TEXT, 'пользовательского соглашения')
    LOCATOR_REGISTER_NEW_USER_LINK = (By.ID, 'kc-register')
    LOCATOR_VK_AUTH = (By.ID, 'oidc_vk')
    LOCATOR_OK_AUTH = (By.ID, 'oidc_ok')
    LOCATOR_MAILRU_AUTH = (By.ID, 'oidc_mail')
    LOCATOR_GOOGLE_AUTH = (By.ID, 'oidc_google')
    LOCATOR_YANDEX_AUTH = (By.ID, 'oidc_ya')


class ClientPageLocators:
    LOCATOR_USER_AVATAR = (By.CLASS_NAME, 'user-avatar')
    LOCATOR_LOGOUT_BUTTON = (By.ID, 'logout-btn')

class RegPageLocators:
    LOCATOR_FIRSTNAME_FIELD = (By.NAME, 'firstName')
    LOCATOR_LASTNAME_FIELD = (By.NAME, 'lastName')
    LOCATOR_REGION_FIELD = (By.XPATH, "//span[contains(text(),'Регион')]")
    LOCATOR_NUMBER_EMAIL_FIELD = (By.ID, 'address')
    LOCATOR_PASSWORD_FIELD = (By.ID, 'password')
    LOCATOR_CONFIRM_PASSWORD_FIELD = (By.ID, 'password-confirm')
    LOCATOR_REGISTER_BUTTON = (By.NAME, 'register')
    LOCATOR_REGISTER_HEADER = (By.XPATH, "//h1[contains(text(),'Регистрация')]")
    LOCATOR_FIRSTNAME_ERROR = (By.XPATH, "//div[1]/span[contains(text(),'кириллицей. От 2 до 30 символов')]")
    LOCATOR_LASTNAME_ERROR = (By.XPATH, "//div[2]/span[contains(text(),'кириллицей. От 2 до 30 символов')]")
    LOCATOR_NUMBER_EMAIL_ERROR = (By.XPATH, "//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ')]")
    LOCATOR_REGISTER_CODE_1 = (By.XPATH, "//input[@id='rt-code-0']")
    LOCATOR_REGISTER_CODE_2 = (By.XPATH, "//input[@id='rt-code-1']")
    LOCATOR_REGISTER_CODE_3 = (By.XPATH, "//input[@id='rt-code-2']")
    LOCATOR_REGISTER_CODE_4 = (By.XPATH, "//input[@id='rt-code-3']")
    LOCATOR_REGISTER_CODE_5 = (By.XPATH, "//input[@id='rt-code-4']")
    LOCATOR_REGISTER_CODE_6 = (By.XPATH, "//input[@id='rt-code-5']")






