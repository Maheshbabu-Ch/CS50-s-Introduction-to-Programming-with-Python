def main():
    s = input("Greeting: ").strip()
    ans = value(s)
    print(ans)


def value(greeting):
    greeting = greeting.lower()
    a = ""
    if greeting.startswith("hello"):
        a = "$0"
    elif greeting.startswith("h"):
        a = "$20"
    else:
        a = "$100"
    return a

if __name__ == "__main__":
    main()
