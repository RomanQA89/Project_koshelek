import pytest
from pages.koshelek import PageRegistration
from pages.settings import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestNegativePageRegistration:
    """ Негативные тесты страницы регистрации сайта https://koshelek.ru/ """

    @pytest.mark.parametrize('username', ['', special_chars(), generate_string_rus(1), generate_string_en(1),
                                          generate_string_en(31), generate_string_en(32),
                                          generate_string_en(33), invalid_username, chinese_chars()],
                             ids=['empty', 'special_chars', '1_rus_chars', '1_en_char', '31_en_chars',
                                  '32_en_chars', '33_eng_chars', 'number', 'chinese_chars'])
    def test_registration_invalid_username(self, web_browser, username):
        """Проверка регистрации пользователей с невалидными именами."""

        page = PageRegistration(web_browser)

        page.input_username.send_keys(username)

        web_browser.implicitly_wait(10)

        page.input_mail.send_keys(valid_email)

        web_browser.implicitly_wait(10)

        page.input_pass.send_keys(valid_password)

        web_browser.implicitly_wait(10)

        page.input_ref_code.send_keys(valid_ref_code)

        web_browser.implicitly_wait(10)

        page.checkbox.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))

        page.btn_next.click()

        web_browser.implicitly_wait(10)

        assert page.error_name.get_text() == 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы' \
               or 'Имя пользователя уже занято' or 'Поле не заполнено'

    @pytest.mark.parametrize('email', [invalid_mail_1, invalid_mail_2, invalid_mail_3, invalid_mail_4,
                                       invalid_mail_5, invalid_mail_6, invalid_mail_7, invalid_mail_8,
                                       invalid_mail_9, f'{russian_chars()}@mail.ru', f'{chinese_chars()}@mail.ru'],
                             ids=['empty', 'invalid_email_2', 'invalid_email_3', 'invalid_email_4', 'invalid_email_5',
                                  'invalid_email_6', 'invalid_email_7', 'invalid_email_8', 'invalid_email_9',
                                  'russian_chars', 'chinese_chars'])
    def test_registration_invalid_email(self, web_browser, email):
        """Проверка регистрации пользователей с невалидными электронными почтами."""

        page = PageRegistration(web_browser)

        page.input_username.send_keys(valid_name)

        web_browser.implicitly_wait(10)

        page.input_mail.send_keys(email)

        web_browser.implicitly_wait(10)

        page.input_pass.send_keys(valid_password)

        web_browser.implicitly_wait(10)

        page.input_ref_code.send_keys(valid_ref_code)

        web_browser.implicitly_wait(10)

        page.checkbox.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))

        page.btn_next.click()

        web_browser.implicitly_wait(10)

        assert page.error_email.get_text() == 'Поле не заполнено' or 'Формат e-mail: somebody@somewhere.ru'

    @pytest.mark.parametrize('password', ['', special_chars(), generate_string_en(7), generate_string_en(8),
                                          generate_string_en(9), generate_string_en(63), generate_string_en(64),
                                          generate_string_en(65), chinese_chars(), russian_chars()],
                             ids=['empty', 'special_chars', '7_en_chars', '8_en_chars', '9_en_chars',
                                  '63_en_chars', '64_en_chars', '65_en_chars', 'chinese_chars', 'rus_chars'])
    def test_registration_invalid_password(self, web_browser, password):
        """Проверка регистрации пользователей с невалидными паролями."""

        page = PageRegistration(web_browser)

        page.input_username.send_keys(valid_name)

        web_browser.implicitly_wait(10)

        page.input_mail.send_keys(valid_email)

        web_browser.implicitly_wait(10)

        page.input_pass.send_keys(password)

        web_browser.implicitly_wait(10)

        page.input_ref_code.send_keys(valid_ref_code)

        web_browser.implicitly_wait(10)

        page.checkbox.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))

        page.btn_next.click()

        web_browser.implicitly_wait(10)

        assert page.error_pass.get_text() == 'Поле не заполнено' or 'Пароль должен содержать минимум 8 символов' or \
            'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры'

    @pytest.mark.parametrize('ref_code', ['', generate_string_en(3), generate_string_en(4),
                                          generate_string_en(5), generate_string_en(8), generate_string_en(9),
                                          generate_string_en(10)],
                             ids=['empty', '3_en_chars', '4_en_chars', '5_en_chars',
                                  '8_en_chars', '9_en_chars', '10_en_chars'])
    def test_registration_invalid_ref_code(self, web_browser, ref_code):
        """Проверка регистрации пользователей с невалидными реферальными кодами."""

        page = PageRegistration(web_browser)

        page.input_username.send_keys(valid_name)

        web_browser.implicitly_wait(10)

        page.input_mail.send_keys(valid_email)

        web_browser.implicitly_wait(10)

        page.input_pass.send_keys(valid_password)

        web_browser.implicitly_wait(10)

        page.input_ref_code.send_keys(ref_code)

        web_browser.implicitly_wait(10)

        page.checkbox.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))

        page.btn_next.click()

        web_browser.implicitly_wait(10)

        assert page.error_code.get_text() == 'Неверный формат ссылки'
