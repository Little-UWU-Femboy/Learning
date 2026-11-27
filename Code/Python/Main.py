x = 1000
y = 2000

print(type(x))               # <class 'int'>
print(type(y))               # <class 'int'>

print(type(x) is type(y))    # True

print(id(type(x)))
print(id(type(y)))
print(id(int))