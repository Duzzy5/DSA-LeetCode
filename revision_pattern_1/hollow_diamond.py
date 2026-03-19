n= int(input("Enter the units for hollow pyramid: "))
#upper hollow pyramid
for i in range(n):
    for j in range(n - i - 1):
        print(" ",end="")
    for k in range(2 * i + 1):
        if i==0 or i==n-1 or k==0 or k==2*i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
#lower hollow pyramid
for i in range(n-1):
    for j in range(i+1):
        print(" ",end="")
    for k in range(2 * n - 3 - 2 * i):
        if k==0 or k == (2*n - 4 - 2*i):
            print("*",end="")
        else:
            print(" ",end="")
    print()
