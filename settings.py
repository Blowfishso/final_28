class TestData:
    valid_email = 'gibisa4765@randrai.com'
    valid_password = 'Gibisa4765'

    invalid_email = 'testemail7238@mail.ru'
    invalid_password = 'testpassword823'
    invalid_phone_number = '79587324426'

    wrong_name = ['S', 'Ы', 1, 11, '@', '@@', 'Ss', 31 * 'S', 31 * 'Ы']
    wrong_name_ids = ['single latin letter', 'single cyrillic letter', 'ome-digit number', 'two-digit number',
                      'single symbol', 'two symbols', '2 latin letters', '31 latin letters', '31 cyrillic letters']

    wrong_number_or_email = ["", 1, "+7974953121",  f"+7974{('8' * 20)}", "testemail@mail", "testemailmail.ru"]
    wrong_number_or_email_ids = ['empty string', 'one-digit number', 'short number', 'long Russian number',
                                 'email without country domain', 'email without @']

    password_less_than_8 = 'testabc'
    password_cyrillic_letters = 'тесттест'
    password_no_special_symbol_or_number = 'testabcd'
    password_no_capital_letters = 'testabcd$'
    password_more_than_20 = 21 * 't'

    wrong_password = ['哒哒哒哒哒哒哒哒Aa1', 'ダダダダダダダダAa1', '다다다다다다다다Aa1']
    wrong_password_ids = ['chinese characters', 'japanese characters', 'korean characters']

    password_chinese = '哒哒哒哒哒哒哒哒1Aa'

    password_1 = 'Testabcd$'
    password_2 = 'Testabcd%'

    first_name = 'Тест'
    last_name = 'Тест'
    email = 'test12332145@mail.ru'
    password = 'Testabcd$'