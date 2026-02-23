"""
Comprehensive Python Keyword & Design Patterns Demo
Python 3.12+
"""

# ===============================
# IMPORT KEYWORDS
# ===============================
import math
import asyncio
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import final

# ===============================
# GLOBAL / ASSERT / DEL
# ===============================
GLOBAL_VAR = "I am global"

def use_global():
    global GLOBAL_VAR
    GLOBAL_VAR = "Modified globally"

use_global()
assert GLOBAL_VAR == "Modified globally"

temp_var = 123
del temp_var


# ===============================
# ABSTRACT BASE CLASS (Abstraction)
# ===============================
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# ===============================
# DATACLASS + ENCAPSULATION
# ===============================
@dataclass
class Rectangle(Shape):
    width: float
    height: float

    def area(self):
        return self.width * self.height


# ===============================
# INHERITANCE + POLYMORPHISM
# ===============================
class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius  # Encapsulation

    def area(self):
        return math.pi * self.__radius ** 2


# ===============================
# SINGLETON (Design Pattern)
# ===============================
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# ===============================
# FACTORY PATTERN
# ===============================
class ShapeFactory:

    @staticmethod
    def create(shape_type, *args):
        if shape_type == "rectangle":
            return Rectangle(*args)
        elif shape_type == "circle":
            return Circle(*args)
        else:
            raise ValueError("Unknown shape")


# ===============================
# STRATEGY PATTERN
# ===============================
class OperationStrategy(ABC):

    @abstractmethod
    def execute(self, a, b):
        pass


class AddStrategy(OperationStrategy):
    def execute(self, a, b):
        return a + b


class MultiplyStrategy(OperationStrategy):
    def execute(self, a, b):
        return a * b


# ===============================
# DECORATOR PATTERN
# ===============================
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_decorator
def decorated_function(x):
    return x * 2


# ===============================
# CONTEXT MANAGER
# ===============================
class CustomContext:

    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        return False


# ===============================
# GENERATOR + YIELD
# ===============================
def generator_example():
    for i in range(3):
        yield i


# ===============================
# ASYNC / AWAIT
# ===============================
async def async_function():
    await asyncio.sleep(1)
    return "Async Done"


# ===============================
# MATCH / CASE (Structural Pattern Matching)
# ===============================
def match_example(value):
    match value:
        case 1:
            return "One"
        case 2 | 3:
            return "Two or Three"
        case _:
            return "Other"


# ===============================
# TRY / EXCEPT / FINALLY / RAISE
# ===============================
def exception_demo():
    try:
        raise RuntimeError("Error occurred")
    except RuntimeError as e:
        print(f"Caught: {e}")
    finally:
        print("Cleanup done")


# ===============================
# WITH / LAMBDA / NONLOCAL
# ===============================
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
    inner()
    return x


square = lambda x: x * x


# ===============================
# MAIN EXECUTION
# ===============================
if __name__ == "__main__":

    shapes = [
        ShapeFactory.create("rectangle", 4, 5),
        ShapeFactory.create("circle", 3)
    ]

    for shape in shapes:
        print(f"Area: {shape.area()}")

    print(decorated_function(5))

    with CustomContext():
        print("Inside block")

    for value in generator_example():
        print(value)

    asyncio.run(async_function())

    print(match_example(2))
    exception_demo()

    print("Nonlocal result:", outer())
    print("Lambda result:", square(4))

    # Singleton demo
    s1 = Singleton()
    s2 = Singleton()
    print("Singleton works:", s1 is s2)
