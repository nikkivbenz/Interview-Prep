import unittest
#given a string, convert whitespace to % 


def urlify(string, lenString):
    strSplit = string.split()
    #splits by whitespace then joins with % char 
    return "%".join(strSplit)

class URLifyTestCase(unittest.TestCase):
    test_cases = [("idk how  this works", "idk%how%this%works"), 
    ("Forever a l one", "Forever%a%l%one")]

    def test_urlify(self): 
        for test_string, expected in self.test_cases:
            testCaseOutput = urlify(test_string, 0)
            assert testCaseOutput == expected
        
unittest.main()


