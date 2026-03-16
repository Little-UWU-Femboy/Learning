def publicFunctionFromEmployee():
    pass

def _privateFunctionFromEmployee():
    pass

class Employee:
    PI = 3.14159

    def __init__(self, n:str, a:int):
        self.name = n
        self.age = a

    def __str__(self):
        return f"Name={self.name} and age = {self.age}"

    @staticmethod
    def staticMethodCall():
        print("I AM A STATIC METHOD")

    @classmethod
    def classMethodCall(cls):
        print(f"I AM A CLASS METHOD AND PI IS {cls.PI}")