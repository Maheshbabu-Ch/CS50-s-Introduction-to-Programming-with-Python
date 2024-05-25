import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # import re
# s = '<iframe src = "https://www.youtube.com/sashgfakfah">'
    a = re.search(r'^<.*(src=("(.+youtube[^\ ].+)")).*>', s)
    if a:
        # print(a.group(2))
        b = re.sub(r"http(s)?://(www.)?youtube.com/embed","https://youtu.be",a.group(3))
        return b
    else:
        return "None"


if __name__ == "__main__":
    main()
