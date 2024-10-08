"""
№ 1 Написание контекстного менеджера для управления ресурсами
В этом задании вам нужно реализовать класс ResourceManager,
который будет управлять ресурсами с использованием механизма менеджера контекста.
Класс должен обеспечивать открытие и закрытие ресурса (например, файла),
а также запись информации о том, когда ресурс был инициализирован и освобождён.

При входе в блок with, класс должен открывать файл resource.txt в режиме записи 
и записывать в него строку "Resource initialized\n".
При выходе из блока with, в файл должна записываться строка "Resource released\n",
и файл должен закрываться.

Необходимо, чтобы запись инициализации и освобождения ресурса происходила автоматически с использованием методов __enter__ и __exit__.
"""


"""
№ 2 Проверка изменяемости и неизменяемости через вложенные структуры

Реализовать функцию check_nested_mutability,
которая проверяет и изменяет вложенные элементы изменяемых структур данных.
Функция должна принимать список или кортеж, изменять их первый вложенный элемент,
и возвращать изменённый объект.
В случае, если передан неподдерживаемый тип данных, должно быть вызвано исключение `Unsupported data type`.
"""


"""
№ 3 Создание матрицы с помощью enumerate и zip

Реализовать функцию create_matrix, которая создаёт матрицу заданного размера
и заполняет её числами по порядку, начиная с 0.
Числа должны быть расположены по строкам слева направо.

Функция должна принимать два параметра: количество строк rows и количество столбцов cols.
На основе этих параметров необходимо создать матрицу (список списков), состоящую из нулей.
После создания матрицы, каждый элемент должен быть заменён на порядковый номер, начиная с 0, заполняя матрицу слева направо по строкам.
"""


def create_matrix(rows, cols):


"""
№ 4 Генерация бесконечной последовательности чисел Фибоначчи
реализовать генератор fibonacci(),
который бесконечно генерирует последовательность чисел Фибоначчи.
Последовательность Фибоначчи начинается с чисел 0 и 1, а каждое следующее число равно сумме двух предыдущих.
"""


# Генератор (yield)
def fibonacci():


"""
№ 5 Реализация функции с переменным числом позиционных и именованных аргументов

Реализуйте функцию advanced_function, которая:
	Суммирует все числовые позиционные аргументы.
	Объединяет все строковые позиционные аргументы.
	Для именованных аргументов:
		Если ключ начинается с префикса 'sum_', то их значение добавляется к общему числовому результату.
		Если ключ начинается с префикса 'concat_', то их значение добавляется к общей строке.
	Игнорирует все другие именованные аргументы.
"""


def advanced_function(*args, **kwargs):


"""
№ 6 Полиморфизм через абстрактные классы и динамическое изменение типа объекта

Реализовать систему классов для различных типов транспортных средств: 
автомобиль, велосипед и электрический скутер.
В основе системы лежит абстрактный класс Vehicle, который задаёт общие методы и поведение для всех транспортных средств.
Кроме того, вам нужно реализовать фабричный метод для создания объектов этих классов.

Создайте абстрактный класс Vehicle, который включает следующие методы:
Конструктор __init__(self, fuel): инициализирует количество топлива.
Абстрактные методы drive() и refuel(amount), которые должны быть реализованы в дочерних классах.
Метод check_fuel(), который проверяет наличие топлива и выбрасывает исключение `Out of fuel!`, если топливо закончилось.

Класс Car, который наследует Vehicle:
Конструктор принимает количество топлива.
Метод drive() устанавливает скорость 60 км/ч и уменьшает топливо на 10 единиц. Возвращает строку `Driving a car at скорость km/h, remaining fuel: топливо`
Метод refuel(amount) добавляет указанное количество топлива. Возвращает строку `Refueled car. Current fuel: топливо`

Класс Bike, который наследует Vehicle:
Велосипед не использует топливо, поэтому передаём None в конструкторе.
Метод drive() устанавливает скорость 20 км/ч. Возвращает строку `Riding a bike at скорость km/h`.
Метод refuel() вызывает исключение NotImplementedError с сообщением `Bikes don't need fuel!`, так как велосипед не нуждается в топливе.

Класс ElectricScooter, который наследует Vehicle:
Вместо топлива используется уровень заряда батареи.
Метод drive() уменьшает заряд батареи на 20%, если заряд достаточный. Возвращает строку `Riding an electric scooter with заряд батареи%  battery remaining`
Если заряд батареи 0 или меньше, то исключение с сообщением `Battery empty!`
Метод refuel() вызывает исключение NotImplementedError с сообщением `Electric scooters don't use fuel, recharge battery instead!`, так как электрический скутер использует батарею, а не топливо.

Реализуйте класс VehicleFactory с методом create_vehicle, который создаёт объекты классов Car, Bike или ElectricScooter в зависимости от типа транспортного средства:
Для Car передаётся количество топлива.
Для ElectricScooter передаётся уровень заряда батареи.
Для Bike параметры не нужны, так как велосипед не использует топливо.
"""
from abc import ABC, abstractmethod


# Абстрактный класс
class Vehicle(ABC):
    pass


# Реализация для автомобиля
class Car(Vehicle):
    pass


# Реализация для велосипеда
class Bike(Vehicle):
    pass


# Электрический скутер
class ElectricScooter(Vehicle):
    pass


# Фабричный метод для создания транспортных средств
class VehicleFactory:
    @staticmethod
    pass
