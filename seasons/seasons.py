from datetime import date
import sys
import inflect

def main():
    print(convo(input("Date of Birth: ")))

def convo(s):
    try:
        p = inflect.engine()
        year,month,day = map(int,s.split("-"))
        # year,month,day = 1970,1,1
        d = date(year,month,day)
        t = date.today()
        # t = date(2000,1,1)
        k = (t-d).days * 24 * 60
        return p.number_to_words(k, andword="").capitalize() + " minutes"
        # print(dir(str))
        # print(d)
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
