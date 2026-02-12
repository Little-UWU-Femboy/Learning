class Animal:  # Create class normally
    __slots__ = "name"  # Uses slots to make sure only ever has a name instance variable
    silly = ["Silly", "List", 1]  # Class variable

    def __init__(self, x):  # initalization method of object
        self.name = x

    @classmethod
    def testClassFunction(cls):
        """Test String method description"""
        print("Test class method call")
        return cls.silly  # Use the cls to access the class variable and return it


class MathStuff:
    def __init__(
        self, num1, num2
    ):  # These paremeters do not determine the variables for the class
        self.x = num1  # instance variable
        self.y = num2  # instance variable

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    def Happy(self):
        print(f"({self.x}, {self.y})")


class Dog(Animal):  # Class with inheritance
    """TEST DOCUMENTATION FOR DOG CLASS"""

    PI = 3.14  # Class variable
    WILD = "Class String thing"
    listening = MathStuff(8, 19)  # This is composition since this

    def __init__(
        self, name, breed, dob, truth
    ):  # initalization method of object + using the super() call
        super().__init__(name)  # Calls Animal.__init__
        self.breed = breed  # Public variable
        self._protected = dob  # Protected variable
        self.__pritvate = truth  # Private and really turns into _Dog__private under the hood by the inteperator

    def __del__(
        self,
    ):  # What happens right before the object gets deleted from memory
        print("Object DOG deleted")

    @classmethod
    def testingCall(cls, x, y):
        return x + y

    @property
    def Wild(self):
        return self.WILD


def start():
    x = Animal("Jack")  # Instance of Animal class
    y = Dog("DOGGO", "Yellow Jacket", "09/10/2011", False)  # Instance of Dog class
    z = MathStuff(1, 2)
    print(z.Happy())
    print(type(x))
    print(type(y))
    print(Dog.PI)  # Uses the Dog class variable
    print(Animal.silly)  # Uses the Animal class variable
    print(Dog.silly)
    print(Dog.__doc__)  # Prints the class docstring made
    print(y._protected)  # Access the protected variable, but should not do this
    # print(y.__pritvate) # Will throw an error since this variables techenically does not exit
    print(Animal.testClassFunction())  # Use the Animal class function
    print(Dog.testingCall(1, 3))  # Use the Dog class function with paremeters
    print(
        MathStuff.add(1, 2)
    )  # Uses the MathStuff class to show example of static method usage
    print(
        MathStuff.multiply(4, 5)
    )  # Uses the MathStuff class to show example of static method usage

    print(y.__dict__)  # See instance variables that are made of this current object

    y.zzz = "I AM ZZZ"  # Can add a whole new instance variable by mistake
    print(y.zzz)

    x.hh = "names"
    print(x.hh)


if __name__ == "__main__":
    start()
