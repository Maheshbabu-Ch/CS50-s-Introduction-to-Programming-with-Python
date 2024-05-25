import sys
import csv
try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # else:
    #     if not sys.argv[1].endswith(".py"):4
    #         sys.exit("Not a Python file")
    c = 0
    with open(sys.argv[1], "r") as file:
        # d = csv.reader(file, delimiter=",")
        d = csv.DictReader(file, delimiter=",")
        # print(d.)
        a = []
        for i in d:
            a.append(i)

    with open(sys.argv[2], "w", newline="") as file:
        # k = csv.writer(file, delimiter="\t")
        f = ["first","last","house"]
        k = csv.DictWriter(file, fieldnames=f)
        # print(a)
        # for i,j in a[1:]:
        #     f,l = i.split(",")
        #     k.writerow([f.strip(),l.strip(),j])
        k = csv.DictWriter(file, delimiter=",", fieldnames=f)
        k.writeheader()
        for i in a:
            f,l = i['name'].split(",")
            ag = i['house']
            k.writerow({"first": l.strip(), "last": f.strip(), "house": ag})
        print(k)


except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")


