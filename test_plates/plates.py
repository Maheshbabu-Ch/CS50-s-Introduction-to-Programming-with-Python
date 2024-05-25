def main():
    plate = input("Plate: ")
    # plate = "GO1DB1"
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    r = True
    if 2 <= len(s) <= 6:
        if all(i.isalpha() for i in s[:2]):
            k = next((i for i, char in enumerate(s) if char.isdigit()), -1)
            # print(k)
            if not s[k] == "0":
                # print(s[k:])
                if k == -1 or all(i.isdigit() for i in s[k:]):
                    return True
                else:
                    # print("num")
                    return False
            else:
                # print("zero")
                return False
        else:
            # print("two")
            return False
    else:
        # print("len")
        return False
main()
