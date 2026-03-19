n=int(input("enter units for downwards triangle"))
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(n * 2 - 1 - 2 * i):
        if k==0 or k ==(2 * n - 2 - 2 * i)or i==0:
            print("*",end="")
        else:
            print(" ",end="")
    print()
