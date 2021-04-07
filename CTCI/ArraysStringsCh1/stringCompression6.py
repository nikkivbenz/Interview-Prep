import unittest

def stringCompression(string):
    n = len(string)
    finalString = ""
    count = 0

    for x in range(0, n):
        if count == 0:
            finalString += string[x]
            count += 1
        else: 
            if string[x] == string[x-1]: 
                count += 1
            else: 
                finalString += str(count)
                finalString += string[x]
                count = 1
    finalString += str(count)
    if len(finalString) < n: 
        return finalString
    else : 
        return string

class TestStringCompression(unittest.TestCase): 
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]

    def test_string_compression(self): 
        for string, expected in self.test_cases: 
            result = stringCompression(string)
            self.assertEqual(result, expected, f"{string}, {expected} caused error")

unittest.main()