import unittest
import itertools

def palindromePermutation(string, testString): 
    allPermutations = 


class TestPalindromePermutation(unittest.TestCase): 
    test_cases = [("a", "ab", True()]

    def test_palindrome_permutation(self): 
        for string, testString, expected in test_cases: 
            result = palindromePermutation(testString)
            assert result == expected

unittest.main()
