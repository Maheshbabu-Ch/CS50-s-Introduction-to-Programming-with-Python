due = 50
print("Amount Due:",due)
while(due > 0):
    k = int(input("Insert Coin: "))
    if k == 25 or k == 10 or k == 5:
        due -= k
    if due > 0:
        print("Amount Due:",due)
    else:
        print("Change Owed:", abs(due))
