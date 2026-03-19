n = int(input("enter the unit length of traingle that you wanna built:"))
for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(i + 1):
        print("*",end="")
    print("")
