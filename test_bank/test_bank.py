from bank import value

def test_hello():
    assert value("Hello") == 0

def test_2():
    assert value("Hello, Newman") == 0

def test_3():
    assert value("How you doing?") == 20

def test_4():
    assert value("What's happening?") == 100

