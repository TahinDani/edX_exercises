def uniqueValues(aDict):
    result = []
    for key in aDict:
        current_value = aDict[key]
        counter = 0
        for k,v in aDict.items():
            if v == current_value:
                counter += 1
        if counter < 2:
            result.append(key)
    return result

print(uniqueValues({'a':1, 'b':2, 'c':2, 'd': 3}))
