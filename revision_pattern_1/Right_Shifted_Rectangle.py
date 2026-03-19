n = int(input("enter the unit of which you want to make right shifted rectangle"))
for i in range(n):
    for k in range(i):
        print(" ",end="")
    for j in range(n):
        print("*",end="")
    print("")
