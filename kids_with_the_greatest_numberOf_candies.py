def kidsWithCandies(candies, extraCandies):

    maxCandies = max(candies)

    result = []

    for candy in candies:
        result.append(candy + extraCandies >= maxCandies)

    return result


if __name__ == "__main__":

    candies1 = [2, 3, 5, 1, 3]
    extraCandies1 = 3
    print(kidsWithCandies(candies1, extraCandies1))

    candies2 = [4, 2, 1, 1, 2]
    extraCandies2 = 1
    print(kidsWithCandies(candies2, extraCandies2))

    candies3 = [12, 1, 12]
    extraCandies3 = 10
    print(kidsWithCandies(candies3, extraCandies3))
