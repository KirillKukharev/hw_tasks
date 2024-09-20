import os
from abc import ABC, abstractmethod

"""
№ 1 Реализуйте класс SafeDict,
который расширяет функционал стандартного словаря Python, обеспечивая более безопасный доступ к ключам,
поддержку вложенных словарей и дополнительных операций.
Этот класс должен обладать следующими возможностями:
Инициализация:

Объект класса инициализируется с помощью обычного словаря.
Безопасный доступ к элементам:

При попытке получить элемент по ключу, который не существует в словаре, возвращается строка "Key not found".
Если ключом является список, возвращаются значения для всех ключей списка (если ключ не найден, возвращается сообщение "Key not found" для этого ключа).
Если значение по ключу — вложенный словарь, то возвращается новый объект SafeDict, который работает с вложенным словарем.
Добавление/изменение элементов:

Объект должен поддерживать добавление новых ключей и значений через синтаксис, аналогичный стандартному словарю.
Удаление элементов:

При удалении элемента по ключу, если ключ существует — он удаляется, иначе выводится сообщение об ошибке: "Key 'ключ' not found, nothing to delete."
Метод update:

Метод update обновляет значение по указанному ключу, если он существует. Если ключ не существует, выводится сообщение об ошибке: "Key 'ключ' not found, cannot update."

"""
class SafeDict:
    def __init__(self, initial_dict=None):
        if initial_dict is None:
            self._dict = {}
        elif isinstance(initial_dict, dict):
            self._dict = initial_dict
        else:
            raise TypeError("Initialization requires a dictionary.")

    def __getitem__(self, key):
        if isinstance(key, list):
            result = []
            for k in key:
                if k in self._dict:
                    value = self._dict[k]
                    if isinstance(value, dict):
                        value = SafeDict(value)
                    result.append(value)
                else:
                    result.append("Key not found")
            return result
        else:
            if key in self._dict:
                value = self._dict[key]
                if isinstance(value, dict):
                    return SafeDict(value)
                return value
            else:
                return "Key not found"

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __delitem__(self, key):
        if key in self._dict:
            del self._dict[key]
        else:
            print(f"Key '{key}' not found, nothing to delete.")

    def update(self, key, value):
        if key in self._dict:
            self._dict[key] = value
        else:
            print(f"Key '{key}' not found, cannot update.")

    def __repr__(self):
        return f"SafeDict({self._dict})"


"""
№ 2 Написание контекстного менеджера для временного изменения окружения

Напишите класс-контекстный менеджер TempEnvVar, который временно изменяет значение переменной окружения.
После выхода из контекста, переменная окружения возвращается к исходному значению.

Требования:
Класс TempEnvVar должен принимать два аргумента при инициализации:
var_name: имя переменной окружения.
value: новое значение переменной окружения.

При входе в контекст, значение переменной окружения должно быть временно заменено на указанное значение.
При выходе из контекста, переменная окружения должна восстановиться до исходного значения.
Если переменная окружения не существовала до входа в контекст, она должна быть удалена при выходе.
"""

# Контекстный менеджер
class TempEnvVar:
    def __init__(self, var_name, value):
        self.var_name = var_name
        self.new_value = value
        self.original_exists = False
        self.original_value = None

    def __enter__(self):
        if self.var_name in os.environ:
            self.original_exists = True
            self.original_value = os.environ[self.var_name]
        os.environ[self.var_name] = self.new_value

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.original_exists:
            os.environ[self.var_name] = self.original_value
        else:
            del os.environ[self.var_name]


"""
№ 3 Поиск максимального элемента в списке и кортеже

Создайте класс CustomCollection, который:

Инициализируется с коллекцией данных (список, кортеж или множество).
Имеет метод max_value(), который возвращает максимальное значение из коллекции, либо None, если коллекция пуста.
Корректно выводится в консоль с помощью метода __repr__ в виде строки `CustomCollection(коллекция)`.

Реализуйте функцию find_max_in_collections,
которая принимает словарь, где ключами являются строки (названия коллекций),
а значениями — коллекции данных (вложенные списки, кортежи, множества, словари, а также объекты класса CustomCollection).

Внутри функции find_max_in_collections напишите вспомогательную функцию get_max_value, которая:

Рекурсивно обходит переданные коллекции (включая вложенные), определяя максимальные значения на всех уровнях вложенности.
Умеет работать с типами list, tuple, set, dict и CustomCollection.
Для словарей максимальное значение ищется по значениям словаря.
Для объектов класса CustomCollection используется метод max_value().
Функция find_max_in_collections должна возвращать словарь,
где ключами являются имена коллекций (ключи исходного словаря),
а значениями — максимальные значения, найденные в соответствующих коллекциях.
"""


class CustomCollection:
    def __init__(self, data):
        if not isinstance(data, (list, tuple, set)):
            raise TypeError("CustomCollection must be initialized with a list, tuple, or set.")
        self.data = data

    def max_value(self):
        if not self.data:
            return None
        return max(self.data)

    def __repr__(self):
        return f"CustomCollection({self.data})"


def find_max_in_collections(collections):
    def get_max_value(collection):
        max_val = None
        if isinstance(collection, CustomCollection):
            max_val = collection.max_value()
        elif isinstance(collection, dict):
            for value in collection.values():
                candidate = get_max_value(value)
                if candidate is not None:
                    if (max_val is None) or (candidate > max_val):
                        max_val = candidate
        elif isinstance(collection, (list, tuple, set)):
            for item in collection:
                candidate = get_max_value(item)
                if candidate is not None:
                    if (max_val is None) or (candidate > max_val):
                        max_val = candidate
        else:
            try:
                if (max_val is None) or (collection > max_val):
                    max_val = collection
            except TypeError:
                pass  # Игнорировать несравнимые элементы
        return max_val

    result = {}
    for name, coll in collections.items():
        result[name] = get_max_value(coll)
    return result


"""
№ 4 Транспонирование матрицы с помощью zip

Реализуйте функцию transpose_matrix, которая принимает на вход матрицу (двумерный список) и возвращает её транспонированный вариант.

Транспонированная матрица — это новая матрица, в которой строки исходной матрицы становятся столбцами, а столбцы — строками.
"""


def transpose_matrix(matrix: list) -> list:
    return [list(row) for row in zip(*matrix)]

"""
№ 5 Поддержка аннотаций типов и их проверка

Реализуйте функцию с аннотациями типов,
которая проверяет соответствие переданных аргументов указанным типам.
"""


def annotated_function(a: int, b: str) -> bool:
    return isinstance(a, int) and isinstance(b, str) # решение в 1 строку


"""
№ 6 Демонстрация наследования через изменение поведения методов

Разработать базовый класс BaseAnimal,
от которого будут наследоваться конкретные классы животных,
такие как Dog и Cat.
Реализуйте методы для возвращения сообщений между животными.

Реализуйте абстрактный класс BaseAnimal с двумя абстрактными методами:
sound: возвращает звук, который издает животное.
communicate: определяет, как одно животное общается с другим.

Создайте класс Dog, который наследуется от BaseAnimal:

Метод sound должен возвращать строку "Woof".
Метод communicate должен возвращать разные строки в зависимости от того, с каким животным происходит общение:
Если это другой Dog, они должны `собака and другая собака bark together`.
Если это Cat, то `собака barks at кошку`
В остальных случаях, `собака doesn't know how to communicate with другие`.

Создайте класс Cat, аналогичный классу Dog, который:

Метод sound возвращает строку "Meow".
Метод communicate также возвращает разные строки в зависимости от того, с кем она взаимодействует:
Если это другой Cat, то "кошка and другая кошка purr together!".
Если это Dog, то "кошка hisses at собаку".
В остальных случаях `кошка doesn't know how to communicate with другими`
"""


# Класс с абстрактными методами
class BaseAnimal(ABC):
    @abstractmethod
    def sound(self) -> str:
        pass

    @abstractmethod
    def communicate(self, other: 'BaseAnimal') -> str:
        pass


# Класс Dog
class Dog(BaseAnimal):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    def sound(self) -> str:
        return "Woof"

    def communicate(self, other: BaseAnimal) -> str:
        if isinstance(other, Dog):
            return 'Buddy and Max bark together!'
        elif isinstance(other, Cat):
            return 'Buddy barks at Whiskers'
        else:
            raise AttributeError("собака doesn't know how to communicate with другие")


# Класс Cat
class Cat(BaseAnimal):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    def sound(self) -> str:
        return "Meow"

    def communicate(self, other: BaseAnimal) -> str:
        if isinstance(other, Cat):
            return 'Whiskers and Mittens purr together!'
        elif isinstance(other, Dog):
            return "Whiskers hisses at Buddy"
        else:
            return 'Whiskers and Mittens purr together!'


"""
№ 7 Реализация класса с магическими методами __len__ и __bool__

Реализуйте класс CustomCollection,
который представляет собой пользовательскую коллекцию элементов с поддержкой различных операций над ними.
Класс должен обладать следующими методами:

Конструктор класса принимает на вход список элементов items.
Если передан не список, должно быть выброшено исключение TypeError с сообщением `Items must be a list.`.

Определение длины коллекции:
Метод __len__ возвращает количество элементов в коллекции.

Проверка на пустоту:
Метод __bool__ возвращает True, если коллекция содержит хотя бы один элемент, и False, если коллекция пуста.

Добавление элемента:
Метод add(item) добавляет элемент item в коллекцию.

Удаление элемента:
Метод remove(item) удаляет элемент item из коллекции. Если элемент не найден, должно быть выброшено исключение ValueError с сообщением `объект not found in the collection.`.

Поиск элемента:
Метод find(predicate) возвращает первый элемент коллекции, который удовлетворяет условию, заданному функцией predicate. Если подходящего элемента нет, метод возвращает None.

Очистка коллекции:
Метод clear() очищает коллекцию, удаляя все элементы.

Поиск максимального элемента:
Метод max_value() возвращает максимальный элемент в коллекции. Если коллекция пуста, должно быть выброшено исключение ValueError с сообщением "CustomCollection is empty."
"""


class CustomCollection:
    def __init__(self, items):
        if not isinstance(items, list):
            raise TypeError("Items must be a list.")
        self.items = items

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return len(self.items) > 0

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        try:
            self.items.remove(item)
        except ValueError:
            raise ValueError("Object not found in the collection.")

    def find(self, predicate):
        for item in self.items:
            if predicate(item):
                return item
        return None

    def clear(self):
        self.items.clear()

    def max_value(self):
        if not self.items:
            raise ValueError("CustomCollection is empty.")
        return max(self.items)

    def __repr__(self):
        return f"CustomCollection({self.items})"
