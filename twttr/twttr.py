# s = "Twitteringtheworld of my own falaxy"

# print("Output:",s)
def main():
    s = input("Input: ")
    o = shorten(s)
    print("Output:",o)


def shorten(word):
    vowels = ['a','e','i','o','u']
    vowels += [i.upper() for i in vowels]
    for i in vowels:
        word = word.replace(i,"")
    return word


if __name__ == "__main__":
    main()
