def lessThan4(aList):
    result = []
    for item in aList:
        if len(item) < 4:
            result.append(item)
    return result

print(lessThan4(["apple", "cat", "dog", "banana"]))