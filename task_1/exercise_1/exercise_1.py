"""
№1 Реализуйте функцию process_data,
которая модифицирует входные данные в зависимости от их типа.
Функция должна обрабатывать вложенные структуры данных, такие как списки, словари и множества.
"""

# проверять, что значение data относится к определённому типу можно с помощью isinstance


def modify_nested_data(data):
    if isinstance(data, list):
        return [modify_nested_data(value) for value in data] + ["modified"]
    elif isinstance(data, dict):
        new_dct = {key: modify_nested_data(value) for key, value in data.items()}
        new_dct['new_key'] = 'new_value'
        return new_dct
    elif isinstance(data, set):
        data.add("new_element")
        return data
    else:
        return data


"""
№ 2 Реализуйте функцию reverse_with_depth,
которая выполняет реверсирование элементов в списках и кортежах на определенной глубине рекурсии.
Функция должна обрабатывать два входных параметра: список и кортеж,
а также параметр глубины, определяющий уровень рекурсии.
"""


def reverse_with_depth(lst, tpl, depth):
    def reverse_recursive(obj, d):
        if d == 0:
            return obj
        if isinstance(obj, list):
            return [reverse_recursive(value, d - 1) for value in obj][::-1]
        elif isinstance(obj, tuple):
            return tuple([reverse_recursive(value, d - 1) for value in obj][::-1])
        return obj

    return reverse_recursive(lst, depth), reverse_recursive(tpl, depth)


"""
№ 3 Напишите функцию pairwise_operations,
которая принимает два списка и операцию, которую нужно применить к
каждому соответствующему элементу (например, сложение, умножение и т. д.).
Она должна возвращать список результатов и индексы, по которым была выполнена операция.
Можно предположить, что оба списка имеют одинаковую длину.
"""


def pairwise_operations(lst1, lst2, operation):
    # решение в 1 строку используя list comprehension
    return [(i, operation(lst1[i], lst2[i])) for i in range(min(len(lst1), len(lst2)))]


"""
№ 4 Напишите три функции:

Процедура modify_external_state, которая принимает список и изменяет его на месте.
Функция compute_difference, возвращающая разность двух чисел.
Генератор infinite_sequence, который выдает последовательность, начиная с заданного числа start и до limit.
"""


def modify_external_state(lst: list):  # добавление строки "modified"
    lst.append("modified")


def compute_difference(a, b):
    return a - b


def infinite_sequence(start, limit):  # использование yield
    for i in range(start, limit + 1):
        yield i


"""
№ 5 Напишите функцию flexible_function,
которая принимает любое количество позиционных и ключевых аргументов,
суммирует позиционные аргументы и перемножает значения ключевых аргументов.
Верните сумму и произведение.
"""


def flexible_function(*args, **kwargs):
    multiplication = 1
    for value in kwargs.values():
        multiplication *= value
    return sum(args), multiplication


"""
№ 6 Объяснить разницу между модулем, фреймворком и библиотекой в
Markdown-документе, указав примеры использования в Python.
"""
