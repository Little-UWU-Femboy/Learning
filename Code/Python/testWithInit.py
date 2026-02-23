import re

x = re.match("You", "Yes silly Yesterday goose")
y = re.match("You", "Youth")
print(x)
print(y)

if y is not None:
    print(y.group())
