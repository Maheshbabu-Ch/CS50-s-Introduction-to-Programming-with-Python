from um import count

def test_1():
    assert count("um") == 1

def test_2():
    assert count("um?") == 1

def test_3():
    assert count("Um, thanks for the album.") == 1

def test_12():
    assert count("Um, thanks, um...") == 2

def test_4():
    assert count("Um, hello ") == 1

def test_5():
    assert count("gum") == 0

# def test_6():
#     count("UM") == 1

# def test_7():
#     count("drum, um,., um bum lum sum um") == 3

# def test_8():
#     count("ummmm.... um mmu um") == 2

# def test_9():
#     count(" um ") == 1

# def test_10():
#     count("UM") == 1

# def test_11():
#     count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
