import emoji
x = input("Input: ").strip()
em = x[x.find(":"):x.rfind(":")+1]
t = emoji.emojize(em, language = "alias")
print("Output:",x.replace(em,t))

