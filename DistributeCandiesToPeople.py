def distribute_candies(candies, num_people):
    distribution = [0] * num_people
    i = 0

    while candies > 0:
        distribution[i % num_people] += min(candies, i + 1)
        candies -= i + 1
        i += 1

    return distribution


candies = 13
num_people = 3

result = distribute_candies(candies, num_people)

for num in result:
    print(num, end=" ")
