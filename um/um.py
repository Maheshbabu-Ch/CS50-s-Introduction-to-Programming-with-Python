import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    a = re.findall(r"\b(um)\b",s,re.I)
    return len(a)



if __name__ == "__main__":
    main()
