import unittest
from collections import Counter


def correctPalindromePermutation(string):   
    #gets rid of whitespace and makes all lower case since Counter considers uppercase and lowercase separately 
    string = string.replace(" ", "").lower()
    strCounter = Counter(string) 

    #theyre can only be 1 odd value if any; needs to be symmetric and if theres 1 odd value then that is the middle element 
    #if there's more than one, then the string isn't symmetric 
    sumOdds = sum(x % 2 for x in strCounter.values())
    if sumOdds > 1: 
        return False
    return True


class TestPalindromePermutation(unittest.TestCase): 
    test_cases = [("taco cat", True), ("tacooppapcat", False)]

    def test_correct_palindrome_permutation(self): 
        for string, expected in self.test_cases: 
            result = correctPalindromePermutation(string)
            assert result == expected

unittest.main()

# print(correctPalindromePermutation("tacooppapcat"))
