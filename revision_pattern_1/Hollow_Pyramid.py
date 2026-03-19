n =int(input("What height of Pyramid do you want"))
for i in range(n):
    #spaces
    for j in range(n - i -1):
        print(" ",end="")

    for k in range(2*i + 1):
    #i == 0 or i == n-1 used to fill up the last line with stars
    #k == 0 or k == 2*i used to fill up boundaries with star
        if k == 0 or k == 2*i or i==0 or i==n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
