import sys
from pyfiglet import Figlet

if len(sys.argv) < 3:
        sys.exit("Invalid usage")
figlet = Figlet()
l = figlet.getFonts()

try:
    c, font = sys.argv[1], sys.argv[2]
    if c == "-f" or c == "--font":
        if font in l:
            figlet.setFont(font=font)
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
    text = input("Input: ")
    print(figlet.renderText(text))
except IndexError:
    sys.exit("Invalid usage")
