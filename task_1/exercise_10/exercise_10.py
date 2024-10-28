
"""
№ 1 Разработайте класс ComplexNumber, который представляет собой комплексное число
и поддерживает следующие операции:

Сложение: Реализуйте метод __add__, который позволяет складывать два комплексных числа. 
При сложении комплексных чисел (a + bi) и (c + di) результатом будет комплексное число (a + c) + (b + d)i.

Умножение: Реализуйте метод __mul__, который позволяет умножать два комплексных числа. 
При умножении комплексных чисел (a + bi) и (c + di) результатом будет комплексное число (ac - bd) + (ad + bc)i.

Модуль: Реализуйте метод __abs__, который возвращает модуль (или длину) комплексного числа. 
Модуль комплексного числа (a + bi) вычисляется как √(a^2 + b^2).

Сравнение на равенство: Реализуйте метод __eq__, который позволяет сравнивать два комплексных числа на равенство. 
Два комплексных числа равны, если их действительные и мнимые части равны.

Сравнение по модулю: Реализуйте метод __lt__, который позволяет сравнивать два комплексных числа по их модулю. 
Комплексное число меньше другого, если его модуль меньше модуля другого числа.

Представление: Реализуйте метод __repr__, который возвращает строковое представление комплексного числа в формате a + bi.

"""


class ComplexNumber:
    def __init__(self, re_num: int = 0, im_num: int = 0): 
        self.__re_num = re_num
        self.__im_num = im_num

    def get_re(self)-> int:
        return self.__re_num

    def get_im(self)-> int:
        return self.__im_num

    def __repr__(self)-> "ComplexNumber":
        return f"{self.get_re()} + {self.get_im()}i"

    def __add__(self, add_num: "ComplexNumber"):
        return ComplexNumber(self.get_re()+add_num.get_re(), self.get_im()+add_num.get_im())

    def __mul__(self, add_num: "ComplexNumber"):
        return ComplexNumber((self.get_re()*add_num.get_re())-(self.get_im()*add_num.get_im()), ((self.get_re()*add_num.get_im())+(self.get_im()*add_num.get_re())))
    
    def __abs__(self)->int:
        return (self.get_re()**2 + self.get_im()**2)**0.5

    def __eq__(self, compair_num: "ComplexNumber")-> bool:
        return (self.get_re() == compair_num.get_re()) and (self.get_im() == compair_num.get_im())

    def __lt__(self, compair_num: "ComplexNumber")-> bool:
        return True if (abs(self) < abs(compair_num)) else False
    

"""
№ 2 Реализация Менеджера Контекста для Управления Файлами с Логированием Ошибок

Реализовать класс FileManagerWithLogging, который будет использоваться как менеджер контекста для управления фTrайлами и логирования ошибок.

Конструктор __init__

Параметры:
filename: Имя файла для открытия.
mode: Режим открытия файла (например, 'r', 'w', 'a' и т.д.).
log_filename (по умолчанию "error_log.txt"): Имя файла для записи логов ошибок.
Инициализируйте атрибуты класса с переданными значениями.
Метод __enter__

Откройте файл с использованием переданных filename и mode.
Верните открытый файл для использования в блоке with.
Метод __exit__

При возникновении исключения:
Запишите сообщение об ошибке в файл лога (log_filename), используя формат: Error: <текст ошибки>.
Закройте файл, независимо от того, возникло ли исключение или нет.
"""


class FileManagerWithLogging:
   
    def __init__(self, filename: str, method: str = "r", log_file: str = "error_log.txt"):
        self.filename = filename
        self.log_file = log_file
        self.method = method
        self.file_obj = None


    def __enter__(self):
      
        try:
            self.file_obj = open(self.filename, self.method)
        except Exception as ex:
            self.logger(type(ex), ex)
            raise ex          
        return self.file_obj
        
    def __exit__(self, type_error, value, traceback):
        if self.file_obj is not None:
            self.file_obj.close()
        if type_error is not None:
            self.logger(type_error, value)
        
    def logger(self, type_error: str, value: str)-> None:
        try:
            self.error_log = open(self.log_file, "a")
            self.error_log.write(f"Error_type:{type_error} - Text: {value}\n")     
        finally:
            self.error_log.close()

# Пример использования
def write_to_file_with_logging(filename: str, content: str)-> None:
    with FileManagerWithLogging(filename, "w") as f:
        f.write(content)

"""
№ 3 Напишите функцию, которая создает замыкание для инкрементации значения.
Замыкание должно позволять динамически изменять шаг инкрементации,
сохраняя при этом текущее состояние. Кроме того, добавьте возможность сброса значения.
"""

def create_incrementer(start = 0):
    counter = start
    step = 1

    def closure(cmd: str = None, call_step: int = step)-> int:
        nonlocal counter, step
        counter += step

        if cmd == "reset":
            counter = 0
            return counter
        
        if cmd == "increment":
            step = call_step
            return counter
        
        
        return counter
    return closure


"""
№ 4 Создание асинхронного обработчика задач

Вам необходимо создать асинхронный обработчик задач с использованием модуля asyncio.
Напишите два асинхронных метода, которые реализуют следующую логику:

async_task(n): Этот метод принимает целое число n и выполняет следующее:

Если n четное, метод должен ожидать 1 секунду (используя await asyncio.sleep(1)) и вернуть строку вида "Task {n} completed".
Если n нечетное, метод должен возбуждать исключение ValueError с сообщением вида "Task {n} failed".
run_tasks(task_list): Этот метод принимает список целых чисел task_list и выполняет следующие действия:

Создает список асинхронных задач, вызывая async_task(n) для каждого числа n в task_list.
Обрабатывает каждую задачу с использованием вложенного асинхронного метода handle_task(n),
который вызывает async_task(n) и возвращает результат, или строку с описанием ошибки, если задача завершилась с исключением.
Сбор всех результатов и исключений в виде списка строк и возвращение этого списка.
"""

import asyncio


async def async_task(n: int)-> str:
    if n % 2 == 0:
       await asyncio.sleep(1)
       return (f"Task {n} completed") 
    else:
        raise ValueError(f"Task {n} failed")


async def run_tasks(task_list: list)-> list:
    async def handle_task(n):
        try:
            return await n
        except ValueError as e:
            return f"{e}"
        
    tasks = [asyncio.create_task(handle_task(async_task(n))) for n in task_list]
    results = [await n for n in tasks]
    return results
    

"""
№ 5 Поиск с валидацией

Вам необходимо реализовать два связанных метода для поиска элемента в отсортированном списке.

Метод binary_search(sorted_list, target)

Реализуйте функцию для выполнения бинарного поиска в отсортированном списке.
Эта функция должна принимать два аргумента:

sorted_list — отсортированный список элементов (список целых чисел).
target — элемент, который нужно найти.
Функция должна вернуть индекс target в sorted_list, если он присутствует в списке, и -1, если элемент не найден.

Метод search_with_validation(lst, target)

Реализуйте функцию, которая сначала проверяет, отсортирован ли список, и затем вызывает binary_search.
Эта функция должна принимать два аргумента:

lst — список целых чисел.
target — элемент, который нужно найти.
Если lst не отсортирован, функция должна возбуждать исключение ValueError с сообщением "List must be sorted".
В противном случае функция должна вызвать binary_search для выполнения поиска и вернуть результат.
"""


def binary_search(sorted_list: list, target: int)-> int:
    start = 0
    high = len(sorted_list) - 1
    mid = len(sorted_list) // 2

    while sorted_list[mid] != target and start <= high:
        if target > sorted_list[mid]:
            start = mid + 1
        else:
            high = mid - 1

        mid = (start + high) // 2
        
    if start > high:
        return -1
    else:
        return mid


def search_with_validation(lst: list, target: int):
    if lst != sorted(lst):
        raise ValueError("List must be sorted")
    return binary_search(lst, target)


"""
№ 6 Реализация Декоратора Кеширования и Повторов

Напишите декоратор cache_and_retry, который комбинирует два поведения:

Кеширование: Сохраняет результаты вызовов функции для уникальных наборов аргументов.
Если функция вызывается с теми же аргументами, кешированный результат возвращается немедленно, без повторного выполнения функции.
Повторные Попытки: Если функция вызывает исключение, повторите её выполнение несколько раз с заданной задержкой между попытками. 
Если после всех попыток функция всё ещё не выполняется успешно, исключение должно быть выброшено.
Детали
Декоратор cache_and_retry должен принимать два параметра:

retries: Количество попыток выполнить функцию (по умолчанию 3).
delay: Задержка между попытками в секундах (по умолчанию 1).
Декоратор должен использовать кеширование для хранения результатов вызовов функции. Кеширование должно быть реализовано с использованием словаря, где ключом является кортеж аргументов функции.

Декоратор должен работать следующим образом:

При первом вызове функции с определёнными аргументами, декоратор выполняет функцию и сохраняет результат в кеше.
При повторном вызове функции с теми же аргументами, декоратор возвращает результат из кеша.
Если функция вызывает исключение, декоратор делает попытку повторного выполнения до тех пор, пока не будет достигнуто максимальное количество попыток.
В случае успеха возвращается результат; в противном случае исключение выбрасывается.
"""

import functools
import time


def cache_and_retry(retries=3, delay=1):
    cache = {}

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = args + tuple(kwargs.values())
            result = 0
            rou = 0
            if key in cache.keys():
                return cache[key]
            else:
                while rou <= retries:
                    try:
                        result = func(*args, **kwargs)
                        cache[key] = result
                        return result
                    except Exception as e:
                        if rou < retries:
                            rou += 1
                            time.sleep(delay)
                            continue
                        else:
                            return e
                         
            return func(*args, **kwargs)
        return wrapper
    return decorator
