from twttr import shorten

def test_abc():
    assert shorten("Pink Panther") == "Pnk Pnthr"

def test_err():
    assert shorten("uello guru") == "ll gr"

def test_upp():
    assert shorten("PINKYPONKY") == "PNKYPNKY"

def test_punc():
    assert shorten("He's Name is Yuzi. ") == "H's Nm s Yz. "

def test_num():
    assert shorten("singham123") == "snghm123"


