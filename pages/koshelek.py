from pages.base import WebPage
from pages.elements import WebElement


class PageRegistration(WebPage):
    """Локаторы для страницы регистрации."""

    def __init__(self, web_driver, url=''):
        url = 'https://koshelek.ru/authorization/signup'
        super().__init__(web_driver, url)

    # Поле ввода имени пользователя
    input_username = WebElement(id='input-582')

    # Поле ввода электронной почты
    input_mail = WebElement(id='username')

    # Поле ввода пароля
    input_pass = WebElement(id='new-password')

    # Поле ввода реферального кода
    input_ref_code = WebElement(id='input-622')

    # Чекбокс для принятия пользовательского соглашения и политики конфиденциальности
    checkbox = WebElement(id='input-634')

    # Кнопка "Далее"
    btn_next = WebElement(xpath='//button[@type="submit"]')

    # Сообщение о неверно введенном имени пользователя
    error_name = WebElement(xpath='//span[contains(text(), "Поле не заполнено")]')

    # Сообщение о неверно введенной электронной почте
    error_email = WebElement(xpath='//span[contains(text(), "Поле не заполнено")]')

    # Сообщение о неверно введенном пароле
    error_pass = WebElement(xpath='//span[contains(text(), "Поле не заполнено")]')

    # Сообщение о неверно введенном реферальном коде
    error_code = WebElement(xpath='//span[contains(text(), "Поле не заполнено")]')
