def summaryRanges(array):
    result = []
    if not array:
        return result
    start = array[0]
    for i in range(1, len(array) + 1):
        if i == len(array) or array[i] != array[i - 1] + 1:
            if array[i - 1] == start:
                result.append(str(start))
            else:
                result.append(f"{start}->{array[i - 1]}")
            if i < len(array):
                start = array[i]
    return result


nums1 = [0, 1, 2, 4, 5, 7]
print(summaryRanges(nums1))  # Output: ['0->2', '4->5', '7']

nums2 = [0, 2, 3, 4, 6, 8, 9]
print(summaryRanges(nums2))  # Output: ['0', '2->4', '6', '8->9']
