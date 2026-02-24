import re

x = re.match("You", "Yes silly Yesterday goose")
y = re.findall("You", "Youth You You with You yo You")
print(x)
print(y)

if x is not None:
    print(x)
if y is not None:
    print(y)
