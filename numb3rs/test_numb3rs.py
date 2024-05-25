from numb3rs import validate

def test_1():
    assert validate("192.168.1.1") == True

def test_2():
    assert validate("cat") == False

def test_3():
    assert validate("512.512.512.512") == False

def test_4():
    assert validate("1.2.3.1000") == False

def test_5():
    assert validate("255.255.255.255") == True

def test_6():
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False

def test_7():
    assert validate("256.255.255.255") == False

def test_8():
    assert validate("68.422.242.744") == False


