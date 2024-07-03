def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    array = [0, 1]
    for i in range(2, n + 1):
        array.append(array[i - 1] + array[i - 2])

    return array[n]

    # Test cases


n1 = 0
print(f"fib({n1}) = {fib(n1)}")  # Output: 0

n2 = 1
print(f"fib({n2}) = {fib(n2)}")  # Output: 1

n3 = 2
print(f"fib({n3}) = {fib(n3)}")  # Output: 1

n4 = 3
print(f"fib({n4}) = {fib(n4)}")  # Output: 2

n5 = 10
print(f"fib({n5}) = {fib(n5)}")  # Output: 55
