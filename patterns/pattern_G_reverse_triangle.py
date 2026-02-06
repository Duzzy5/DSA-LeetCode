n = int(input("Enter what unit length of triangle do you want?"))
m=(n*2)-1

for i in range(n):
    o=m-(2*i)
    for j in range(o):
        print("*",end="")
    print()
       
