from modules import *

def start():
  x = Employee.Employee("Jack", 20)
  print(x)
  print(type(x))
  print(id(x))

if __name__ == "__main__":
   start()