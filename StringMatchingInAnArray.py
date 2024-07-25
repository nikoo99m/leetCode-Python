def matchingStrings(array):
    result = []
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if i != j and array[i] in array[j]:
                result.append(array[i])
                break

    return result


words = ["mass", "as", "hero", "superhero"]
print(matchingStrings(words))
