d = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        x = input("Date: ")
        if '/' in x:
            month,day,year = map(int,x.split("/"))
        elif "," in x:
            month, day, year = map(str.strip, x.replace(",","").split(" "))
            month = d.index(month) + 1
            day = int(day)
            year = int(year)
        else:
            continue
        if day > 31 or month > 12:
            continue
    except ValueError:
        continue
    else:
        print(f"{year}-{month:02}-{day:02}")
        break


    