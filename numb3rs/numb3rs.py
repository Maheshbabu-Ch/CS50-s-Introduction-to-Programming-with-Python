# import re
# import sys


# def main():
#     print(validate(input("IPv4 Address: ")))


# def validate(ip):
#     try:
#         a = list(map(int,ip.split(".")))
#         if len(a) != 4:
#             return "False"
#         for i in a:
#             if i > 255:
#                 return "False"
#         return "True"
#     except ValueError:
#         return "False"


# ...


# if __name__ == "__main__":
#     main()


import re
import sys


def main():
    if validate(input('IPv4 Address: ')):
        sys.exit("True")
    else:
        sys.exit("False")

def validate(ip):
    a = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$",ip)
    ans = True
    if a :
        # print(a.groups())
        for i in a.groups():
            print(i)
            if int(i) > 255:
                return False
        return ans
    else:
        return False

if __name__ == "__main__":
    main()
