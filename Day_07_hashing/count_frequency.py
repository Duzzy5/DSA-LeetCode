def count_frequency(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    return freq


if __name__ == "__main__":
    arr = [1, 2, 1, 3, 2, 1]
    result = count_frequency(arr)
    print(result)
