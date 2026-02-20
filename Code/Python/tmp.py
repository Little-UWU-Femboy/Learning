import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize("x, y, z", [(1, 2, 3), (4, 5, 9), (10, 11, 30)])
def test_add(x, y, z):
    print(f"x = {x}, y={y}, z={z}")
    assert add(x, y) >= z


# First run will have x = 1, y = 2, z = 3
# Second run will have x = 4, y = 5, z = 9
# Third run will have x = 10, y = 11, z = 30
