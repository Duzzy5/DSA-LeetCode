n = int(input("enter what length of diamond you want from teh centre"))
if n ==1 or n==2:
    print("not possible")
else:
    for i in range(n):
        for j in range(n - i - 1):
            print(" ",end="")
        for k in range(2 * i + 1):
            print("*",end="")
        print("")
    for i in range(n - 1):
        for j in range(i + 1):
            print(" ",end="")
        for k in range(2 * n - 3 - 2 *i) :#n*2 - 2*i -3):
            print("*",end="")
        print("")
