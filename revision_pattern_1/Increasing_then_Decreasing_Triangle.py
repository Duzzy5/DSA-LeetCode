n= int(input("Enter the triangle peak, when measured from the right to left:"))
for i in range(2 * n - 1):
    #upper tiangle
    if i<n:
        for j in range(i + 1):
            print("*",end="")
    else:
        for k in range(2 * n - 1 - i):
            print("*",end="")
    print()
