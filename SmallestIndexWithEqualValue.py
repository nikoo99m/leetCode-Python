def smallest_equal(nums):
    for i in range(len(nums)):
        if i % 10 == nums[i]:
            return i
    return -1


# Test cases
test_array1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_array2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
test_array3 = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]

print("Test Array 1:", smallest_equal(test_array1))
print("Test Array 2:", smallest_equal(test_array2))
print("Test Array 3:", smallest_equal(test_array3))
