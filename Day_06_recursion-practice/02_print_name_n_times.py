# Prints a given name n times using recursion
def print_name_n_times(name, n):
    if n == 0:
        return

    print(name)
    print_name_n_times(name, n - 1)


name = input("Enter name: ")
n = int(input("Enter n: "))
print_name_n_times(name, n)
