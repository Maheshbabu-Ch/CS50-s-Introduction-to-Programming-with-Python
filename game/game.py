import random
n = "-1"
while not n.isdigit() or int(n) < 0:
    n = input("Level: ")
n = int(n)
a = random.randint(0,n)
# g = int(input("Guess: "))
while True:
    try:
        g = int(input("Guess: "))
        if g < 0:
            continue
        if g < a:
            print("Too small!")
        elif g > a:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue
