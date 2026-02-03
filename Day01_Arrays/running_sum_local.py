# Running Sum - Local Practice Version
# Author: DUZZY

def tp(ltf):
    nt = len(ltf)

    # creating ans array
    ans = []
    for i in range(0, nt):
        ans.append(0)

    ans[0] = ltf[0]

    # filling running sum
    for i in range(1, nt):
        ans[i] = ans[i-1] + ltf[i]

    return ans


n = int(input("enter n: "))
lt = []

print("Enter numbers one by one")
for i in range(0, n):
    lt.append(int(input()))

rs = tp(lt)
print(rs)
