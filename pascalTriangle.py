def generate(numRows):
    triangle = []

    if numRows <= 0:
        return triangle

    # First row is always [1]
    triangle.append([1])

    for i in range(1, numRows):
        prev_row = triangle[i - 1]
        curr_row = [1]  # First element of each row is always 1

        # Each triangle element (except the first and last of each row) is equal to
        # the sum of the elements above-and-to-the-left and above-and-to-the-right.
        for j in range(1, i):
            curr_row.append(prev_row[j - 1] + prev_row[j])

        curr_row.append(1)  # Last element of each row is always 1
        triangle.append(curr_row)

    return triangle


# Example usage
if __name__ == "__main__":
    numRows = 5
    result = generate(numRows)
    for row in result:
        print(row)
