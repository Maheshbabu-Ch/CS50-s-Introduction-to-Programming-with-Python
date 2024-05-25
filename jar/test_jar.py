from jar import Jar
import pytest

def test_init():
    ...


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(6)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(7)



def test_withdraw():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(6)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"
    jar.deposit(6)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(7)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.withdraw(7)
