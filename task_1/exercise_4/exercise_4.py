import copy

"""
№ 1 Глубокое и поверхностное копирование
Напишите функцию, которая демонстрирует различие между неглубоким (shallow) и глубоким (deep) копированием сложных объектов в Python.
Для этого вам нужно:
Создать двумерный список original, содержащий два вложенных списка 1,2,3 и 4,5,6.
Использовать встроенные модули для создания неглубокой и глубокой копии этого списка.
Изменить самый первый элемент вложенного списка на 99.
вернуть результат shallow и deep_copy
"""

def copy_comparison():
    original = [[1,2,3],[4,5,6]]
    copy_orig = copy.copy(original)
    deep_orig = copy.deepcopy(original)
    original[0][0] = 99
    return copy_orig, deep_orig


"""
№ 2 Изменение элементов в списке и попытка изменения элементов в кортеже
Объявить список длиной 3 и кортеж длиной 3.
В первом списке изменить первый элемент на 99.
В кортеже попытаться присвоить первому элементу тоже 99, но предусмотреть исключение TypeError.
Вернуть список, кортеж и ошибку для присвоения значения в кортеже.
"""

def modify_elements():
    lst = list(range(1,4))
    tpl = tuple(range(1,4))
    lst[0] = 99
    try:
        tpl[0] = 99
    except TypeError as ex:
        return lst, tpl, str(ex)[15:]
    return 0



"""
№ 3 Создание списка кортежей с помощью zip и enumerate
"""

def create_tuples(list1: list, list2: list) -> list:
    lst = []
    # tupl = zip(list1,list2)
    #очень интересно что после принта tupl пропадает
    # print(list(tupl))
    # print(tupl)
    for i, (l1,l2) in enumerate(zip(list1,list2)):
         lst.append((i , l1, l2))
    return lst


"""
№ 4 Вычисление факториала с помощью обычной функции и генератора
"""

# Обычная функция
def factorial(n: int) -> int:
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)

# Генератор
def factorial_generator(n: int): # использовать yield
    f = 1
    if n == 1:
        yield 1
    else:
        for i in range(2, n+1):
            f *= i
            yield f

"""
№ 5 Определение принадлежности пакета через код
"""
# Заполнить одним из значений library/framework/module/unknown
packages = {
    "numpy": "library",
    "pandas": "library",
    "django": "framework",
    "flask": "framework",
    "math": "module",
    "itertools": "module",
}

# на вход название модуля/библиотеки/фреймворка
def classify_package(pkg_name: str) -> str:
    packages = {
        "numpy": "library",
        "pandas": "library",
        "django": "framework",
        "flask": "framework",
        "math": "module",
        "itertools": "module",
    }
    try:
        ans = packages[pkg_name]
    except KeyError as e:
        ans = "unknown"

    return ans

print(classify_package("numpy"))
print(classify_package("adas"))

"""
№ 6 Реализация классов с динамическим полиморфизмом и данных скрытием

Реализовать метод do_work в классе Programmer который возвращает строку `Writing code`
Реализовать метод do_work в классе Designer который возвращает строку `Designing interface`
"""


# Полиморфизм через метод do_work()
class Worker:
    def do_work(self):
        raise NotImplementedError


class Programmer(Worker):
    def do_work(self):
        return 'Writing code'


class Designer(Worker):
    def do_work(self):
        return 'Designing interface'


"""
# Инкапсуляция: скрытие реализации с использованием методов доступа
# При инициализации оъекта класса PrivateAccount объявить приватный атрибут balance
# Реализовать метод get_balance возвращающий приватный атрибут текущего баланса
# Реализовать метод deposit с возможностью внесения у казанной суммы условной единицы
"""
class PrivateAccount:
    def __init__(self,balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, dep):
        if dep > 0:
            self.__balance += dep


