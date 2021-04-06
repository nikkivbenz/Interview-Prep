import itertools as it
from collections import Counter

def isPermutation(a, b): 
    counterA = Counter(a) 
    counterB = Counter(b) 
    if counterA == counterB: 
        return True
    return False
    
print(isPermutation("ba", "ab"))

def isPermutationsVersion2(a, b): 
    #checking a against b
    allPermutations = list(it.permutations(a, len(b)))
    print(allPermutations)
    if allPermutations.count(tuple(b)) > 0: 
        return True
    return False

