s = input("File name: ").lower().strip().split(".")[-1]
# print(s)
match s:
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "gif" | "png":
        print("image/"+s)
    case "pdf" | "zip":
        print("application/"+s)
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
