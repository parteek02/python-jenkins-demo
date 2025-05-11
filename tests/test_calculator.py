from app import calculator


def test_add():
    assert calculator.add(3, 2) == 5


def test_subtract():
    assert calculator.subtract(5, 3) == 2
