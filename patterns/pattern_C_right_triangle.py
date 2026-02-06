n = int(input("Enter what unit length of triangle do you want?"))
p = 1
for i in range(n):
    for j in range(p):
        print("*",end="")
    p=p+1
    print()
