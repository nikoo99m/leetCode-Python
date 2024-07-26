def busyStudent(startTime, endTime, queryTime):
    count = 0
    for start, end in zip(startTime, endTime):
        if start <= queryTime <= end:
            count += 1
    return count


# Test cases
print(busyStudent([1, 2, 3], [3, 2, 7], 4))  # Expected output: 1
print(busyStudent([4], [4], 4))  # Expected output: 1
print(busyStudent([1, 1, 1, 1], [1, 3, 2, 4], 7))  # Expected output: 0
