def transpose(matrix):

    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


if __name__ == "__main__":

    matrix = [[1, 2, 3], [4, 5, 6], [3, 5, 9]]

    transposed_matrix = transpose(matrix)

    print("Original Matrix:")
    for row in matrix:
        print(row)

    print("\nTransposed Matrix:")
    for row in transposed_matrix:
        print(row)
