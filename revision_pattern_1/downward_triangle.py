n= int(input("enter the height of your hollow downward triangle"))
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(2 * n - 1 - 2 * i):
        print("*",end="")
    print()
