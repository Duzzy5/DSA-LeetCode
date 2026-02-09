# Prints numbers from n to 1 using recursion
def print_n_to_1(n):
    if n == 0:
        return

    print(n)
    print_n_to_1(n - 1)


print_n_to_1(5)
