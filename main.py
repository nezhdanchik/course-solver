import requests
import time
courses = {'Введение': (1312, '/courses/python-basics/lessons/intro'),
           'Hello, World!': (
           2185, '/courses/python-basics/lessons/hello-world'),
           'Инструкции': (2186, '/courses/python-basics/lessons/instructions'),
           'Арифметические операции': (
           2187, '/courses/python-basics/lessons/arithmetics'),
           'Ошибки оформления — синтаксис и линтер': (
           2191, '/courses/python-basics/lessons/linting'),
           'Строки': (2192, '/courses/python-basics/lessons/strings'),
           'Переменные': (2246, '/courses/python-basics/lessons/variables'),
           'Выражения в определениях': (
           2417, '/courses/python-basics/lessons/variables-expression'),
           'Именование': (2247, '/courses/python-basics/lessons/naming'),
           'Интерполяция': (
           2418, '/courses/python-basics/lessons/interpolation'),
           'Извлечение символов из строки': (
           2340, '/courses/python-basics/lessons/symbols'),
           'Срезы строк': (2419, '/courses/python-basics/lessons/slises'),
           'Типы данных': (2245, '/courses/python-basics/lessons/data-types'),
           'Неизменяемость и примитивные типы': (2375,
                                                 '/courses/python-basics/lessons/immutability-of-primitive-types'),
           'Функции и их вызов': (
           2363, '/courses/python-basics/lessons/calling-functons'),
           'Сигнатура функции': (
           2373, '/courses/python-basics/lessons/signature'),
           'Вызов функции — выражение': (
           2374, '/courses/python-basics/lessons/call-function-expression'),
           'Детерминированность': (
           2365, '/courses/python-basics/lessons/deterministic'),
           'Стандартная библиотека': (
           2376, '/courses/python-basics/lessons/stdlib'),
           'Свойства и методы': (
           2362, '/courses/python-basics/lessons/methods'), 'Цепочка методов': (
    2421, '/courses/python-basics/lessons/methods-chain'),
           'Определение функций': (
           2368, '/courses/python-basics/lessons/functions-define'),
           'Возврат значений': (
           2369, '/courses/python-basics/lessons/functions-return'),
           'Параметры функций': (
           2370, '/courses/python-basics/lessons/functions-arguments'),
           'Необязательные параметры функций': (
           2422, '/courses/python-basics/lessons/default-parameters'),
           'Именованные аргументы': (
           2423, '/courses/python-basics/lessons/named-arguments'),
           'Аннотации типов': (
           3847, '/courses/python-basics/lessons/type-annotations'),
           'Окружение': (2372, '/courses/python-basics/lessons/environment'),
           'Логика': (
           2248, '/courses/python-basics/lessons/logical-operations'),
           'Логические операторы': (
           2249, '/courses/python-basics/lessons/logical-operators'),
           'Результат логических операций': (
           2424, '/courses/python-basics/lessons/logical-expressions'),
           'Условные конструкции': (
           2250, '/courses/python-basics/lessons/conditionals'),
           'Оператор match': (3657, '/courses/python-basics/lessons/match'),
           'Цикл while': (2251, '/courses/python-basics/lessons/while'),
           'Агрегация данных': (
           2604, '/courses/python-basics/lessons/aggregation'), 'Обход строк': (
    2603, '/courses/python-basics/lessons/iteration-over-string'),
           'Условия внутри тела цикла': (
           2253, '/courses/python-basics/lessons/conditions-inside-loops'),
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

authenticity_token = 'YOUR-TOKEN-HERE'
cookie = 'YOUR-COOKIE-HERE'

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

def evaluate_status_code(status_code):
    if status_code >= 400:
        return 'Ошибка: Этот шаг был уже выполнен или произошла какая-то другая ошибка (код: ' + str(status_code) + ')'
    return 'Все хорошо'
c = 0
time_sleep = 0.35
for course in courses:
    c += 1
    print(f'----------------- #{c}  Выполняем урок "{course}"  -----------------')
    course_id, course_url = courses[course]
    print('Открываем...', evaluate_status_code(first_open(course_url)))
    time.sleep(time_sleep)
    print('Проходим теорию...', evaluate_status_code(finish_theory(course_url)))
    time.sleep(time_sleep)
    print('Проходим квиз...', evaluate_status_code(finish_quiz(course_url)))
    time.sleep(time_sleep)
    print('Проходим упражнение...', evaluate_status_code(finish_exercize(course_id)))
    time.sleep(time_sleep)
