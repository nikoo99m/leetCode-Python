def unique_occurrences(arr):

    frequency_dict = {}
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    frequency_set = set()
    for frequency in frequency_dict.values():
        if frequency in frequency_set:
            return False
        frequency_set.add(frequency)

    return True


arr1 = [1, 2, 2, 1, 1, 3]
print(unique_occurrences(arr1))

arr2 = [1, 2, 2, 1, 1, 2]
print(unique_occurrences(arr2))
