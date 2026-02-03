#using 1 loop
def tp(xx):
    n = len(xx)
    m = n // 2
    b = []

    for i in range(m):
        b.append(xx[i])
        b.append(xx[i + m])

    return b

n = int(input("what length of array do you want: "))
a = []
print("first enter the value of all x then all y")
for i in range(0,n):
    a.append(int(input()))

#after shuffling 
sp = tp(a)
print(sp)

#using 2 loops
def tp(xx):
    n=len(xx)
    b = []
    m=(n//2)
    for i in range (0,n):
        b.append(0)
    b[0]=xx[0]
    for i in range (0,m):
        b[i] = xx[2*i]
        b[m+i]=xx[(2*i)+1]
    print(b)
    return b
    

#SHUFFLE THE ARRAY
n = int(input("what length of array do you want: "))
a = []
print("first enter the value of all x then all y")
for i in range(0,n):
    a.append(int(input()))

#after shuffling 
sp = tp(a)
print(sp)
