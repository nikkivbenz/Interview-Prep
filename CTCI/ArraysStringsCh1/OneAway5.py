import unittest

from collections import Counter

def oneAway(string1, string2): 
    pass


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
