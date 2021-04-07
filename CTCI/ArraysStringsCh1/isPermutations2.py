import itertools as it
from collections import Counter

#given two strings, decides if they're permutations of one another 

def isPermutation(a, b): 
    counterA = Counter(a) 
    counterB = Counter(b) 

    #if the count of all chars in a and b match each other
    if counterA == counterB: 
        return True
    return False
    
print(isPermutation("ba", "ab"))


