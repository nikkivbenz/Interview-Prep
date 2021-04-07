import unittest

from collections import Counter

def oneAway(string1, string2): 
    str1C = Counter(string1) 
    str2C = Counter(string2) 

    s1Set = set(str1C.elements())
    s2Set = set(str2C.elements())
    print(s1Set)
    print(s2Set)

    #get unicode of each letter and multiple * value
    #compare their sums, should be a difference of 1 


class TestOneAway(unittest.TestCase): 
    test_cases = [
                ("pale", "ple", True), 
                ("pales", "pale", True),  
                ("pale", "bale", True),
                ("pale", "bake", False)]

    def test_one_away(self): 
        for str1, str2, expected in self.test_cases: 
            result = oneAway(str1, str2)
            self.assertEquals(result, expected, f"{str1}, {str2} are the errors")




# unittest.main()
oneAway("pale", "bale")
