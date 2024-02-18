# Тестовое задание по автоматизации тестирования негативных сценариев полей ввода на странице регистрации сайта https://koshelek.ru/

Примечание. Тесты не могут быть запущены без ошибок, т.к. на сайте не функционируют локаторы для полей ввода на странице регистрации.
Чтобы в будущем тесты успешно заработали, нужно в файле koshelek.py заменить локаторы на исправные и в файле test_negative_registration.py
в явных ожиданиях WebDriverWait тоже заменить содержимое локатора. Обычное открытие страницы сайта без взаимодействия с элементами страницы происходит
исправно после запуска автотеста.

При проектировании автоматизированных тестов были применены фреймворки Pytest, Selenium и паттерн PageObject.

При тестировании сайта были применены следующие техники тест-дизайна:
- разбиение на классы эквивалентности;
- анализ граничных значений.
Данные техники применялись для полей ввода данных при тестировании негативных сценариев.

Папка pages содержит следующие файлы:

- elements.py - функции для взаимодействия с элементами страницы сайта при проведении автотестов;
- base.py - функции для получения главной страницы сайта и пути текущей страницы;
- koshelek.py - функции для взаимодействия с url страницы и локаторы для элементов сайта;
- settings.py - учетные данные, используемые в процессе теста.

Папка tests содержит:

- test_negative_registration.py - негативные тесты страницы регистрации.

Также проект содержит такие файлы, как:

- conftest.py - фикстуры для работы с браузером;
- .env - валидные данные для регистрации на сайте;
- requirements.txt - используемые при тестировании библиотеки PyCharm.

Для подготовки к запуску автотестов необходимо установить необходимые библиотеки PyCharm с помощью вводимой команды в консоли терминала:

       pip install -r requirements.txt

Также необходимо скачать актуальную версию драйвера для вашего браузера для успешного прохождения тестов.

Для запуска автотестов необходимо вводить команды в консоли терминала.

1. Для поля ввода "Имя пользователя":

       python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\test_negative_registration.py -k test_registration_invalid_username

2. Для поля ввода "Электронная почта":

       python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\test_negative_registration.py -k test_registration_invalid_email

3. Для поля ввода "Пароль":

       python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\test_negative_registration.py -k test_registration_invalid_password
   
4. Для поля ввода "Реферальный код":

       python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\test_negative_registration.py -k test_registration_invalid_ref_code

<chromedriver_directory>\<chromedriver_file> - путь к директории файла драйвера\название файла браузера. Например: C:\Chrome-selenium\chromedriver.exe

Окружение: Google Chrome Версия 121, Windows 11 Home (64 бит)
