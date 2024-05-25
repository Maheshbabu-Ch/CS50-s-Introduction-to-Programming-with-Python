def convert(text):
    l = text.split(" ")
    for i in range(len(l)):
        if l[i] == ":)":
            l[i] = "🙂"
        if l[i] == ":(":
            l[i] = "🙁"

    return " ".join(l)
def __main__():
    print(convert(input()))

__main__()
