def union(arr1, arr2):
    i = j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            val = arr1[i]
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            val = arr1[i]
            i += 1
        else:
            val = arr2[j]
            j += 1

        if not result or result[-1] != val:
            result.append(val)

    while i < len(arr1):
        if result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1

    while j < len(arr2):
        if result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1

    return result
