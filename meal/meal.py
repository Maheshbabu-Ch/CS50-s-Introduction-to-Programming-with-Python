def main():
    time = input("What time is it? ")
    a = convert(time)
    if 7 <= a <= 8:
        print("breakfast time")
    elif 12 <= a <= 13:
        print("lunch time")
    elif 18 <= a <= 19:
        print("dinner time")



def convert(time):
    h,m = map(float, time.split(":"))
    m = (m / 60)mkdir 
    return h+m


if __name__ == "__main__":
    main()
