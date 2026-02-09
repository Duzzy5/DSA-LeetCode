#prints a message n times
def print_n_times(n):
    if n == 0:
        return
    print("hello")
    print_n_times(n-1)

print_n_times(5)
