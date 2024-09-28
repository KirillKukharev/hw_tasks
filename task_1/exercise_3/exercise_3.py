import json
import math
import time

"""
№ 1 Создание словаря из двух списков с помощью zip
"""
def lists_to_dict(keys: list, values: list) -> dict:
    return dict(zip(keys, values)) # решение в 1 строку

"""
№ 2 Сериализация и сумма значений генератора (используя yield и генераторные выражения)
"""

def generate_numbers(n: int): # функция-генератор для создания значений от 0 до n
    for i in range (n):
        yield i 

def sum_generator(gen): # функция-генератор для суммирования
    return sum(i for i in gen) # решение в 1 строку

def serialize_generator(gen): # функция сериализации генератора
    return str(list(gen)) # решение в 1 строку

"""
№ 3 Валидация типов параметров с использованием аннотаций
"""
def validate_param_types(a: int, b: float, c: str) -> bool:
    if not isinstance(a, int):
        return False
    if not isinstance(b, float):
        return False
    if not isinstance(c, str):
        return False
    return True

"""
№ 4 Реализация классов с полиморфизмом и наследованием
Реализовать класс Rectangle, при инициализации можно указать ширину (width) и высоту (height)
Реализовать метод area для нахождения площади прямоугольника.

Реализовать класс Circle, при инициализации можно указать радиус (radius)
Реализовать метод area для нахождения площади круга.

Реализовать класс PrivateData при инициализации можно указать значение приватной переменной data.
Реализовать метод get_data для получения значения приватной переменной без указания параметров.
"""

# Полиморфизм через наследование
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius = 0):
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius ** 2)


# Инкапсуляция
class PrivateData:
    def __init__(self, data = 0):
        self.__data = data
    
    def get_data(self):
        return self.__data


"""
№ 5 Создание класса с перегрузкой операторов
Реализовать класс ComplexNumber, при инициализации можно указать действительную и мнимую части
Реализовать метод сложения действительной и мнимой частей для двух объектов класса ComplexNumber
Реализовать метод для отображения строки `(действительная часть + мнимания часть i)`
Реализовать метод для сравнения двух комплексных чисел
"""

class ComplexNumber:
    def __init__(self, real = 0, imaginary = 0):
        self.__real = real
        self.__imaginary = imaginary
      
    def __add__(self, complex2):
        return ComplexNumber(self.__real + complex2.__real, self.__imaginary + complex2.__imaginary)

    def __repr__(self):
        return f"({self.__real} + {self.__imaginary}i)"

    def __str__(self):
        return f"({self.__real} + {self.__imaginary}i)"

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.__real == other.__real and self.__imaginary == other.__imaginary


"""
№ 6 Создание и использование контекстного менеджера для долговременных операций
Реализовать класс LongOperationManager.
При инициализации контекстного менеджера можно задать время, также необходимо вывести принтом `Start long operation` и вернуть объект.
При окончании долгосрочной операции отобразить информацию о длительности операции принтом `End long operation in кол-во секунд seconds`.
Если возникла ошибка, вывести принтом сообщение `Exception: значение ошибки`
"""

class LongOperationManager:
    def __init__(self, duration = 0):
        self.__duration = duration
        print("Start long operation")

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        final_time = end_time - self.start_time

        if exc_type:
            print(f"Exception: {exc_val}")
        else:
            print(f"End long operation in {final_time:.2f} seconds")

        return False