def fizzBuzz(n: int):
    array = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            array.append("FizzBuzz")
        elif i % 3 == 0:
            array.append("Fizz")
        elif i % 5 == 0:
            array.append("Buzz")
        else:
            array.append(str(i))

    return array


if __name__ == "__main__":
    n = 15  # You can change this value to test with different inputs
    result = fizzBuzz(n)

    for s in result:
        print(s)
