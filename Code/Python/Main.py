"""
Dummy Python file demonstrating many Python concepts and keywords.
this this is nice
"""

# ------------------------
# Imports
# ------------------------
import math
import sys
import ModuleTest
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Optional, Generator

# ------------------------
# Global Variable
# ------------------------
GLOBAL_COUNTER = 0


# PERSONAL MADE
class Employee:
    def __init__(self, x, y, n: str):
        self.x = x
        self.y = y
        self.NAME = n

    def info(self):
        """
        This is a function to display test information
        When it comes to this being on a second line!
        I am happy!
        """
        return "TEST FUNCTION DONE"

    @classmethod
    def classDescription(cls):
        print("I am the Employee class")


# ------------------------
# Enum
# ------------------------
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Employee.classDescription())


# ------------------------
# Dataclass
# ------------------------
@dataclass
class Point:
    x: float
    y: float


thingy = "TEST NAME"
thingyage = 50
jack = Employee(3, 1, "Jack Black")


print(jack.NAME)


def tmp():
    return "FUNCTION TESTING"


# ------------------------
# Decorator
# ------------------------
def logger(func):
    def wrapper(*args, **kwargs):
        print(
            f"Calling {func.__name__} is nice when we can see the age {40} and the house of {thingyage} with {thingy} and function {tmp()} with employee {jack.NAME} and {jack.x + 4} with {jack.info()}"
        )
        return func(*args, **kwargs)

    return wrapper


# ------------------------
# Function with Type Hints
# ------------------------
@logger
def add(a: int, b: int) -> int:
    return a + b


# ------------------------
# Lambda
# ------------------------
square = lambda x: x * x


# ------------------------
# Generator
# ------------------------
def count_up_to(n: int) -> Generator[int, None, None]:
    i = 0
    while i < n:
        yield i
        i += 1


# ------------------------
# Class + Inheritance
# ------------------------
class Animal:
    def speak(self):
        raise NotImplementedError


class Dog(Animal):
    def speak(self):
        return "Woof"


# ------------------------
# Context Manager
# ------------------------
class DummyFile:
    def __enter__(self):
        print("Opening resource")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing resource")


# ------------------------
# Closure with nonlocal
# ------------------------
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


# ------------------------
# Async Function
# ------------------------
async def async_task():
    return "Async result"


# ------------------------
# Control Flow Demo
# ------------------------
def control_flow_demo(x):
    if x > 10:
        print("Greater than 10")
    elif x == 10:
        print("Exactly 10")
    else:
        print("Less than 10")

    for i in range(3):
        if i == 1:
            continue
        if i == 2:
            break
        print("Loop:", i)

    i = 0
    while i < 2:
        print("While loop:", i)
        i += 1


# ------------------------
# Match (Pattern Matching)
# ------------------------
def http_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"


# ------------------------
# Exception Handling
# ------------------------
def exception_demo():
    try:
        x = int("not_a_number")
    except ValueError as e:
        print("Caught exception:", e)
    else:
        print("No error occurred")
    finally:
        print("Finally block executed")


# ------------------------
# Comprehensions
# ------------------------
def comprehension_demo():
    nums = [1, 2, 3, 4]

    squares = [n * n for n in nums]
    square_set = {n * n for n in nums}
    square_dict = {n: n * n for n in nums}

    return squares, square_set, square_dict


# ------------------------
# Assertions
# ------------------------
def assert_demo(x):
    assert x > 0, "x must be positive"


# ------------------------
# Main
# ------------------------
def main():
    global GLOBAL_COUNTER
    GLOBAL_COUNTER += 1

    print(add(2, 3))
    print(square(4))

    p = Point(1.5, 2.5)
    print(p)

    dog = Dog()
    print(dog.speak())

    for num in count_up_to(3):
        print("Generator:", num)

    inc = counter()
    print(inc(), inc(), inc())

    control_flow_demo(5)

    print(http_status(404))

    exception_demo()

    print(comprehension_demo())

    assert_demo(1)

    with DummyFile() as f:
        pass


# ------------------------
# Entry Point
# ------------------------
if __name__ == "__main__":
    main()

    testing = Employee(2, 3, "Yes")
    testing.info()
    valueNumber = add(4, 5)
    print(ModuleTest.externalAdd())

    sys.exit()
