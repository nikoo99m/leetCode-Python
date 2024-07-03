def constructRectangle(area):
    outPut = [0, 0]
    minDifference = float("inf")

    for i in range(1, area + 1):
        if area % i == 0:
            j = area // i
            difference = abs(i - j)

            if difference < minDifference:
                outPut[0] = max(i, j)
                outPut[1] = min(i, j)
                minDifference = difference

    return outPut


# Example usage:
print(constructRectangle(4))  # Output: [2, 2]
print(constructRectangle(37))  # Output: [37, 1]
print(constructRectangle(122122))  # Output: [427, 286]
