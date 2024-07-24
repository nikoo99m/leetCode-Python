def matrixDiagnol(matrix):
    sum = 0
    n = len(matrix)
    for i in range(0, n):
        sum += matrix[i][i]
        if i != n - 1 - i:
            sum += matrix[i][n - 1 - i]
    return sum


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = matrixDiagnol(matrix)
    print("The sum of the diagonals is:", result)
