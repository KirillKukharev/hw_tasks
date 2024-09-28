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
    def __init__(self, name, mood, hunger=10, tiredness=0):
        self._name = name
        self._mood = mood
        self._hunger = hunger
        self._tiredness = tiredness

    @property
    def name(self):
        return self._name

    @property
    def mood(self):
        return self._mood

    @property
    def hunger(self):
        return self._hunger

    @property
    def tiredness(self):
        return self._tiredness

    @name.setter
    def name(self, value):
        self._name = value

    @mood.setter
    def mood(self, value):
        self._mood = value

    @hunger.setter
    def hunger(self, value):
        if value > 10:
            raise ValueError
        self._hunger = value

    @tiredness.setter
    def tiredness(self, value):
        if value > 10:
            raise ValueError
        self._tiredness = value

    @abstractmethod
    def speak(self):
        pass

    def feed(self):
        if self.hunger > 3:
            self.hunger -= 3
        else:
            self.hunger = 0
        print("Feed")

    def rest(self):
        if self.tiredness > 3:
            self.tiredness -= 3
        else:
            self.tiredness = 0
        print("Rest")

    def play(self, toy):
        if toy.is_fun:
            self.mood = "happy"
        self.tiredness += 2
        print("Play")

    def stat(self):
        if self.hunger > 7:
            return "hungry"
        if self.mood == "happy":
            return "happy"


class Dog(Animal):
    def speak(self):
        return f"Woof! I'm {self.stat()}!"


class Cat(Animal):
    def speak(self):
        return f"Meow! I'm {self.stat()}!"


class Parrot(Animal):
    def speak(self):
        # if str.lower(self.name) == "говорун":
        #     return "Птица Говорун обладает умом и сообразительностью"
        return "Кря! I'm {self.stat()}!"


class Toy:
    def __init__(self, name, is_fun):
        self.name = name
        self.interest = is_fun

    def is_fun(self):
        return self.interest


"""
№ 2 Написать класс с использованием магических методов (__str__, __len__, __getitem__).

для __len__ выводить длину объекта

для __str__ выводить `MyContainer with длина объекта items`

для __getitem__ выводить значение по индексу
"""


class MyContainer:
    def __init__(self, items):
        self.items = items

    def __str__(self):
        return f"MyContainer with {len(self.items)} items"

    def __len__(self):
        return len(self.items)

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
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


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


def list_tuple_operations_deep(lst, tpl):
    answer = ["", "", "", ""]
    start_list = time.time()
    time.sleep(0.0001)
    answer[0] = modify_list(lst)
    end_list = time.time()
    answer[2] = end_list - start_list

    start_tuple = time.time()
    time.sleep(0.0001)
    answer[1] = modify_tuple(tpl)
    end_tuple = time.time()

    answer[3] = end_tuple - start_tuple

    return tuple(answer)


def modify_list(lst):
    for i in range(len(lst)):
        if type(lst[i]) == list:
            modify_list(lst[i])
        else:
            lst[i] = 'modified'

    return lst


def modify_tuple(tpl):
    try:
        for i in range(len(tpl)):
            if type(tpl[i]) == tuple:
                modify_tuple(tpl[i])
            else:
                tpl[i] = 'modified'

        return tpl
    except Exception as ex:
        return str(ex)


"""
№ 5 Напишите функцию, которая принимает большое число n и возвращает квадраты всех чисел от 1 до n как с использованием списка,
так и с использованием генератора. Измерьте память с помощью tracemalloc.get_traced_memory(), занимаемую каждым подходом.
"""


def square_numbers(n):
    return [x ** 2 for x in range(1, n + 1)]  # решение в 1 строку


def square_numbers_generator(n):
    for i in range(n):
        yield (i + 1) ** 2


def memory_usage_comparison(n):
    answer = ""

    square_numbers(n)
    current, peak = tracemalloc.get_traced_memory()
    answer += "current = " + str(current) + ", peak = " + str(peak) + "\n"

    tracemalloc.reset_peak()

    square_numbers_generator(n)
    current1, peak1 = tracemalloc.get_traced_memory()
    answer += "current = " + str(current) + ", peak = " + str(peak)

    return (peak, peak1)