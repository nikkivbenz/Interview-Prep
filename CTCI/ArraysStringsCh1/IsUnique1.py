from collections import Counter
#determines if all characters in a string are unique


def isUnique(string): 
    strSet = set(string)
    n = len(string)
    lenSet = len(strSet)

    if n == lenSet: 
        return True
    return False


def isUniqueVersion2(string): 
    counterString = Counter(string) 
    highest = counterString.most_common(1)[0] 
    if highest[1] > 1: 
        return False
    return True

def testing(): 
    test1 = "barth"
    test2 = "barthA"
    test3 = "pop"
    print(isUnique(test1))
    print(isUnique(test2))
    print(isUnique(test3))


    print(isUniqueVersion2(test1))
    print(isUniqueVersion2(test2))
    print(isUniqueVersion2(test3))

testing()