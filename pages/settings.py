import os
from dotenv import load_dotenv
import string
load_dotenv()


"""Валидные данные для регистрации в системе"""
valid_email = os.getenv('email')
valid_name = os.getenv('username')
valid_password = os.getenv('password')
valid_ref_code = os.getenv('ref_code')


"""Невалидные данные для регистрации в системе."""
invalid_mail_1 = ''
invalid_mail_2 = '@'
invalid_mail_3 = '@.'
invalid_mail_4 = 'b2cb4a217it@'
invalid_mail_5 = '@laafd.com'
invalid_mail_6 = 'b2cb4a217it@laafd.'
invalid_mail_7 = 'b2cb4a217it@laafdcom'
invalid_mail_8 = 'b2cb4a217it@laafd.77'
invalid_mail_9 = '.'

invalid_username = '123456789'


def generate_string_rus(n):
    return 'б' * n


def generate_string_en(n):
    return 'x' * n


def english_chars():
    return 'qwertyuiopasdfghjklzxcvbnm'


def russian_chars():
    return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'


def chinese_chars():    # 20 популярных китайских иероглифов
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return f'{string.punctuation}'
