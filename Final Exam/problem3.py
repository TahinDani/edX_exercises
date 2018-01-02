# Suppose you are given two strings (they may be empty), s1 and s2. 
# You would like to "lace" these strings together, by successively alternating 
# elements of each string (starting with the first character of s1). If one 
# string is longer than the other, then the remaining elements of the longer 
# string should simply be added at the end of the new string. For example, if 
# we lace 'abcd' and 'efghi', we would get the new string: 'aebfcgdhi'.


def laceStrings(s1, s2):
    result = ""
    len_s1 = len(s1)
    len_s2 = len(s2)
    index = 0
    while len_s1 and len_s2:
        result += s1[index]
        result += s2[index]
        index += 1
        len_s1 -= 1
        len_s2 -= 1
    while len_s1 > 0:
        result += s1[index]
        index +=1
        len_s1 -=1
    while len_s2 > 0:
        result += s2[index]
        index += 1
        len_s2 -= 1
    print(result)

laceStrings('acegi', 'bdfh')
        