def solution(array):
    x = len(array) / 2
    for i in range(0, len(array)):
        count = 0
        for j in range(0, len(array)):
            if array[i] == array[j]:
                count += 1

        if count > x:
            return array[i]

    return -1


nums = [3, 2, 3]
print(solution(nums))
