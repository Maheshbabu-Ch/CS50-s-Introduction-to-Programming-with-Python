from PIL import Image,ImageOps
import sys
import os

try:
    e = ['jpg','png','jpeg']
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        i,j = sys.argv[1].split(".")[1], sys.argv[2].split(".")[1]
        if i not in e or j not in e:
            sys.exit("Invalid output")
        elif i != j:
            sys.exit("Input and output have different extensions")

    shirt = Image.open("shirt.png")
    size = shirt.size
    # print(size)
    mod = Image.open(sys.argv[1])
    mod = ImageOps.fit(mod,size)
    mod.paste(shirt,shirt)
    mod.save(sys.argv[2])
except FileNotFoundError:
    print("Input does not exist")
