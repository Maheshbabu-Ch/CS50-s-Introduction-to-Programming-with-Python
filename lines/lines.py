import sys
try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
    c = 0
    with open(sys.argv[1], "r") as file:
        for line in file.readlines():
            if not (line.lstrip() == "" or line.lstrip().startswith("#")):
                c+=1
        print(c)


except FileNotFoundError:
    print("File does not exist")
