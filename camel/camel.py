s = input("camelCase: ")
# helloMrNookaL
t = ""
for i in range(len(s)-1):
    t += s[i]
    if s[i+1].isupper():
        t += "_"
t += s[-1]
print(t.lower())
