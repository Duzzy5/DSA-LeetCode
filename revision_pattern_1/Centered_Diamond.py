n= int(input("Enter the triangle peak, when measured from the left to right:"))
for i in range(2 * n - 1):
    if i < n:
        #spaces
        for j in range(n - 1 - i):
            print(" ",end="")
        for k in range(i + 1):
            print("*",end="")
        print()
    else:
        for l in range(i - n + 1):
            print(" ",end="")
        for m in range(2*n-i-1):
            print("*",end="")
        print()
