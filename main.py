import time

import requests

python_course = {'Введение': (1312, '/courses/python-basics/lessons/intro'),
                 'Hello, World!': (
                     2185, '/courses/python-basics/lessons/hello-world'),
                 'Инструкции': (
                     2186, '/courses/python-basics/lessons/instructions'),
                 'Арифметические операции': (
                     2187, '/courses/python-basics/lessons/arithmetics'),
                 'Ошибки оформления — синтаксис и линтер': (
                     2191, '/courses/python-basics/lessons/linting'),
                 'Строки': (2192, '/courses/python-basics/lessons/strings'),
                 'Переменные': (
                     2246, '/courses/python-basics/lessons/variables'),
                 'Выражения в определениях': (
                     2417,
                     '/courses/python-basics/lessons/variables-expression'),
                 'Именование': (2247, '/courses/python-basics/lessons/naming'),
                 'Интерполяция': (
                     2418, '/courses/python-basics/lessons/interpolation'),
                 'Извлечение символов из строки': (
                     2340, '/courses/python-basics/lessons/symbols'),
                 'Срезы строк': (
                     2419, '/courses/python-basics/lessons/slises'),
                 'Типы данных': (
                     2245, '/courses/python-basics/lessons/data-types'),
                 'Неизменяемость и примитивные типы': (2375,
                                                       '/courses/python-basics/lessons/immutability-of-primitive-types'),
                 'Функции и их вызов': (
                     2363, '/courses/python-basics/lessons/calling-functons'),
                 'Сигнатура функции': (
                     2373, '/courses/python-basics/lessons/signature'),
                 'Вызов функции — выражение': (
                     2374,
                     '/courses/python-basics/lessons/call-function-expression'),
                 'Детерминированность': (
                     2365, '/courses/python-basics/lessons/deterministic'),
                 'Стандартная библиотека': (
                     2376, '/courses/python-basics/lessons/stdlib'),
                 'Свойства и методы': (
                     2362, '/courses/python-basics/lessons/methods'),
                 'Цепочка методов': (
                     2421, '/courses/python-basics/lessons/methods-chain'),
                 'Определение функций': (
                     2368, '/courses/python-basics/lessons/functions-define'),
                 'Возврат значений': (
                     2369, '/courses/python-basics/lessons/functions-return'),
                 'Параметры функций': (
                     2370,
                     '/courses/python-basics/lessons/functions-arguments'),
                 'Необязательные параметры функций': (
                     2422,
                     '/courses/python-basics/lessons/default-parameters'),
                 'Именованные аргументы': (
                     2423, '/courses/python-basics/lessons/named-arguments'),
                 'Аннотации типов': (
                     3847, '/courses/python-basics/lessons/type-annotations'),
                 'Окружение': (
                     2372, '/courses/python-basics/lessons/environment'),
                 'Логика': (
                     2248,
                     '/courses/python-basics/lessons/logical-operations'),
                 'Логические операторы': (
                     2249, '/courses/python-basics/lessons/logical-operators'),
                 'Результат логических операций': (
                     2424,
                     '/courses/python-basics/lessons/logical-expressions'),
                 'Условные конструкции': (
                     2250, '/courses/python-basics/lessons/conditionals'),
                 'Оператор match': (
                     3657, '/courses/python-basics/lessons/match'),
                 'Цикл while': (2251, '/courses/python-basics/lessons/while'),
                 'Агрегация данных': (
                     2604, '/courses/python-basics/lessons/aggregation'),
                 'Обход строк': (
                     2603,
                     '/courses/python-basics/lessons/iteration-over-string'),
                 'Условия внутри тела цикла': (
                     2253,
                     '/courses/python-basics/lessons/conditions-inside-loops'),
                 'Цикл for': (2254, '/courses/python-basics/lessons/for'),
                 'Отладка': (1313, '/courses/python-basics/lessons/debug'),
                 'Модули': (1316, '/courses/python-basics/lessons/modules'),
                 'Модули поглубже': (
                     1315, '/courses/python-basics/lessons/modules-in-depth'),
                 'Пакеты': (1318, '/courses/python-basics/lessons/packages'),
                 'Модуль random': (
                     1341, '/courses/python-basics/lessons/module-random'),
                 'Кортежи': (1340, '/courses/python-basics/lessons/tuples'),
                 'История развития языка Python': (
                     1319, '/courses/python-basics/lessons/history')}
python_place_in_development_course = {'Введение': (
    4949, '/courses/python-development-overview/lessons/requirements'),
    'Программирование как профессия': (4950,
                                       '/courses/python-development-overview/lessons/about'),
    'Виды компаний и разработки': (4951,
                                   '/courses/python-development-overview/lessons/kinds'),
    'Написание кода': (4952,
                       '/courses/python-development-overview/lessons/coding'),
    'Неустаревающие знания': (4953,
                              '/courses/python-development-overview/lessons/knowledge')}
js_course = {'Введение': (2606, '/courses/js-basics/lessons/intro'),
             'Hello, World!': (2607, '/courses/js-basics/lessons/hello-world'),
             'Инструкции': (2609, '/courses/js-basics/lessons/instructions'),
             'Арифметические операции': (
                 2610, '/courses/js-basics/lessons/arithmetics'),
             'Ошибки оформления (синтаксиса и линтера)': (
                 2611, '/courses/js-basics/lessons/errors'),
             'Строки': (2612, '/courses/js-basics/lessons/strings'),
             'Переменные': (2613, '/courses/js-basics/lessons/variables'),
             'Выражения в определениях': (
                 2614, '/courses/js-basics/lessons/variables-expression'),
             'Именование': (2615, '/courses/js-basics/lessons/naming'),
             'Интерполяция': (
                 2616, '/courses/js-basics/lessons/interpolation'),
             'Извлечение символов из строки': (
                 2617, '/courses/js-basics/lessons/symbols'),
             'Типы данных': (2618, '/courses/js-basics/lessons/data-types'),
             'Неизменяемость и примитивные типы': (2619,
                                                   '/courses/js-basics/lessons/immutability-of-primitive-types'),
             'Функции и их вызов': (
                 2927, '/courses/js-basics/lessons/calling-functions'),
             'Сигнатура функции': (
                 2621, '/courses/js-basics/lessons/signature'),
             'Вызов функции — выражение': (
                 2622, '/courses/js-basics/lessons/call-function-expression'),
             'Функции с переменным числом параметров': (
                 2623, '/courses/js-basics/lessons/variadic-parameters'),
             'Детерминированность': (
                 2624, '/courses/js-basics/lessons/deterministic'),
             'Стандартная библиотека': (
                 2625, '/courses/js-basics/lessons/stdlib'),
             'Свойства и методы': (
                 2626, '/courses/js-basics/lessons/properties-methods'),
             'Цепочка вызовов': (
                 2627, '/courses/js-basics/lessons/methods-chain'),
             'Определение функций': (
                 2628, '/courses/js-basics/lessons/functions-define'),
             'Возврат значений': (
                 2629, '/courses/js-basics/lessons/functions-return'),
             'Параметры функций': (
                 2630, '/courses/js-basics/lessons/functions-parameters'),
             'Необязательные параметры функций': (
                 2631,
                 '/courses/js-basics/lessons/functions-default-parameters'),
             'Упрощенный синтаксис функций': (
                 2632, '/courses/js-basics/lessons/functions-short-syntax'),
             'Логика': (2633, '/courses/js-basics/lessons/logical-operations'),
             'Логические операторы': (
                 2634, '/courses/js-basics/lessons/logical-operators'),
             'Результат логических операций': (
                 2635, '/courses/js-basics/lessons/logical-expressions'),
             'Условные конструкции': (
                 2636, '/courses/js-basics/lessons/conditionals'),
             'Тернарный оператор': (
                 2637, '/courses/js-basics/lessons/ternary-operator'),
             'Конструкция Switch': (2638, '/courses/js-basics/lessons/switch'),
             'Цикл while': (2639, '/courses/js-basics/lessons/while'),
             'Агрегация данных': (
                 2640, '/courses/js-basics/lessons/aggregation'),
             'Обход строк в цикле': (
                 2641, '/courses/js-basics/lessons/iteration-over-strings'),
             'Условия внутри тела цикла': (
                 2642, '/courses/js-basics/lessons/conditions-inside-loops'),
             'Инкремент и декремент': (
                 2643, '/courses/js-basics/lessons/mutators'),
             'Цикл for': (2644, '/courses/js-basics/lessons/for'),
             'Модули': (2650, '/courses/js-basics/lessons/modules')}

authenticity_token = ''  # YOUR-TOKEN-HERE
cookie = ''  # YOUR-COOKIE-HERE

payload = f'_method=patch&authenticity_token={authenticity_token}'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36',
    'Cookie': cookie,
    'Content-Type': 'application/x-www-form-urlencoded'
}

DIR = 'https://ru.hexlet.io'


def first_open(url):
    return requests.request("GET", DIR + url + '/theory_unit', headers=headers,
                            data=payload).status_code


def finish_theory(url):
    return requests.request("POST", DIR + f'{url}/finish_unit?unit=theory',
                            headers=headers, data=payload).status_code


def finish_quiz(url):
    return requests.request("POST", DIR + f'{url}/finish_unit?unit=quiz',
                            headers=headers, data=payload).status_code


def finish_exercize(id):
    url = f"https://ru.hexlet.io/api/lessons/{id}/finish_unit.json?unit=exercise"
    return requests.request("PUT", url, headers=headers,
                            data=payload).status_code


def run_function(function, param, time_to_wait=30):
    status_code = function(param)
    if status_code == 429:
        print(
            f'Hexlet ругается на слишком большое количество запросов. Подождём {time_to_wait} секунд, может поможет')
        time.sleep(time_to_wait)
        print('Подождали... Попробуем ещё раз')
        run_function(function, param)
    if status_code >= 400:
        return 'Ошибка: Этот шаг был уже выполнен или произошла какая-то другая ошибка (код: ' + str(
            status_code) + ')'
    return f'Все хорошо (код: {status_code})'


def main():
    assert len(authenticity_token) != 0, 'Заполните поле "authenticity_token"'
    assert len(cookie) != 0, 'Заполните поле "cookie"'

    time_sleep = 0.5

    # меняем этот словарь, чтобы выбрать курс
    aim_course = python_place_in_development_course

    # меняем этот список, чтобы выбрать уроки
    aim_numbers = list(range(1, len(aim_course) + 1))

    c = 0
    start_from = 0
    for course in aim_course:
        c += 1
        if c < start_from:
            continue
        if c not in aim_numbers:
            continue
        print(
            f'----------------- #{c}  Выполняем урок "{course}"  -----------------')
        course_id, course_url = aim_course[course]
        print('Открываем...', run_function(first_open, course_url))
        time.sleep(time_sleep)
        print('Проходим теорию...', run_function(finish_theory, course_url))
        time.sleep(time_sleep)
        print('Проходим квиз...', run_function(finish_quiz, course_url))
        time.sleep(time_sleep)
        print('Проходим упражнение...',
              run_function(finish_exercize, course_id))
        time.sleep(time_sleep)


if __name__ == '__main__':
    main()
