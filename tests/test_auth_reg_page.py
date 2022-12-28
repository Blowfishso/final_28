import pytest
from settings import TestData
from pages.auth_page import AuthPage
from pages.client_page import ClientPage
from pages.reg_page import RegPage


def test_auth_page_smoke_test(browser):
    rostelecom_auth_page = AuthPage(browser)
    rostelecom_auth_page.go_to_site()
    rostelecom_auth_page.check_auth_form_header()


def test_login_valid_email_and_password(browser):
    rostelecom_auth_page = AuthPage(browser)
    rostelecom_client_page = ClientPage(browser)
    rostelecom_auth_page.fill_fields_and_log_in(email=TestData.valid_email, password=TestData.valid_password)
    rostelecom_client_page.check_avatar()


def test_negative_login_invalid_email_and_password(browser):
    rostelecom_auth_page = ClientPage(browser)
    rostelecom_auth_page.log_out()
    rostelecom_auth_page = AuthPage(browser)
    rostelecom_auth_page.fill_fields_and_log_in(email=TestData.invalid_email, password=TestData.invalid_password)
    rostelecom_auth_page.check_error_message()


def test_negative_login_invalid_phone_number_valid_password(browser):
    rostelecom_auth_page = AuthPage(browser)
    rostelecom_auth_page.fill_fields_and_log_in(email=TestData.invalid_phone_number, password=TestData.invalid_password)
    rostelecom_auth_page.check_error_message()


def test_forgot_password(browser):
    rostelecom_auth_page = AuthPage(browser)
    rostelecom_auth_page.check_forgot_password()


def test_vk_auth(browser):
    rostelecom_auth_page = AuthPage(browser)
    rostelecom_auth_page.vk_auth()
    assert 'oauth.vk.com' in rostelecom_auth_page.get_current_link()


def test_ok_auth(browser):
    rostelecom_auth_page = AuthPage(browser)
    rostelecom_auth_page.ok_auth()
    assert 'onnect.ok.ru' in rostelecom_auth_page.get_current_link()


def test_mailru_auth(browser):
    rostelecom_auth_page = AuthPage(browser)
    rostelecom_auth_page.mailru_auth()
    assert 'connect.mail.ru' in rostelecom_auth_page.get_current_link()


def test_google_auth(browser):
    rostelecom_auth_page = AuthPage(browser)
    rostelecom_auth_page.google_auth()
    assert 'accounts.google.com' in rostelecom_auth_page.get_current_link()


def test_yandex_auth(browser):
    rostelecom_auth_page = AuthPage(browser)
    rostelecom_auth_page.yandex_auth()
    assert 'passport.yandex.ru' in rostelecom_auth_page.get_current_link()


def test_user_agreement_link(browser):
    rostelecom_auth_page = AuthPage(browser)
    rostelecom_auth_page.click_user_agreement_link()
    assert 'agreement' in rostelecom_auth_page.get_current_link()


def test_register_new_user_link(browser):
    rostelecom_auth_page = AuthPage(browser)
    rostelecom_auth_page.check_register_new_user_link()
    assert 'registration' in rostelecom_auth_page.get_current_link()


@pytest.mark.parametrize("firstname", TestData.wrong_name, ids=TestData.wrong_name_ids)
def test_negative_register_firstname(browser, firstname):
    rostelecom_reg_page = RegPage(browser)
    rostelecom_reg_page.fill_firstname(firstname)


@pytest.mark.parametrize("lastname", TestData.wrong_name, ids=TestData.wrong_name_ids)
def test_negative_register_lastname(browser, lastname):
    rostelecom_reg_page = RegPage(browser)
    rostelecom_reg_page.fill_lastname(lastname)


@pytest.mark.parametrize("number_email", TestData.wrong_number_or_email, ids=TestData.wrong_number_or_email_ids)
def test_negative_register_number_email(browser, number_email):
    rostelecom_reg_page = RegPage(browser)
    rostelecom_reg_page.fill_number_email(number_email)


def test_negative_register_password_less_than_8(browser):
    rostelecom_reg_page = RegPage(browser)
    rostelecom_reg_page.fill_password(password=TestData.password_less_than_8)
    assert 'Длина пароля должна быть не менее 8 символов' in rostelecom_reg_page.get_page_source()


def test_negative_register_password_cyrillic_letters(browser):
    rostelecom_reg_page = RegPage(browser)
    rostelecom_reg_page.fill_password(password=TestData.password_cyrillic_letters)
    assert 'Пароль должен содержать только латинские буквы' in rostelecom_reg_page.get_page_source()


def test_negative_register_password_no_special_symbol_or_number(browser):
    rostelecom_reg_page = RegPage(browser)
    rostelecom_reg_page.fill_password(password=TestData.password_no_special_symbol_or_number)
    assert 'Пароль должен содержать хотя бы 1 спецсимвол' in rostelecom_reg_page.get_page_source()


def test_negative_register_password_no_capital_letters(browser):
    rostelecom_reg_page = RegPage(browser)
    rostelecom_reg_page.fill_password(password=TestData.password_no_capital_letters)
    assert 'Пароль должен содержать хотя бы одну заглавную букву' in rostelecom_reg_page.get_page_source()


def test_negative_register_password_more_than_20(browser):
    rostelecom_reg_page = RegPage(browser)
    rostelecom_reg_page.fill_password(password=TestData.password_more_than_20)
    assert 'Длина пароля должна быть не более 20 символов' in rostelecom_reg_page.get_page_source()


#   bug-001, bug-002, bug-003
@pytest.mark.parametrize('password', TestData.wrong_password, ids=TestData.wrong_password_ids)
def test_register_password(browser, password):
    rostelecom_reg_page = RegPage(browser)
    rostelecom_reg_page.fill_password(password)
    assert 'Пароль должен содержать только латинские буквы' in rostelecom_reg_page.get_page_source()


def test_negative_register_different_passwords(browser):
    rostelecom_reg_page = RegPage(browser)
    rostelecom_reg_page.fill_both_password_fields(password_1=TestData.password_1, password_2=TestData.password_2)
    assert 'Пароли не совпадают' in rostelecom_reg_page.get_page_source()


def test_register_new_user(browser):
    rostelecom_reg_page = RegPage(browser)
    rostelecom_reg_page.register_new_user(firstname=TestData.first_name, lastname=TestData.last_name,
                                          email=TestData.email, password=TestData.password)
    assert 'Подтверждение email' in rostelecom_reg_page.get_page_source()