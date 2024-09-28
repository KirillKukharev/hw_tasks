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
    execution_times = list[float]

    def __init__(self, use_cpu_time=False):
        """
        :param use_cpu_time: если True, измеряется время процессора (CPU), в противном случае измеряется реальное время
        """
        self.use_cpu_time = use_cpu_time

    def __enter__(self):
        """Запуск таймера и регистрация начала выполнения."""
        self.start_time = time.process_time() if self.use_cpu_time else time.time()
        logging.info("Execution started.")
        return self  # Возвращает self, чтобы разрешить извлечение времени выполнения из контекста

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Остановка таймера, запись результата и обработка исключений."""
        self.end_time = time.process_time() if self.use_cpu_time else time.time()
        self.elapsed_time = self.end_time - self.start_time
        self.execution_times.append(self.elapsed_time)

        if exc_type is None:
            logging.info(f"Execution finished in {self.elapsed_time:.6f} seconds.")
        else:
            logging.error(f"An exception occurred: {exc_val}")

    @classmethod
    def average_execution_time(self):
        """Возврат среднего времени выполнения всех записанных блоков."""
        if not self.execution_times:
            return 0
        return sum(self.execution_times) / len(self.execution_times)



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


def is_iterable(obj: Any) -> bool:
    """
    Проверьте, является ли объект итерабельным.
    """
    return isinstance(obj, Iterable) and not isinstance(obj, (str, bytes))


def deep_intersection(set1: Set, set2: Set) -> Set:
    """
    Рекурсивное нахождение пересечения между двумя наборами.
    Если элемент в обоих наборах также является итерабельным (вложенное множество, список или кортеж),
    функция будет рекурсивно искать пересечения внутри этих элементов.
    """
    result = set()
    
    for item in set1:
        if item in set2:
            if isinstance(item, set):
                sub_intersection = deep_intersection(item, set2 & {item})
                if sub_intersection:
                    result.add(frozenset(sub_intersection))
            elif is_iterable(item):
                corresponding_item = next((x for x in set2 if isinstance(x, type(item))), None)
                if corresponding_item:
                    common_elements = deep_intersection(set(item), set(corresponding_item))
                    if common_elements:
                        result.add(type(item)(common_elements))
            else:
                result.add(item)
    
    return result


def find_common_elements_recursive(*sets: Set) -> Set:
    """
    Нахождение пересечений нескольких наборов, рекурсивно обрабатывая вложенные повторяющиеся значения.
    Поддерживает произвольное количество наборов и рекурсивно вызывает deep_intersection.
    """
    if not sets:
        return set()
    
    common = sets[0]
    for s in sets[1:]:
        common = deep_intersection(set(common), set(s))
        if not common:
            return set()
    return common




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
    """
    Преобразование двух списков (ключи и значения) в словарь.
    
    Если ключей больше, чем значений, дополнительные ключи будут иметь значение None.
    Если значений больше, чем ключей, дополнительные значения будут проигнорированы.
    """
    result = {key: value for key, value in zip(keys, values)}
    for key in keys[len(values):]:
        result[key] = None
    return result


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
    """
    Объединение списка строк в одну строку с необязательным преобразованием и разделителем.
    
    Args:
        :param strings: Список строк, которые нужно объединить.
        :param transform_func: Дополнительная функция для преобразования каждой строки перед объединением.
        :param delimiter: Строка-разделитель для разделения объединенных строк (по умолчанию используется пустая строка).
    
    Returns:
        :return str: Объединенная строка с примененными преобразованиями и разделителем.
    
    Raises:
        :raises ValueError: Если какой-либо элемент в строках не является строкой.
        :raises ValueError: Если transform_func указан и не может быть вызван.
    """
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the list must be strings.")
    
    if transform_func is not None and not callable(transform_func):
        raise ValueError("Transform function must be callable.")
    
    if transform_func:
        strings = [transform_func(s) for s in strings]

    return delimiter.join(strings)


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
    def __init__(self, title: str, duration: str):
        self.title = title
        self.duration = duration
        self._is_playing = False
    
    def play(self) -> str:
        if self._is_playing:
            return f"{self.title} is already playing."
        self._is_playing = True
        return f"Playing {self.title}."
    
    def pause(self) -> str:
        if not self._is_playing:
            return f"{self.title} is not playing."
        self._is_playing = False
        return f"Paused {self.title}."
    
    def get_info(self) -> str:
        return f"Title: {self.title}, Duration: {self.duration}"

    
class Music(Media):
    def __init__(self, title: str, duration: str, genre: str):
        super().__init__(title, duration)
        self.genre = genre
    
    def play(self) -> str:
        if self._is_playing:
            return f"{self.title} (Music) is already playing."
        self._is_playing = True
        return f"Playing music: {self.title} in genre {self.genre}."


class Video(Media):
    def __init__(self, title: str, duration: str, resolution: str):
        super().__init__(title, duration)
        self.resolution = resolution
    
    def play(self) -> str:
        if self._is_playing:
            return f"{self.title} (Video) is already playing."
        self._is_playing = True
        return f"Playing video: {self.title} in resolution {self.resolution}."


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
    pass


class CustomStack:
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if self.is_empty():
            raise StackError("Pop from an empty stack")
        return self._stack.pop()

    def peek(self):
        if self.is_empty():
            raise StackError("Peek from an empty stack")
        return self._stack[-1]

    def is_empty(self):
        return len(self._stack) == 0

    def __str__(self):
        return str(self._stack)

    def __iter__(self):
        return iter(self._stack)