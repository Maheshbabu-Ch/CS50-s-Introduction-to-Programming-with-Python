from plates import is_valid

def test_1():
    assert is_valid("HELLO") == True

def test_2():
    assert is_valid("HELLO, WORLD") == False

def test_3():
    assert is_valid("GOODBYE") == False

def test_4():
    assert is_valid("CS50") == True

def test_5():
    assert is_valid("CS05") == False

def test_6():
    assert is_valid("1234") == False

def test_7():
    assert is_valid("CS5D3") == False

def test_8():
    assert is_valid("PI3.14") == False

