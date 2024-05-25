import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        #  s = "12:59 AM to 12:00 PM"
        a = re.search(r"^\d{1,2}(:\d{2})? (AM|PM) to \d{1,2}(:\d{2})? (AM|PM)",s)
        if a :
        # print("Match")
            time = s.split(" to ")
            ans = []
            for i in time:
                # print(i)
                if ":" in i:
                    h,m = map(int,i.split(" ")[0].split(":"))
                else:
                    h = int(i.split(" ")[0])
                    m = 0
                t = i.split(" ")[1]
                if 1 <= h <= 12 and 0 <= m <= 59:
                    # print(h,m)
                    if t == 'PM':
                        if h != 12:
                            h += 12
                    else:
                        if h == 12:
                            h = 0
                    ans.append(f"{h:02d}:{m:02d}")
                else:
                    # print("not")
                    raise ValueError
            res = " to ".join(ans)
            return res

            # print(time)
        else:
            # print("Not Match")
            raise ValueError
    except ValueError:
        raise ValueError


...


if __name__ == "__main__":
    main()
