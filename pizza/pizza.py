import sys
import csv
from tabulate import tabulate

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")

    with open(sys.argv[1], "r") as file:
        d = csv.reader(file, delimiter=",")
        a = []
        for i in d:
            a.append(i)
        print(tabulate(a[1:], headers = a[0], tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
