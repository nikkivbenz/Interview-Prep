import unittest
from collections import Counter

def palindromePermutation(string): 
    #remove all whitespace in the string because it counts in the counter as an element
    string = string.replace(" ", "")

    #counts all the chars in the string 
    strCounter = Counter(string) 

    #counts all the values of each char 
    countCounter = Counter(list(strCounter.values()))

    #a palindrome is only a palindrome if there are the same number of letters of each or there is just 1 letter that has a count of 1 
    #which would be a middle element and all 
    if len(countCounter) > 2: 
        return False
    #else: 
        # just a way to retrieve all the counters of the chars
        # allE = countCounter.most_common(2)
        # since only 1 other char can be a count of 1 (different from the rest), then if it is not 
        # if allE[1][1] != 1: 
        #     print(2)
        #     return False

    return True

def correctPalindromePermutation(string):   
    string = string.replace(" ", "").lower()
    strCounter = Counter(string) 
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
