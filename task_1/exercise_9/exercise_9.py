import time
import tracemalloc
from abc import ABC, abstractmethod

"""
№ 1 Написать класс, использующий наследование и полиморфизм. 

Создайте систему для управления поведением различных домашних животных,
используя принципы объектно-ориентированного программирования (ООП) и инкапсуляцию.
В этой системе вы должны определить абстрактный класс для животных, а затем создать конкретные реализации для собак, кошек и попугаев.
Каждое животное должно иметь возможность изменять своё настроение, уровень голода и усталости, а также взаимодействовать с игрушками.

Абстрактный класс Animal:

Создайте абстрактный класс Animal с полями для имени, настроения, голода и усталости.
Используйте инкапсуляцию с помощью свойства (property) для управления доступом к полям настроения, голода и усталости.
Определите абстрактный метод speak, который должен быть реализован в подклассах.
Реализуйте методы feed, rest и play, которые изменяют уровень голода и усталости, а также изменяют настроение и выводят сообщение о действиях.

Классы-потомки:

Создайте классы Dog, Cat и Parrot, наследующие от Animal.
Каждый класс должен реализовать метод speak, который возвращает строку в зависимости от уровня голода, усталости и настроения.

Класс Toy:

Реализуйте класс Toy, который будет представлять игрушку.
Игрушка должна иметь имя и булево значение, указывающее, является ли она интересной (fun).
"""


class Animal(ABC):
    def __init__(self, name, mood, hunger=None, tiredness=None):
        self._name = name
        self._mood = mood
        if hunger is not None:
            self._hunger = hunger
        else:
            self._hunger = None
        if hunger is not None:
            self._tiredness = tiredness
        else:
            self._tiredness = None

    @property
    def mood(self):
        return self._mood

    @mood.setter
    def mood(self, value):
        self._mood = value

    @property
    def hunger(self):
        return self._hunger

    @hunger.setter
    def hunger(self, value):
        if not 0 <= value <= 10:
            raise ValueError("0 <= hunger <= 10.")
        self._hunger = value

    @property
    def tiredness(self):
        return self._tiredness

    @tiredness.setter
    def tiredness(self, value):
        if not 0 <= value <= 10:
            raise ValueError("0 <= tiredness <= 10")
        self._tiredness = value

    @abstractmethod
    def speak(self):
        pass

    def feed(self):
        self.hunger = max(0, self.hunger - 3)
        self.update_mood()

    def rest(self):
        self.tiredness = max(0, self.tiredness - 3)
        self.update_mood()

    def play(self, toy):
        if toy.is_fun:
            self.mood = "happy"
        else:
            self.mood = "bored"
        self.tiredness = min(10, self.tiredness + 2)

    def update_mood(self):
        if self.hunger > 7 or self.tiredness > 7:
            self.mood = "irritated"
        elif self.hunger < 3 and self.tiredness < 3:
            self.mood = "happy"
        else:
            self.mood = "neutral"


class Dog(Animal):
    def speak(self):
        if self.hunger > 7:
            return "Woof! I'm hungry!"
        elif self.tiredness > 7:
            return "Woof! I'm tired!"
        elif self.mood == "happy":
            return "Woof! I'm happy!"
        return "Woof!"


class Cat(Animal):
    def speak(self):
        if self.hunger > 7:
            return "Meow! I'm hungry!"
        elif self.tiredness > 7:
            return "Meow! I'm tired!"
        elif self.mood == "happy":
            return "Meow! I'm happy!"
        return "Meow!"


class Parrot(Animal):
    def speak(self):
        if self.hunger > 7:
            return "Chirping! I'm hungry!"
        elif self.tiredness > 7:
            return "Chirping! I'm tired!"
        elif self.mood == "happy":
            return "Chirping! I'm happy!"
        return "Chirping!"


class Toy:
    def __init__(self, name, is_fun):
        self.name = name
        self.is_fun = is_fun


"""
№ 2 Написать класс с использованием магических методов (__str__, __len__, __getitem__).

для __len__ выводить длину объекта

для __str__ выводить `MyContainer with длина объекта items`

для __getitem__ выводить значение по индексу
"""


class MyContainer:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"MyContainer with {len(self.items)} items"

    def __getitem__(self, index):
        return self.items[index]


"""
№ 3 Реализация Менеджера Файлов

Напишите класс FileManager, который реализует интерфейс контекстного менеджера для работы с файлами.
Класс должен использовать методы __enter__ и __exit__ для открытия и закрытия файла.

Класс FileManager должен быть инициализирован с двумя параметрами:

filename (строка): Имя файла, с которым будет производиться работа.
mode (строка): Режим открытия файла (например, 'r' для чтения, 'w' для записи и т.д.).

При создании экземпляра класса FileManager файл не должен открываться немедленно.
Файл должен открываться только при входе в контекстный менеджер.

Метод __enter__ должен открывать файл с использованием переданного режима и возвращать объект файла.

Метод __exit__ должен закрывать файл при выходе из контекста.
Он должен принимать параметры, соответствующие стандартному интерфейсу метода __exit__,
но эти параметры не должны использоваться в реализации метода.
"""


class FileManager:

    _file = None

    def __init__(self, filename, mode):
        self._filename = filename
        self._mode = mode

    def __enter__(self):
        self._file = open(self._filename, self._mode)
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._file:
            self._file.close()


"""
№ 4 Напишите функцию, которая принимает два аргумента:

lst: Вложенный список (список, содержащий другие списки и/или элементы).
tpl: Вложенный кортеж (кортеж, содержащий другие кортежи и/или элементы).

Внутри функции:

Измерьте время выполнения операции изменения всех элементов во вложенном списке lst следующим образом:

Напишите внутреннюю рекурсивную функцию modify_list(l), которая изменяет все элементы вложенного списка l на строку "modified".
Если элемент сам является списком, рекурсивно вызывайте modify_list.
Запишите время выполнения этой операции.
Затем, измерьте время выполнения попытки изменения всех элементов во вложенном кортеже tpl следующим образом:

Напишите внутреннюю рекурсивную функцию modify_tuple(t), которая изменяет все элементы вложенного кортежа t на строку "modified".
Если элемент сам является кортежем, рекурсивно вызывайте modify_tuple.
Поскольку кортежи в Python неизменяемы, это должно вызвать исключение TypeError.
Функция должна возвращать кортеж, содержащий:

Изменённый список lst.
Сообщение об ошибке, возникшей при попытке изменения кортежа.
Время, затраченное на изменение списка.
Время, затраченное на попытку изменения кортежа.
"""


def modify_list(l):
    for i in range(len(l)):
        if isinstance(l[i], list):
            modify_list(l[i])
        else:
            l[i] = "modified"
    return l


def modify_tuple(t):
    for i in range(len(t)):
        if isinstance(t[i], tuple):
            modify_tuple(t[i])
        else:
            t[i] = "modified"


def list_tuple_operations_deep(lst, tpl):
    start_list = time.time()
    updated_lst = modify_list(lst)
    time.sleep(0.0001)
    end_list = time.time()
    list_time = end_list - start_list

    start_tuple = time.time()
    error_msg = ""
    try:
        modify_tuple(tpl)
    except TypeError as te:
        error_msg = str(te)
    time.sleep(0.0001)
    end_tuple = time.time()
    tuple_time = end_tuple - start_tuple

    return updated_lst, error_msg, list_time, tuple_time


"""
№ 5 Напишите функцию, которая принимает большое число n и возвращает квадраты всех чисел от 1 до n как с использованием списка,
так и с использованием генератора. Измерьте память с помощью tracemalloc.get_traced_memory(), занимаемую каждым подходом.
"""


def square_numbers(n):
    return [i ** 2 for i in range(1, n+1)]  # решение в 1 строку


def square_numbers_generator(n):
    for i in range(1, n+1):
        yield i ** 2


def memory_usage_comparison(n):

    tracemalloc.start()
    squares_lst = square_numbers(n)
    lst_current, lst_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tracemalloc.start()
    squares_generator = square_numbers_generator(n)
    gen_current, gen_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return lst_peak, gen_peak
