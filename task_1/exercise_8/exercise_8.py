import logging
import string
from collections.abc import Iterable
from typing import Dict, List, Optional

"""
№ 1 Реализовать класс MultiTempAttributes, который позволяет временно изменять значения атрибутов объекта.
Этот класс должен поддерживать контекстный менеджер, который изменяет указанные атрибуты объекта на новые значения,
а после завершения работы с объектом автоматически восстанавливает исходные значения атрибутов.

Класс MultiTempAttributes должен реализовывать следующие методы:

__init__(self, obj, attrs_values): Конструктор, принимающий два аргумента:

obj: Объект, атрибуты которого будут временно изменяться.
attrs_values: Словарь, где ключи — это имена атрибутов, которые нужно изменить, а значения — новые значения для этих атрибутов.
__enter__(self): Метод, который сохраняет исходные значения указанных атрибутов и устанавливает новые значения.

__exit__(self, exc_type, exc_value, traceback): Метод, который восстанавливает исходные значения атрибутов после выхода из контекстного менеджера, независимо от того, произошла ли ошибка.
"""


# Контекстный менеджер
class MultiTempAttributes:
    def __init__(self, obj, attrs_values):
        self.obj = obj
        self.attrs_values = attrs_values
        self.null_values = {}

    def __enter__(self):
        for attr, val in self.attrs_values.items():
            self.null_values[attr] = getattr(self.obj, attr)
            setattr(self.obj, attr, val)
        return self.obj

    def __exit__(self, exc_type, exc_value, traceback):
        for attr, val in self.null_values.items():
            setattr(self.obj, attr, val)



"""
№ 2 Подсчет уникальных слов

Вам дан текст в виде строки, содержащий слова и пунктуацию.
Напишите функцию, которая определяет количество уникальных слов в этом тексте. Для подсчета уникальных слов следует учитывать следующие условия:

Текст должен быть приведен к нижнему регистру, чтобы слова с разными регистрами считались одинаковыми.
Все знаки пунктуации должны быть удалены из текста.
После удаления пунктуации текст следует разбить на слова, разделенные пробелами.
Слово считается уникальным, если оно встречается в тексте только один раз после удаления пунктуации и приведения текста к нижнему регистру.
"""


def count_unique_words(text: str) -> int:
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, '')
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

"""
№ 3 Анализ четных чисел

Аргументы:
numbers: Список целых чисел.


Возвращаемое значение:
Словарь с ключами:
"count": Количество четных чисел.
"sum": Сумма четных чисел (или None, если четных чисел нет).
"average": Среднее значение четных чисел (или None, если четных чисел нет).
"max": Максимальное значение четных чисел (или None, если четных чисел нет).
"min": Минимальное значение четных чисел (или None, если четных чисел нет).
"""


def analyze_even_numbers(numbers: List[int]) -> Dict[str, Optional[float]]:
    numbers = [num for num in numbers if num % 2 == 0]
    result = {
        "count": len(numbers),
        "sum": sum(numbers) if numbers else None,
        "average": sum(numbers) / len(numbers) if numbers else None,
        "max": max(numbers) if numbers else None,
        "min": min(numbers) if numbers else None,
    }
    return result


"""
№ 4 Проверка уникальности элементов в вложенных структурах данных

Реализовать функцию all_unique_elements, которая проверяет,
содержатся ли в заданной структуре данных только уникальные элементы.

Поддерживаются следующие типы данных:
Строки
Списки
Кортежи
Множества
Вложенные структуры (например, списки внутри списков и т.д.)
Функция должна игнорировать значения типа None.
"""


def all_unique_elements(data) -> bool:
    def flatten(d):
        """Вспомогательная функция для рекурсивного разворачивания вложенных структур"""
        if isinstance(d, (list, tuple, set)):
            return [item for sublist in d for item in flatten(sublist) if item is not None]
        elif isinstance(d, dict):
            return [item for sublist in d.values() for item in flatten(sublist) if item is not None]
        return [d]

    flattened_data = flatten(data)

    return len(flattened_data) == len(set(flattened_data))


"""
№ 5 

Напишите функцию enumerate_list,
которая принимает на вход список data и возвращает новый список,
содержащий элементы из data, но каждый элемент дополнен его индексом.
Индекс каждого элемента рассчитывается начиная с start и увеличивается на step для каждого следующего элемента.

Функция должна поддерживать следующие параметры:

data (list): список, элементы которого нужно перечислить.
start (int, по умолчанию 0): начальный индекс.
step (int, по умолчанию 1): шаг, на который увеличивается индекс.
recursive (bool, по умолчанию False): если True, функция должна рекурсивно обрабатывать вложенные списки.
Функция должна возвращать список, в котором каждый элемент является кортежем из двух элементов: индекса и значения из исходного списка.
"""


def enumerate_list(data: list, start: int = 0, step: int = 1, recursive: bool = False) -> list:
    def recursive_enumerate(lst, idx):
        result = []
        for i, item in enumerate(lst):
            if isinstance(item, list) and recursive:
                result.append((idx, recursive_enumerate(item, idx)))
            else:
                result.append((idx, item))
            idx += step
        return result
    return recursive_enumerate(data, start)

"""
№ 6 Реализация контекстного менеджера для подключения к базе данных (симуляция)

Вам необходимо реализовать класс DatabaseConnection,
который будет управлять подключением к базе данных и транзакциями(симуляция в виде сообщений),
используя менеджер контекста. Класс должен поддерживать следующие функции:

Инициализация: При создании экземпляра класса, он должен принимать имя базы данных (db_name), к которой будет подключаться.

Менеджер контекста: Класс должен реализовывать методы __enter__ и __exit__, чтобы использовать его в блоке with. 
При входе в блок контекста должно происходить подключение к базе данных, а при выходе из блока — закрытие соединения и обработка возможных ошибок.

Подключение к базе данных: Метод connect должен инициировать подключение к базе данных и сохранять его состояние.

Выполнение запроса: Метод execute_query должен выполнять запрос, если активна транзакция. В противном случае должен выбрасываться исключение.

Управление транзакциями: Методы start_transaction, commit и rollback должны управлять транзакциями. Транзакция должна быть активна для выполнения запросов, и должна быть закрыта после коммита или отката.

Логирование: Класс должен использовать встроенный модуль logging для записи логов подключения, выполнения запросов, начала и завершения транзакций, а также для обработки ошибок.
"""

# Настройка логирования для примера
logging.basicConfig(level=logging.INFO)


class DatabaseConnection:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.connection = None
        self.transaction_active = False

    def __enter__(self):
        logging.info(f"Connecting to the database {self.db_name}")
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        logging.info(f"Closing the database {self.db_name} connection")
        self.close()

    def connect(self):
        logging.info(f"A connection to the database {self.db_name} has been established")
        self.connection = f"Connected to {self.db_name} database"

    def execute_query(self, query: str):
        if self.transaction_active:
            logging.info(f"Request execution: {query}")
            return f"Result of '{query}'"
        else:
            raise RuntimeError("No active transaction")

    def start_transaction(self):

        if not self.transaction_active:
            logging.info(f"The beginning of the transaction")
            self.transaction_active = True
        else:
            logging.warning("The transaction is already active")


    def commit(self):
        if self.transaction_active:
            logging.info("Transaction commit")
            self.transaction_active = False
        else:
            raise RuntimeError("No active transaction to commit")

    def rollback(self):

        if self.transaction_active:
            logging.info("Rollback a transaction")
            self.transaction_active = False
        else:
            logging.warning("The transaction is not active")

    def close(self):

        if self.connection:
            logging.info("The connection to the database is closed")
            self.connection = None
            self.transaction_active = False
        else:
            logging.warning("The connection to the database has already been closed")