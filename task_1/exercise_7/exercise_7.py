import logging
import time
from collections.abc import Iterable
from typing import Any, Callable, Dict, Iterable, List, Optional, Set

"""
№ 1 Создание контекстного менеджера для логирования выполнения кода

Реализуйте контекстный менеджер,
который замеряет время выполнения блока кода и записывает это время в лог.
Используйте класс ExecutionTimer, который должен поддерживать следующие функции:

Класс должен реализовывать методы __enter__ и __exit__.
Вход в контекстный менеджер должен начать отсчет времени, а выход — остановить и зафиксировать время выполнения в секундах.

Выбор типа времени: В классе предусмотрите возможность замера либо реального времени выполнения (по умолчанию),
либо процессорного времени (при установке соответствующего флага).
Это может быть полезно для более точной оценки времени работы CPU на длинных операциях.

Журналирование: В процессе работы класса ведите журнал с помощью модуля logging.

При входе в контекст: запишите сообщение о начале выполнения блока. сообщение `Execution started.`
При выходе из контекста: запишите время выполнения. сообщение `Execution finished in время seconds.`
В случае исключений: зафиксируйте возникшую ошибку в логах. сообщение `An exception occurred: ошибка`
Хранение времени выполнения: Реализуйте механизм сохранения всех измеренных временных интервалов в списке execution_times. Это нужно для подсчета среднего времени выполнения нескольких блоков кода.

Среднее время выполнения: Добавьте метод average_execution_time,
который возвращает среднее время выполнения всех замеров (либо 0, если замеров ещё не было).
"""

# логгирование
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


class ExecutionTimer:
    def __init__(self, use_cpu_time=False):
        self.use_cpu_time = use_cpu_time
        self.execution_time = 0
        self.execution_times = []

    def __enter__(self):
        self.start_time = time.process_time() if self.use_cpu_time else time.time()
        logging.info("Execution started.")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is not None:
            logging.error("An exception occurred: {}".format(exc_value))
        else:
            end_time = time.process_time() if self.use_cpu_time else time.time()
            execution_time = end_time - self.start_time
            
            self.execution_time = execution_time
            self.execution_times.append(execution_time)
            logging.info("Execution finished in {} seconds.".format(execution_time))

    def average_execution_time(self):
        return sum(self.execution_times) / len(self.execution_times) if self.execution_times else 0


"""
№ 2  Поиск общих элементов в двух наборах (set)

Реализуйте функцию для нахождения общих элементов в нескольких множествах,
поддерживая как простые типы данных, так и вложенные структуры данных (вложенные множества, списки и кортежи).
Ваше решение должно корректно обрабатывать вложенные итерабельные объекты и поддерживать рекурсивное нахождение пересечений в этих структурах.

Напишите функцию deep_intersection(set1: Set, set2: Set), которая находит пересечение между двумя множествами.
Если элемент в обоих множествах также является множеством или итерабельным объектом, функция должна рекурсивно искать пересечения внутри этих элементов.
Напишите функцию find_common_elements_recursive(*sets: List[Set]), которая находит пересечение в нескольких множествах.
Функция должна работать с произвольным количеством аргументов и вызывать рекурсивно функцию deep_intersection для каждого множества.
Программа должна корректно работать для всех типов итерабельных объектов, таких как множества, списки, кортежи, но игнорировать строки и байтовые объекты.
Если пересечение пустое, функция должна возвращать пустое множество.
"""


def deep_intersection(set1: Set, set2: Set) -> Set:
    result = set()
    for item in set1:
        if item in set2:
            result.add(item)
        elif isinstance(item, (set, list, tuple)):
            result.update(deep_intersection(set1, item))
    return result


def find_common_elements_recursive(*sets: List[Set]) -> Set:
    if not all(isinstance(s, set) for s in sets):
        raise ValueError("Все аргументы должны быть множествами.")

    if not sets:
        return set()

    result = sets[0]
    for s in sets[1:]:
        result = deep_intersection(result, s)

    return result


"""
№ 3  Напишите функцию lists_to_dict,
которая принимает два списка: keys и values.
Функция должна преобразовывать эти списки в словарь, где элементы из keys становятся ключами,
а элементы из values становятся значениями.

Если количество ключей больше количества значений,
функция должна добавлять недостающие значения как None.
Если же количество значений превышает количество ключей, функция должна обрезать лишние значения.
"""


def lists_to_dict(keys: List[Any], values: List[Any]) -> Dict[Any, Any]:
    if len(keys) > len(values):
        values.extend([None] * (len(keys) - len(values)))
    elif len(keys) < len(values):
        values = values[:len(keys)]
    return dict(zip(keys, values))


"""
№ 4 Позиционные аргументы и аргументы с именем, их воздействие на результат

Напишите функцию combine_strings, которая объединяет список строк в одну строку. Функция должна принимать три аргумента:

strings: список строк (List[str]), который нужно объединить.
transform_func: необязательная функция (Optional[Callable[[str], str]]), которая будет применяться к каждой строке перед объединением. Если не передана, строки объединяются без изменений.
delimiter: строка-разделитель (str), которая будет вставлена между строками. По умолчанию это пустая строка.

Проверить, что все элементы в strings являются строками. Если это не так, вызвать исключение ValueError с сообщением "All elements in the list must be strings."
Если передана функция трансформации, убедиться, что она является вызываемым объектом. Если нет, вызвать исключение ValueError с сообщением "Transform function must be callable."
Если функция трансформации предоставлена, применить её к каждой строке в списке strings.
Объединить строки из списка с использованием delimiter в качестве разделителя и вернуть результат.
"""


def combine_strings(
    strings: List[str],
    transform_func: Optional[Callable[[str], str]] = None,
    delimiter: str = "",
) -> str:
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the list must be strings.")
    
    if transform_func is not None and not callable(transform_func):
        raise ValueError("Transform function must be callable.")
    
    if transform_func:
        strings = list(map(transform_func, strings))
    
    result = delimiter.join(strings)
    return result
    


"""
№ 5 реализовать иерархию классов для работы с медиа-контентом.
У вас есть три типа медиа-контента: общие медиа (Media), музыка (Music) и видео (Video).
Каждый из этих типов медиа должен поддерживать базовые операции, такие как воспроизведение,
пауза и получение информации.

Базовый класс Media:

Свойства:
title (строка) – название медиа.
duration (строка) – продолжительность медиа.
_is_playing (логическое) – состояние воспроизведения (изначально False).
Методы:
play() – начинает воспроизведение медиа. Если медиа уже воспроизводится, возвращает сообщение `произведение is already playing`. Если нет – изменяет состояние и возвращает сообщение о начале воспроизведения `Playing произведение`.
pause() – ставит медиа на паузу. Если медиа не воспроизводится, возвращает сообщение `произведение is not playing`. Если воспроизводится – изменяет состояние и возвращает сообщение `Paused произведение`.
get_info() – возвращает строку с информацией о названии и продолжительности медиа (`Title: произведение, Duration: длительность`).

Класс Music (наследуется от Media):

Свойства:
genre (строка) – жанр музыки.
Методы:
Переопределяет метод play(), чтобы возвращать сообщение о воспроизведении музыки с указанием жанра.
(`произведение (Music) is already playing`), (`Playing music: произведение in genre жанр`)


Класс Video (наследуется от Media):
Свойства:
resolution (строка) – разрешение видео.
Методы:
Переопределяет метод play(), чтобы возвращать сообщение о воспроизведении видео с указанием разрешения.
(`произведение (Video) is already playing`), (`Playing video: произведение in resolution разрешение`)
"""


class Media:
    def __init__(self, title, duration, _is_playing = False):
        self.title = title
        self.duration = duration
        self._is_playing = _is_playing
    
    def play(self):
        if self._is_playing:
            return f'{self.title} is already playing'
        else:
            self._is_playing = True
            return f'Playing {self.title}'

    def pause(self):
        if self._is_playing:
            self._is_playing = False
            return f'Paused {self.title}'
        else:
            return f'{self.title} is not playing'
        

    def get_info(self):
        return f'Title: {self.title}, Duration: {self.duration}'


class Music(Media):
    def __init__(self, title, duration, genre, _is_playing=False):
        super().__init__(title, duration, _is_playing)
        self.genre = genre

    def play(self):
        if self._is_playing:
            return f'{self.title} (Music) is already playing'
        else:
            self._is_playing = True
            return f'Playing music: {self.title} in genre {self.genre}'


class Video(Media):
    def __init__(self, title, duration, resolution, _is_playing=False):
        super().__init__(title, duration, _is_playing)
        self.resolution = resolution

    def play(self):
        if self._is_playing:
            return f'{self.title} (Video) is already playing'
        else:
            self._is_playing = True
            return f'Playing video: {self.title} at resolution {self.resolution}'


"""
№ 6 Реализация кастомного стека с магическими методами __str__, __iter__

Реализовать класс CustomStack, представляющий собой стек.
Стек — это структура данных, которая следует принципу "последний пришёл — первый вышел" (LIFO).
Ваша реализация должна включать следующие методы:

Конструктор __init__:

Создайте пустой стек.
Метод push(item):

Добавляет элемент item на верх стека.
Метод pop():

Удаляет и возвращает элемент с вершины стека.
Если стек пуст, выбрасывает исключение StackError с сообщением "Pop from an empty stack".

Метод peek():

Возвращает элемент с вершины стека, не удаляя его.
Если стек пуст, выбрасывает исключение StackError с сообщением "Peek from an empty stack".
Метод is_empty():

Возвращает True, если стек пуст, и False в противном случае.
Метод __str__():

Возвращает строковое представление стека в виде списка.
Метод __iter__():

Позволяет итерировать элементы стека в порядке их добавления.
"""


class StackError(Exception):
    """Custom exception for stack errors."""
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

            
class CustomStack:
    def __init__(self):
        self.__stack = list()

    def push(self, item):
        self.__stack.append(item)
    
    def pop(self):
        if not self.__stack:
            raise StackError("Pop from an empty stack")
        else:
            return self.__stack.pop()
    
    def peek(self):
        if not self.__stack:
            raise StackError("Peek from an empty stack")
        return self.__stack[-1]
    
    def is_empty(self):
        if not self.__stack:
            return True
        else:
            return False
    
    def __str__(self):
        return str(self.__stack)
    
    def __iter__(self):
        return iter(self.__stack)
    