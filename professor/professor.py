import random


def main():
    lvl = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        c = 0
        sum = x + y
        while True:
            try:
                ans = input(f"{x} + {y} = ")
                if not ans.isdigit():
                    raise ValueError
                ans = int(ans)
                if ans == sum:
                    # print("Correct")
                    score += 1
                    break
                if ans != sum or c <= 3:
                    c+=1
                    print("EEE")
                if c == 3:
                    print(f"{x} + {y} = {sum}")
                    break

            except ValueError:
                print("EEE")
                continue

    print("Score:",score)

def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            # if not lvl.isdigit() or 1 <= int(lvl) <= 3:
            if 0 < lvl <= 3:
                # raise ValueError
                return lvl
        except ValueError:
            continue



def generate_integer(level):
    if level == 1:
        mi = 0
    else:
        mi = 10 ** (level - 1)
    ma = 10 ** level - 1
    # print(mi,ma)
    return random.randint(mi,ma)




if __name__ == "__main__":
    main()
