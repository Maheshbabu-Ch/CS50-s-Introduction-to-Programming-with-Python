import inflect
p = inflect.engine()
s ="Adieu, adieu, to"
l = []
while True:
    try:
        x = input("Name: ")
        l.append(x)
    except EOFError:
        # t = ""
        # if len(l) == 1:
        #     print(s, l[-1])
        # elif len(l) == 2:
        #     print(s , " and ".join(l))
        # else:
        #     # t += ", ".join(l[:-1])
        #     # t += l[-2] + " and " + l[-1]
        #     # print(s,t)
        #     for i in l[:-2]:
        #         t += i + ", "
        #     t += f"{l[-2]} and {l[-1]}"
        #     print(s,t)
        print(s, gaep.join(l))
        break
# Adieu, adieu, to Liesl, Friedrich, and Louisa
