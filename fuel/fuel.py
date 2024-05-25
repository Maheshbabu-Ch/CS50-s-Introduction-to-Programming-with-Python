# while True:
#     try:
#         x,y = map(int,input("Fraction: ").strip().split("/"))
#         r = round(x/y * 100)
#     except (ValueError, ZeroDivisionError):
#         continue
#     else:
#         if r <= 1:
#             print("E")
#         elif 2 < r < 99:
#             print(f"{r}%")
#         elif 99 <= r<= 100:
#             print("F")
#         else:
#             continue
#         break

def main():
    while True:
        try:
            t = input("Fraction: ")
            conv = convert(t)
            print(gauge(conv))
            break
        except (ZeroDivisionError, ValueError):
            continue

def convert(fraction):
    try:
        x,y = map(int,fraction.strip().split("/"))
        if y == 0:
            raise ZeroDivisionError
        r = round(x/y * 100)
        return r
    except ValueError:
        raise ValueError

def gauge(r):
        if r <= 1:
            return "E"
        elif 2 < r < 99:
            return f"{r}%"
        elif 99 <= r<= 100:
            return "F"
        else:
            raise ValueError

if __name__ == "__main__":
    main()
