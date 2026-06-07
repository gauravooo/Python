# Please implement a class called Jar that models a cookie jar. The Jar class should have the following methods and properties:
from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(5)
    assert jar.capacity == 5
    with pytest.raises(ValueError):
        Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(12)
    jar.deposit(4)
    assert jar.size == 4
    jar.deposit(3)
    assert jar.size == 7


def test_withdraw():
    jar = Jar(12)
    jar.deposit(7)
    assert jar.size == 7
    jar.withdraw(3)
    assert jar.size == 4


def test_capacity_property():
    jar = Jar(20)
    assert jar.capacity == 20

def test_size_property():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
