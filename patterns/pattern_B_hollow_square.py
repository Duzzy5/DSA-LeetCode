n = int(input("Enter what unit length of square border do you want?"))
p= n-1
for i in range(n):
    if i==0 or i==p:
        for j in range(n):
            print("*",end="")
    else:
        for k in range(n):
            if k==0 or k==p:
                print("*",end="")
            else:
                print(" ",end="")
    print("")
