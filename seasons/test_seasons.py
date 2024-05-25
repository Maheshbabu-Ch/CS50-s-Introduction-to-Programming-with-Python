from seasons import convo
import pytest

def test_1():
    assert convo("2023-05-24") == "Five hundred twenty-seven thousand forty minutes"

def test_2():
    assert convo("2022-05-24") == "One million, fifty-two thousand, six hundred forty minutes"

def test_3():
    with pytest.raises(SystemExit):
        convo("2023-20-10")
