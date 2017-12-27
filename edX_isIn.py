def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '' or len(aStr) == 1:
        return False
    half_point = int((len(aStr))/2)
    test_char = aStr[half_point]
    
    if char == test_char:
        return True
    elif char > test_char:
        return isIn(char, aStr[half_point:])
    elif char < test_char:
        return isIn(char, aStr[:half_point])
    

print(isIn('a', ''))