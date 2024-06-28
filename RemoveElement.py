def remove(array, num):
    x = 0
    for i in range(len(array)):
        if array[i] != num:
            array[x] = array[i]
            x += 1
    return x


nums = [1, 7, 2, 7, 3, 5, 71]

new_length = remove(nums, 7)
print(f"New length: {new_length}")
print(f"Array after removing : {nums[:new_length]}")
