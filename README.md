# Python-HW4

Тут опишу инструкцию по тестам для всех issue_i сразу, чтобы несколько раз не описывать правильную работу в разных файлах. Для запуска нам понадобится терминал (можно встроенным, можно через Pycharm - он там тоже есть). Предполагаем, что файлы с тестами скачены. Далее нужно открыть терминал (пусть будет Pycharm). Также будем использовать тесты как с пробелами лишними, так и с числами, буквами и пункуацией (проверим по максимуму):

issue_1
1) Вводим команду python -m doctest -o NORMALIZE_WHITESPACE -v issue_1_test.py
2) Получаем результат


issue_2
1) Вводим команду python -m pytest -v issue_2_test.py
2) Получаем резы

issue_3
1) Вводим команду python -m unittest issue_3_test.py

issue_4
1) Вводим команду python -m pytest issue_4_test.py

issue_5
1) python -m pytest -q issue_5_test.py --cov=what_is_year_now - процент покрытия
2) python -m pytest -v -s issue_5_test.py - запуск самих тестов
3) python -m pytest --cov . --cov-report html - для оформления в html
